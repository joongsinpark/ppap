import selenium_bundle
import ppinfo
import doneListControl
import pg_support
import login_control
import inspect


options = selenium_bundle.webdriver.ChromeOptions()
#options.add_argument('headless')
#options.add_argument('window-size=1920x1080')
#options.add_argument("disable-gpu")

# UserAgent값을 바꿔줍시다!
options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")

driver = selenium_bundle.webdriver.Chrome('/Users/joongsinpark/Desktop/chromedriver', chrome_options=options)

driver.implicitly_wait(3)

login_control.login_naver(driver)   #네이버 로그인

doneListControl.sync_done_li()

while(1):
    pb = ppinfo.ppboard(driver)
    if pb.list_crawling() == 0:     #다하지 않고 맨 위에꺼만, done_li 비교 후 포스팅
        print("error called")
    # print(inspect.getmembers(pb))
    if pb.content_crawling() == 0:       #pb.content_modify()
        print("error")
        break
    pb.title_modify()
    pb.content_modify()
    pb.nb_post()
    pg_support.timer()
