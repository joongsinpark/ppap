#!/usr/bin/env python3
# -*- coding: utf-8 -*-



from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests
import re

from bs4 import BeautifulSoup

options = webdriver.ChromeOptions()
#options.add_argument('headless')
#options.add_argument('window-size=1920x1080')
#options.add_argument("disable-gpu")

# UserAgent값을 바꿔줍시다!
options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")

driver = webdriver.Chrome('/Users/joongsinpark/Desktop/chromedriver', chrome_options=options)

driver.implicitly_wait(3)

def login_naver():
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

        time.sleep(15)

    except:
        return


login_naver()

driver.get('https://blog.naver.com/hotdeal_pjs?Redirect=Write&categoryNo=9')

hash_li = ['실시간', '뽐뿌', '미샤', '포맨', '익스트림', '리뉴', '남성', '스킨로션', '0', '11번가']
