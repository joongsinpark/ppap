# -*- coding: utf-8 -*-
"""
humor_post.py - 오유 -> 뽐뿌 포스팅 파일
pp_posting.py - 뽐뿌 -> 네이버 블로그 포스팅 파일

"""








chk_login = 0



def login_pp():     #다시 수정해야함
    driver.get('http://www.ppomppu.co.kr/zboard/zboard.php?id=freeboard')
    driver.find_element_by_name('id').click()
    driver.find_element_by_name('id').send_keys('pjs6795')
    driver.find_element_by_name('pw').click()
    driver.find_element_by_name('pw').send_keys('1')
    driver.find_element_by_xpath('//*[@id="zb_login"]/ul/a').click()

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



def done_listing(no_title):
    print("done_no_listing")
    fout = open("done_list_%s.txt" %(today),"a", encoding='UTF8') #게시글 리스트 기록파일 오픈
    fout.write("%s\n"%(no_title))
    fout.close()

def cleanText(readData):

    #텍스트에 포함되어 있는 특수 문자 제거

    text = re.sub('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]', ' ', readData)

    return text







def nb_post(content_li):
    print("naver blog posting")

    #print(content_li)
    #content_li = [no_title, type_title, writer_title, name_title, time_title, recommend_title, link_title, content]

    #----------------작성할 데이터 변수할당----------------
    no_des = content_li[0]
    type_des = content_li[1].strip()
    writer_des = content_li[2]
    name_des = content_li[3]
    time_des = content_li[4]
    recommend_des = content_li[5]
    link_des = content_li[6]
    descript = content_li[7]

#    [실시간 뽐뿌] 심플 논슬립 옷걸이 30P (6,900원/무료배송) - 페이코 쿠폰 소진용/인터파크)





#    print(title)
#    print(descript)


    #---------------- 글쓰기 창 진입 / 작성 ----------------
    type_li = ["","","","","","","","","","컴퓨터", "디지털", "식품/건강", "서적", "가전/가구", "육아", "상품권", "의류/잡화", "화장품", "등산/캠핑", "기타"]

    type_footer = str(type_li.index(type_des))

    type_link = "https://blog.naver.com/hotdeal_pjs/postwrite?categoryNo=" + type_footer
    print (type_link)

    print("1")
    #driver.get('http://www.ppomppu.co.kr/zboard/zboard.php?id=freeboard')

    driver.get(type_link)


    print("2")

    while(1):
        try:
            driver.find_element_by_name('post.title').click()
            break
        except:
            login_naver()

    print("3")

    driver.find_element_by_name('post.title').send_keys(name_des)
    print("4")

    #---------------- iframe이 사용된 에디터 처리 ----------------

    # 현재 웹페이지에서 iframe이 몇개가 있는지 변수에 넣고 확인해 봅니다.

    #driver.find_element_by_xpath('//*[@id="se2_iframe"]').click()


    driver.find_element_by_xpath('//*[@id="smart_editor2_content"]/div[5]/ul/li[2]/button').click()
    driver.find_element_by_xpath('//*[@id="smart_editor2_content"]/div[4]/textarea[1]').send_keys(descript)
    time.sleep(10)
    driver.find_element_by_xpath('//*[@id="btn_submit"]/img').click()
    time.sleep(1)
    try:
        chk_alert(driver)
    except:
        print("no alert")

    done_listing(no_des)


    #chk_out = 0
    # 확인된 ifrime으로 변경합니다.
