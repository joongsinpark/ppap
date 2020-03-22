#!/usr/bin/env python

import selenium_bundle
import sys
import re
import time


def timer():
    waiting_time = 30
    for i in range(0, waiting_time) :
        print("remain sec : %d" %(30-i))
        time.sleep(1)
    print("re-posting")

def chk_alert(driver):
    try:
        driver.switch_to.alert().accept()
        print("accepted")
#        except:
 #           driver.switch_to.alert().dismiss()
  #          print("dismissed")
    except:
        print("no alert")

def cleanText(readData):

    #텍스트에 포함되어 있는 특수 문자 제거

    text = re.sub('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]', ' ', readData)

    return text


def funcname():
    return sys._getframe(1).f_code.co_name + "() is called (now func)"

def callername():
    return sys._getframe(2).f_code.co_name + "() called (caller)"

def chk_frame(iframes):
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
