#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 11:54:34 2020

@author: joongsinpark
"""

from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests

from bs4 import BeautifulSoup

#driver = webdriver.Chrome('/Users/joongsinpark/Desktop/chromedriver')
#
#driver.implicitly_wait(3)
#chk_login = 0



def pp_content_crawling():
    print("crawling ppomppu list")
    fout = open("pp_list.txt","w", encoding='UTF8') #게시글 리스트 기록파일 오픈
    i = 2
    #driver.get('http://www.todayhumor.co.kr/board/list.php?table=bestofbest&page=1')
    #driver.implicitly_wait(5)
    #wait = WebDriverWait(driver, 10)
    #element = wait.until(EC.element_to_be_clickable((By.ID, 'logo_line_container')))
    
    chk_error = 1
    chk_index = 0
    
    for p in range(1,2) :     
        driver.get('http://www.ppomppu.co.kr/zboard/zboard.php?id=ppomppu') 
        #driver.get('http://www.ppomppu.co.kr/zboard/zboard.php?id=ppomppu&page=2&divpage=60') 
        
        #driver.implicitly_wait(5)
        req = driver.page_source
        soup = BeautifulSoup(req, 'html.parser')     
    
        no_title=5
        link_no = 1
        
        element_0 = soup.find_all(class_='list0') #홀수번째 글 10개씩 
        element_1 = soup.find_all(class_='list1') #짝수번째 10개씩
        
        #print (element_0[0].prettify())
        
        print (type(element_0[0]))
        print (element_0[0].prettify())
        

        
        
        while(1):
            
            

            chk_index += 1
            '''
            print ("-------------------%d-----------------------" %(chk_index))
            for link in soup.find(class_='list1'):
                print (link)
                
            chk_index += 1
            '''
            if chk_index >= chk_error :
                break
            
        
        
        '''
        for i in range(1,no_title+1) : # # of books
            
            
            
            select_i = 2*i + 4
    
            while(1) : 
                try:
                    
       
                    link_inf = [link_no, no_title, type_title, writer_title, name_title, time_title, recommend_title, link_title]
                    print(link_inf)
                    fout.write("%d\t %s\t %s\t %s\t %s\t %s\t %s\t %s\n"%(link_no, no_title, type_title, writer_title, name_title, time_title, recommend_title, link_title))
                    
                    print("10")
                    
                    break
                except:                
                    req = driver.page_source
                    soup = BeautifulSoup(req, 'html.parser')
                    print("except called")
                    break
                    

            link_no += 1
            chk_index = 1
        '''
    
    fout.close()


def title_modify(name_des):
    
    psd = name_des.split("]")
    mall_name = psd[0].strip("[")
    title_tail = psd[1].rstrip(")")
    title_mod = "[실시간 뽐뿌] " + title_tail + "/" + mall_name + ")"
    
    return title_mod

def title_analysis(title):
    psd = title.replace(']','(').split("(")

    product_inf = ""
    
    for i in range(1,len(psd)-1):
        product_inf += psd[i]
    
    product_inf = product_inf.strip(" ")
    
    price_inf = psd[len(psd)-1].split("/")
    
    price_product = price_inf[0].strip(" ")
    price_delivery = price_inf[1].strip(" ")
    mall = price_inf[2].strip(")")
    
    title_inf = [product_inf, price_product, price_delivery, mall]
    
    return title_inf
    


def timer():
    waiting_time = 30
    for i in range(0, waiting_time) : 
        print("remain sec : %d" %(30-i))
        time.sleep(1)
    print("re-posting")
    
#timer()



def done_list_sync():
    global done_li
    
    fdone = open("done_list_%s.txt" %(today),"r", encoding='UTF8')
    for line in fdone:
        done_no = line.strip("\r\n")
        print(done_no)
        done_li.append(done_no)

def done_listing(no_title):
    print("done_no_listing")
    fout = open("done_list_%s.txt" %(today),"a", encoding='UTF8') #게시글 리스트 기록파일 오픈
    fout.write("%s\n"%(no_title))
    fout.close()        

def chk_done_li():
    global done_li
    print(done_li)

today = time.strftime('%Y-%m-%d', time.localtime(time.time()))

for i in range(1,10):
    done_listing(str(i))

done_li = []

done_list_sync()

print (done_li)

chk_done_li()
    
    
    




    
#pp_content_crawling()
    
    