'''
    while(1):
        try :
            iframes = driver.find_elements_by_tag_name('iframe')
            print("5")

            chk_frame(iframes)
            print("6")

            print("1")
            driver.switch_to.frame(iframes[6])      #뽐뿌 - 2번째 // 네이버 - 6번째
            # 본문을 작성하는 editor element를 지정합니다.
            print("2")

            editor = driver.find_element_by_xpath('/html/body')

            print("3")
            # editor element에 글을 작성합니다.
#            driver.implicitly_wait(5)

            #---------------- 본문 + 추가할 내용 작성 ----------------

            editor.send_keys(descript+"<br>출처:뽐뿌")
            driver.implicitly_wait(10)
            time.sleep(5)

            # ifrime에서 원래 frame으로 돌아옵니다.
            #driver.switch_to.default_content()
            #time.sleep(5)

            print("5")
            #자게 글 작성

            #---------------- 일반 에디터로 진입 ----------------
#            driver.find_element_by_xpath('/html/body/div[6]/div[2]/div[4]/div/form/table/tbody/tr/td/table[2]/tbody/tr[8]/td[2]/div[4]/div[6]/div[1]').click()
#            print("6")
#
#            time.sleep(3)
#            driver.implicitly_wait(3)

            #---------------- ok버튼 입력 및 종료 ----------------
            #driver.find_element_by_xpath('//*[@id="save_tmp"]').click()
            driver.find_element_by_xpath('//*[@id="btn_submit"]/img').click()
            print("7")

            chk_alert()

            break

        except:
            #---------------- iframe 작업 내부에서 오류가 난 경우 메인 컨텐츠로 회귀 ----------------
            print("writing contents")
            driver.switch_to_default_content()
            if chk_out >= 5:
                break
            chk_out +=1
'''
def done_list_sync():
    global done_li

    print("done_list_sync is called")

    yesterday = time.strftime('%Y-%m-%d', time.localtime(time.time()-86400))

    try:
        print("done_list is loaded")
        fdone = open("done_list_%s.txt" %(today),"r", encoding='UTF8')

        for line in fdone:
            done_no = line.strip("\r\n")
#            print(done_no)
            done_li.append(done_no)

    except:
        print("done_list is made")
        fdone = open("done_list_%s.txt" %(today),"a", encoding='UTF8')
        fdone.close()

    try:
        print("yesterday_done_list is loaded")
        fdone_pre = open("done_list_%s.txt" %(yesterday),"r", encoding='UTF8')

        for line in fdone_pre:
            done_no = line.strip("\r\n")
#            print(done_no)
            done_li.append(done_no)

    except:
        print("yesterday_done_list is made")
        fdone_pre = open("done_list_%s.txt" %(yesterday),"a", encoding='UTF8')
        fdone_pre.close()
#        fdone.close()

    print("done_list_sync end")



#----------------오유 베오베 글 크롤링----------------
def pp_list_crawling():
    print("crawling ppomppu list")

    global done_li
    global pre_content_no
    global crawled_li
    print(pre_content_no)

    time.sleep(3)

    driver.get('http://www.ppomppu.co.kr/zboard/zboard.php?id=ppomppu&page=1&divpage=60')
    driver.implicitly_wait(5)
    time.sleep(2)
    req = driver.page_source
    soup = BeautifulSoup(req, 'html.parser')

    try:
        no_title = soup.select('#revolution_main_table > tbody > tr:nth-child(6) > td:nth-child(1)')[0].text.strip("\n").strip("\t")
    except:
        no_title = soup.select('#revolution_main_table > tbody > tr:nth-child(4) > td:nth-child(1)')[0].text.strip("\n").strip("\t")


    if str(pre_content_no) == str(no_title) :
        print("duplicated")
        return

    else:
        crawled_li =[]

#    i = 2
#    fout = open("pp_list_%s.txt" %(today),"w", encoding='UTF8') #게시글 리스트 기록파일 오픈

    chk_error = 5
    chk_index = 1
    link_no = 1
    max_page_search = 5

    for p in range(1,max_page_search+1) :
        driver.get('http://www.ppomppu.co.kr/zboard/zboard.php?id=ppomppu&page=%d&divpage=60' % p)
        req = driver.page_source
        soup = BeautifulSoup(req, 'html.parser')

        no_title=20

        for i in range(1,no_title+1) : # # of product

            select_i = 2*i + 4

            while(1) :
                try:
                    print("lc-1")
                    link_header = "http://www.ppomppu.co.kr/zboard/view.php?id=ppomppu&page=2&divpage=60&no="
                    print("lc-2")
                    no_title = soup.select('#revolution_main_table > tbody > tr:nth-child(%d) > td:nth-child(1)'%(select_i))[0].text.strip("\n").strip("\t")
