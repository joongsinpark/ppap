
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests

from bs4 import BeautifulSoup

driver = webdriver.Chrome('/Users/joongsinpark/Desktop/chromedriver')

driver.implicitly_wait(3)


def login_pp():
    driver.get('http://www.ppomppu.co.kr/zboard/zboard.php?id=freeboard')
    driver.find_element_by_xpath('/html/body/div/div[2]/div[3]/div/span[1]/a').click()    
    driver.find_element_by_name('user_id').send_keys('pjs6795')
    driver.find_element_by_name('password').send_keys('1')
    driver.find_element_by_xpath('//*[@id="zb_login"]/ul/a').click()


def write_post():    
    print("wp is called")
    #print(content_li)
    
    title = content_li[0]
    contents = content_li[1]
    
    print(title)
    print(contents)
    
    driver.get('http://www.ppomppu.co.kr/zboard/zboard.php?id=freeboard')
    driver.find_element_by_xpath('/html/body/div[6]/div[2]/div[4]/div[1]/table[4]/tbody/tr[2]/td[2]/nobr/a').click()

        
    # 현재 웹페이지에서 iframe이 몇개가 있는지 변수에 넣고 확인해 봅니다.

    
    """
    print('현재 페이지에 iframe은 %d개가 있습니다.' % len(iframes))
 
    # 배열로된 iframes 변수를 for문을 이용해 하나씩 확인해 봅니다.
    # enumerate() 함수를 사용하면 배열의 index(순번)을 확인할 수 있습니다.
    for i, iframe in enumerate(iframes):
    	try:
    		print('%d번째 iframe 입니다.' % i)
    
    		# i 번째 iframe으로 변경합니다.
    		driver.switch_to_frame(iframes[i])
    
    		# 변경한 iframe 안의 소스를 확인합니다.
    		print(driver.page_source)
    
    		# 원래 frame으로 돌아옵니다.
    		driver.switch_to_default_content()
    	except:
    		# exception이 발생했다면 원래 frame으로 돌아옵니다.
    		driver.switch_to_default_content()
    
    		# 몇 번째 frame에서 에러가 났었는지 확인합니다.
    		print('pass by except : iframes[%d]' % i)
    """
    
    driver.find_element_by_name('subject').send_keys(title)

    driver.find_element_by_xpath('/html/body/div[6]/div[2]/div[4]/div/form/table/tbody/tr/td/table[2]/tbody/tr[6]/td[2]/div[4]/div[6]/div[2]').click()
    
    # 확인된 ifrime으로 변경합니다.
    iframes = driver.find_elements_by_tag_name('iframe')
    driver.switch_to_frame(iframes[1])
    # 본문을 작성하는 editor element를 지정합니다.
    editor = driver.find_element_by_xpath("/html/body")
    # editor element에 글을 작성합니다.
    editor.send_keys(contents)
    
    # ifrime에서 원래 frame으로 돌아옵니다.
    driver.switch_to_default_content()
 
    driver.find_element_by_xpath('/html/body/div[6]/div[2]/div[4]/div/form/table/tbody/tr/td/table[2]/tbody/tr[6]/td[2]/div[4]/div[6]/div[1]').click()
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="save_tmp"]').click()
    time.sleep(3)
    
    driver.switch_to_alert().accept()
    driver.switch_to_alert().dismiss()
    
    
content_li=["title","contents"]
login_pp()
write_post()
