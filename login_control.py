import selenium_bundle
import time

global driver

def login_pp():     #다시 수정해야함
    global driver
    driver.get('http://www.ppomppu.co.kr/zboard/zboard.php?id=freeboard')
    driver.find_element_by_name('id').click()
    driver.find_element_by_name('id').send_keys('pjs6795')
    driver.find_element_by_name('pw').click()
    driver.find_element_by_name('pw').send_keys('1')
    driver.find_element_by_xpath('//*[@id="zb_login"]/ul/a').click()

def login_naver(driver):
    driver.get('http://www.naver.com')
    driver.find_element_by_xpath('//*[@id="account"]/div/a/i').click()
    driver.find_element_by_name('id').click()
    driver.find_element_by_name('id').send_keys('hotdeal_pjs')
    driver.find_element_by_name('pw').click()
    driver.find_element_by_name('pw').send_keys('wndtls1004!')
    driver.find_element_by_xpath('//*[@id="log.login"]').click()

    time.sleep(1)
    try:
        driver.find_element_by_name('pw').click()
        driver.find_element_by_name('pw').send_keys('wndtls1004!')
        driver.find_element_by_xpath('//*[@id="chptcha"]').click()

        time.sleep(30)

    except:
        return