#                    print(no_title)
#                    print(type(no_title))

                    if no_title in done_li:
                        print("This is in done_li. Skipped (pp_list_crawling)")
                        break

                    print("lc-3")
                    link_title = (link_header + no_title).strip("\t")
                    print("lc-4")
                    type_title = soup.select('#revolution_main_table > tbody > tr:nth-child(%d) > td.han4.list_vspace > nobr'%(select_i))[0].text
                    print(type_title)
                    print("lc-5")
                                            #revolution_main_table > tbody > tr:nth-child(6) > td.han4.list_vspace > nobr
                    try:
                        writer_title = soup.select('#revolution_main_table > tbody > tr:nth-child(%d) > td:nth-child(3) > div > nobr > a > span'%(select_i))[0].text
                    except:
                        writer_title = soup.select('#revolution_main_table > tbody > tr:nth-child(%d) > td:nth-child(3) > div > nobr > a > img'%(select_i))[0].attrs['alt']
                    print("lc-6")

                    name_title = soup.select('#revolution_main_table > tbody > tr:nth-child(%d) > td:nth-child(4) > table > tbody > tr > td:nth-child(2) > a > font'%(select_i))[0].text
                    print("lc-7")

                    time_title = soup.select('#revolution_main_table > tbody > tr:nth-child(%d) > td:nth-child(5) > nobr'%(select_i))[0].text
                    print("lc-8")

                    recommend_title = soup.select('#revolution_main_table > tbody > tr:nth-child(%d) > td:nth-child(6)'%(select_i))[0].text
                    print("lc-9")

                    click_no = soup.select('#revolution_main_table > tbody > tr:nth-child(%d) > td:nth-child(7)'%(select_i))[0].text
    #                    print(click_no)
                    print("lc-10")

                    link_inf = [link_no, no_title, type_title, writer_title, name_title, time_title, recommend_title, click_no, link_title]
                    print(link_inf)


                    if '/' in time_title :
                        today_day = time.strftime('%d', time.localtime(time.time()))
                        today_chk = int(today_day) - int(time_title.split("/")[2])
                        if today_chk > 1 :
                            return
#                        return
#
                    try :

#                        fout.write("%d\t %s\t %s\t %s\t %s\t %s\t %s\t %s\t %s\n"%(link_no, no_title, type_title, writer_title, name_title, time_title, recommend_title, click_no, link_title))
                        crawled_li.append("%d\t %s\t %s\t %s\t %s\t %s\t %s\t %s\t %s\n"%(link_no, no_title, type_title, writer_title, name_title, time_title, recommend_title, click_no, link_title))
                        print("lc-11")
                        link_no += 1

                    except:
                        print("can't update crawled list")
                        break

                    break

                except:
                    req = driver.page_source
                    soup = BeautifulSoup(req, 'html.parser')
                    print("except called")
                    select_i -= 2
                    continue

#                    chk_index += 1
#                    if chk_index >= chk_error:
#                        return


            chk_index = 1

#    fout.close()



#----------------정치 글 제외----------------

#----------------뽐뿌에서 동일 글 확인---------------- 할 필요 없음
#
#def is_empty_chk():
#    fp = open("humor_list.txt","r", encoding='UTF8')
#
#    cnt_no = 0
#    cnt_chk = 1
#
#    for line in fp :
#        time.sleep(1)
#        if cnt_chk <= cnt_no:
#            print("%d skipped" %(cnt_chk))
#            cnt_chk += 1
#            continue
#        try:
#            line = line.strip("\r\n")
#            psd = line.split("\t")
#            no = psd[0]
#            name = psd[1]
#            link = psd[2]
#
#            driver.get("http://www.ppomppu.co.kr/search_bbs.php?keyword="+name)
#            time.sleep(1)
#            #driver.find_element_by_name('keyword').send_keys(name)
#            #driver.find_element_by_xpath('/html/body/div[6]/div[2]/div[1]/div/form/button').click()
#            driver.implicitly_wait(5)
#
#            is_empty = driver.find_element_by_class_name("empty").text
#            print(is_empty)
#
#            driver.get(link)
#            time.sleep(1)
#            btn_name = driver.find_element_by_xpath('//*[@id="app"]/main/div/div/div/div[2]/div/button').text
#            while(btn_name != '다운로드') :
#                driver.find_element_by_xpath('//*[@id="app"]/main/div/div/div/div[2]/div/button').click()
#                time.sleep(1)
#                btn_name = driver.find_element_by_xpath('//*[@id="app"]/main/div/div/div/div[2]/div/button').text
#            print(no+" "+name+" completed")
#        except:
#            print(no+" "+name+" terminated")
#
#----------------원본 글 크롤링----------------


#def chk_uploaded():
#    fp = open("pp_list_%s.txt" %(today),"r", encoding='UTF8') #게시글 리스트 기록파일 오픈
#
#    for line in fp:
#        fp2 = open("uploaded_pp_list_%s.txt" %(today),"r", encoding='UTF8') #게시글 리스트 기록파일 오픈
#        for line2 in fp2:
#            #print("line2 = "+line2)
#            if line == line2 :
#                print("same")



def chk_alert(driver):
    try:
        driver.switch_to.alert().accept()
        print("accepted")
#        except:
 #           driver.switch_to.alert().dismiss()
  #          print("dismissed")
    except:
        print("no alert")


def pp_content_crawling():


#    fp = open("pp_list_%s.txt" %(today),"r", encoding='UTF8')
    global crawled_li
    global done_li
    global is_done_li
    global chk_done_li

    cnt_no = 0
    cnt_chk = 1
#    test_no = 2
#    test_i = 0


    pp_list_crawling()


    for line in crawled_li :
#        print(line)
        if cnt_chk <= cnt_no:
            print("%d skipped" %(cnt_chk))
            cnt_chk += 1
            continue
#        try:
        print("1")
        line = line.strip("\r\n")
        psd = line.split("\t")
        link_no = psd[0]
        no_title = psd[1]

        if no_title in done_li:
            print("This is in done_li. Skipped (pp_content_crawling)")
            is_done_li = 1
            continue
#            break

        type_title = psd[2]
        writer_title = psd[3]
        name_title = psd[4]
        time_title = psd[5]
        recommend_title = psd[6]
        click_no = psd[7]
        link_title = psd[8]

        print(line)

        chk_alert(driver)

        print("cc-1")
        try:
            driver.get(link_title)

        except:
            print("maybe, link is broken")
            done_li.append(no_title)
            done_listing(no_title)
            break

        print("cc-2")

        chk_alert(driver)

        req = driver.page_source

        print("cc-3")


        soup = BeautifulSoup(req, 'html.parser')
        print("cc-4")
        product_link = soup.select('body > div > div.contents > div.container > div > table:nth-child(9) > tbody > tr:nth-child(3) > td > table > tbody > tr > td:nth-child(5) > div > a')[0].text

        print("pd_link : " + product_link)

        contents = soup.find('td', {'class':'board-contents'})

        contents = affiliating_link(contents)

        content = str(contents.prettify())

#        print(type(content))

        print("cc-5")

        link_info = soup.select('body > div > div.contents > div.container > div > table:nth-child(9) > tbody > tr:nth-child(3) > td > table > tbody > tr > td:nth-child(5) > div > a')
        print("cc-6")
        real_link = link_info[0].text
#        print(real_link)
        print("cc-7")

        real_href = make_affiliate_link(real_link)
#        print(real_href)
        print("cc-8")

        content_li = [no_title, type_title, writer_title, name_title, time_title, recommend_title, link_title, click_no, content, real_link, real_href]

        #컨텐츠 가공
        print("cc-")


#        print("here?")
        content_li = content_modify(content_li)
        if content_li == 0:
            done_listing(no_title)
            break
        print("cc-10")
        #컨텐츠 포스팅
        nb_post(content_li)

        print("posting is done")
        chk_done_li = 1

        break


#        except:
#            print("skipped")
#            driver.get(link)
#            chk_alert()
#            chk_alert()

def content_modify(content_li):

    global hash_li
#     content_li = [no_title, type_title, writer_title, name_title, time_title, recommend_title, link_title, click_no, content, real_link, real_href]

    print("cm-1")
    no_des = content_li[0]
    print("cm-2")
    type_des = content_li[1].strip()
    print("cm-3")
    writer_des = content_li[2]
    print("cm-4")
#    print(content_li[3])
    if '[' in content_li[3]:
        name_des_li = title_modify(content_li[3]) #title
    else :
        return 0
    print("cm-5")
    time_des = content_li[4]
    print("cm-6")
    recommend_des = content_li[5].split(" ")[0]
    print("cm-7")
    link_des = content_li[6]
    print("cm-8")
    click_no = content_li[7]
    print("cm-9")
    descript = content_li[8]
    print("cm-10")
    real_link = content_li[9]
    print("cm-11")
    real_href = content_li[10]
    print("cm-12")
    #타이틀 편집
    title_inf = title_analysis(name_des_li)  #title_inf = [product_inf, price_product, price_delivery, mall]
    print(title_inf[0])
    print("cm-13")


    hash_source = cleanText(title_inf[0])
    hash_string = ""
#    print(thisdata)

    hash_li = hash_source.replace('  ',' ').replace('  ',' ').strip(' ').split(' ')

#    print (thisdata)
    """
    for no in range(0,10):
        for i in hash_li:
            if str(no) in i:
                hash_li.remove(i)
                break
    """

    for string in hash_li:
        hash_string += "#"+string+" "


#    print(name_des)
#    print(title_inf)

    #본문 편집
#    print("cm_1")
    product_info = "<p>가격 : %s </p><p>배송비 : %s </p><p>분류 : %s </p> <p>조회수 / 추천수 : %s / %s </p><p>링크 : <a href=%s\" target=\"_blank\" class=\"con_link\"> %s </a></p><br>" %(title_inf[1], title_inf[2], type_des, click_no, recommend_des, real_href, real_link)
    greeting = "<p></p><p>안녕하세요! 핫티입니다.</p> <p>나만 알기 아까운 뽐뿌 핫딜정보를 실시간으로 전해 드리는 '핫티의 쇼핑 셀렉트'</p>"
    introduce = "<p>%s에서 구매 가능한 '%s' 정보를 전해드립니다.</p><p></p><p>시간은 금이죠! 필요한 물품 얼른 구매하시고 가족들과 함께 시간 보내는건 어떨까요?</p><p></p><p>자, 그럼 정보 확인하시죠!</p><br>" %(title_inf[3], title_inf[0])
#    print("cm_2")
    last_link = "<br><p>구매링크 : <a href=%s\" target=\"_blank\" class=\"con_link\"> %s </a></p><br><br>" %(real_href, real_link)
#    print("cm_3")
    descript = product_info + greeting + introduce + descript + last_link + hash_string
#    print("cm_4")
    content_li = [no_des, type_des, writer_des, name_des_li[0], time_des, recommend_des, link_des, descript]
#    print("cm_5")

    return content_li

#@nb_post ---> content_li = [no_title, type_title, writer_title, name_title, time_title, recommend_title, link_title, content]





def title_modify(name_des):

    psd = name_des.split("]")
    mall_name = psd[0].strip(" ").strip("[")
    title_tail = psd[1].rstrip(")")
    title_mod = "[실시간 뽐뿌] " + title_tail + "/" + mall_name + ")"
    title_mod_li = [title_mod, mall_name]
    return title_mod_li

def title_analysis(title_li):

    psd = title_li[0].replace(']','(').split("(")
    print("ta-1")
    product_inf = ""

    for i in range(1,len(psd)-1):
        product_inf += psd[i]
    print("ta-2")

    product_inf = product_inf.strip(" ")
#    print("2a")
    price_inf = psd[len(psd)-1].split("/")
#    print("2b")
    price_product = price_inf[0].strip(" ")
#    print("2c")
    price_delivery = price_inf[1].strip(" ")
#    print("2d")
#    print(price_inf)
#    return
#    mall = price_inf[2].strip(")")  #여기가 문제
    mall = title_li[1]
#    ['  아미노에너지 585g 포도맛 [유통기한 6월 1일 까지', '개근질마트)']
    print("ta-3")
    title_inf = [product_inf, price_product, price_delivery, mall]
    print("ta-4")
    return title_inf




def affiliating_link(tag_file):

    for link in tag_file.find_all('a'):
        target_url = link.string
        affiliated_url = make_affiliate_link(target_url)

        link['href'] = affiliated_url

    return tag_file




def make_affiliate_link(target_url):

    host = 'https://api.linkprice.com'
    path = '/ci/service/custom_link_xml'
    params = {
            'a_id' : 'A100665008', #어필레이션 id
            'url' : target_url, #변환할 링크
            #'url' : 'http://www.gmarket.co.kr/',
            'mode' : 'json' #응답 모드
            }

    url = host + path

    response = requests.get(url, params=params)

    print ("req url : "+response.url)

    data = response.json()

    try :
        if data["result"] == 'S':
            print("ans url : "+data["url"])
            return data["url"]

        elif data["result"] == 'F':
            print("no ans")
            faff_link = open("no_affiliated_list.txt","a", encoding='UTF8')
            faff_link.write("%s\n"%(target_url))
            faff_link.close()
            return target_url
    except:
        return target_url




#이건 한참 작업 해야 할듯
def pp_reply_crawling(no_title):

    link_header = "http://www.ppomppu.co.kr/zboard/popup_comment.php?id=ppomppu&no="
    reply_link = link_header + no_title
    driver.get(reply_link)


    #글쓴이
    #comment_10174875 > div.comment_line > table > tbody > tr > td:nth-child(5) > b > a
    # //*[@id="comment_10174875"]/div[1]/table/tbody/tr/td[5]/b/a

    #답글내용
    #commentContent_10174875
    # //*[@id="commentContent_10174875"]

    #대댓글 글쓴이
    #comment_10174912 > div.comment_line > table > tbody > tr > td:nth-child(5) > b > a

    #대댓글 내용
    #commentContent_10174912

#
#def is_today_list():
#    try:
#        fp = open("pp_list_%s.txt" %(today),"r", encoding='UTF8')
#        print("exist")
#        return 1
#    except:
#        print("no file")
#        return 0
#
def timer():
    waiting_time = 30
    for i in range(0, waiting_time) :
        print("remain sec : %d" %(30-i))
        time.sleep(1)
    print("re-posting")


#print(time.strftime('%Y-%m-%d, %H:%M:%S', time.localtime(time.time())))
#print(time.strftime('%c', time.localtime(time.time())))

today = time.strftime('%Y-%m-%d', time.localtime(time.time()))
#chk_file_exist = is_today_list()
#print(chk_file_exist)

login_naver()

chk_done_li = 0
is_done_li = 0

hash_li = []
done_li = []
pre_content_no = 0
content_li = [0]
crawled_li =[]

done_list_sync()
#pp_list_crawling()

while(1):
#    try:
    pp_content_crawling()

#    timer()

    pre_content_no = content_li[0]

#    except:
#        print("reload program")
#        done_li.append(content_li[0])
#        done_listing(content_li[0])
##        timer()

#pp_reply_crawling()
#login_pp()
