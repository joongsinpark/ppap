import pg_support
import doneListControl
import time
from bs4 import BeautifulSoup
import affiliate


class ppomppu:

    def __init__(self, driver):
        self.boardlist_link = "http://www.ppomppu.co.kr/zboard/zboard.php?id=ppomppu&page=%d&divpage=60"
        self.link_header = "http://www.ppomppu.co.kr/zboard/view.php?id=ppomppu&page=2&divpage=60&no="
        self.link_content = ""
        self.id = ""
        self.type = ""
        self.author = ""
        self.title = ""
        self.time = ""
        self.numRecommend = ""
        self.numClick = ""

        self.mainText = ""

        self.done = 0
        self.hashTag=[]
        self.driver = driver


    def list_crawling(self):             #다하지 않고 맨 위에꺼만, done_li 비교 후 포스팅
        driver = self.driver
        pg_support.funcname()
        start_index = 1
        driver.get(self.boardlist_link % start_index)
        driver.implicitly_wait(5)
        time.sleep(2)
        req = driver.page_source
        soup = BeautifulSoup(req, 'html.parser')

        global done_li
        # 1page는 6, 2page는 4인거 처리해야함
        num_title=20

        #p의 최대범위 정해주기
        max_page_search = 5

        for p in range(1,max_page_search+1) :
            boardlist_link = self.boardlist_link % p
            driver.get(boardlist_link)
            req = driver.page_source
            soup = BeautifulSoup(req, 'html.parser')



            for i in range(1,num_title+1) : # # of product

                # while(1) :
                try:
                    if p == 2 :
                        select_i = 2*i + 2
                    else:
                        select_i = 2*i + 4

                    selector_header = '#revolution_main_table > tbody > tr:nth-child(%d) > ' % select_i
                    self.id = soup.select(selector_header +'td:nth-child(1)')[0].text.strip("\n").strip("\t")
                    if doneListControl.is_done_li(self.id):
                        continue

                    self.time = soup.select(selector_header +'td:nth-child(5) > nobr')[0].text
                    if '/' in self.time and doneListControl.yesterday_chk(self.time):
                        return 0

                    print (getId())
                    print(self.id)

                    print("lc-3")
                    self.link_content = self.link_header + self.id
                    # print(self.link_content)
                    print("lc-4")
                    self.type = soup.select(selector_header +'td.han4.list_vspace > nobr')[0].text
                    print("lc-5")

                    try:        #글쓴이 id가 text이거나 이모티콘인 경우 처리
                        self.author = soup.select(selector_header +'td:nth-child(3) > div > nobr > a > span')[0].text
                    except:
                        self.author = soup.select(selector_header +'td:nth-child(3) > div > nobr > a > img')[0].attrs['alt']

                    print("lc-6")
                    self.title = soup.select(selector_header +'td:nth-child(4) > table > tbody > tr > td:nth-child(2) > a > font')[0].text
                    print("lc-7")
                    self.numRecommend = soup.select(selector_header +'td:nth-child(6)')[0].text
                    print("lc-8")
                    self.numClick = soup.select(selector_header +'td:nth-child(7)')[0].text
                    print("lc-9")

                    return 1

                except:
                    print("except called")
                    return 0


    def content_crawling(self):       #pb.content_modify()
    #return 값 정해두
            driver = self.driver
            pg_support.funcname()
            pg_support.chk_alert(driver)

            print("cc-1")
            print(self.link_content)

            try:        #동작하나?
                driver.get(self.link_content)

            except:
                print("Maybe, Link is broken")
                doneListControl.done_listing(self.id)
                return 0

            print("cc-2")

            pg_support.chk_alert(driver)

            req = driver.page_source

            print("cc-3")

            soup = BeautifulSoup(req, 'html.parser')
            print("cc-4")
            self.shopLink = soup.select('body > div > div.contents > div.container > div > table:nth-child(9) > tbody > tr:nth-child(3) > td > table > tbody > tr > td:nth-child(5) > div > a')[0].text

            print("pd_link : " + self.shopLink)

            self.mainText = soup.find('td', {'class':'board-contents'})

            self.mainText, self.shopLink, self.affLink = affiliate.affiliating_link(self.mainText)

            self.mainText = str(self.mainText.prettify())

            print("cc-5")

        #        print("here?")








    def getId(self): return self.id
    def setId(self, id): self.id = id
    def getType(self): return self.type
    def setType(self, type): self.type = type
    def getAuthor(self): return self.author
    def setAuthor(self, author): self.author = author
    def getTitle(self): return self.title
    def setTitle(self, title): self.title = title
    def getTime(self): return self.time
    def setTime(self, time): self.time = time
    def getNumrecommend(self): return self.numRecommend
    def setNumrecommend(self, numRecommend): self.numRecommend = numRecommend
    def getNumclick(self): return self.numClick
    def setNumclick(self, numClick): self.numClick = numClick
    def getMaintext(self): return self.mainText
    def setMaintext(self, mainText): self.mainText = mainText
    def getDone(self): return self.done
    def setDone(self, done): self.done = done
    def getHashtag(self): return self.hashTag
    def pushHashtag(self, tag): self.hashTag.append("#"+tag)





class ppboard(ppomppu):

    def __init__(self, driver):

        self.driver = driver
        self.boardlist_link = "http://www.ppomppu.co.kr/zboard/zboard.php?id=ppomppu&page=%d&divpage=60"
        # self.link_header = ""
        self.shopLink = ""
        self.affLink = ""

        self.product_inf = ""
        self.price = ""
        self.deliveryPrice = ""
        self.mall = ""

    def title_modify(self):
        # [티몬] 백진미채/홍진미채 1kg (14,900/무료)
        pg_support.funcname()

        psd = self.title.replace(']','(').split("(")
        print("ta-1")
        self.mall = psd[0].strip("[")

        print("ta-2")
        for i in range(1,len(psd)-1):
            self.product_inf += psd[i]
        print("ta-3")

        self.product_inf = self.product_inf.strip(" ")
        print("2a")
        price_inf = psd[len(psd)-1].split("/")
        print("2b")
        self.price = price_inf[0].strip(" ")
        print("2c")
        self.deliveryPrice = price_inf[1].strip(" ")
    #    ['  아미노에너지 585g 포도맛 [유통기한 6월 1일 까지', '개근질마트)']
        self.title = "[실시간 뽐뿌] %s (%s / %s / %s)" %(self.product_inf, self.price, self.deliveryPrice, self.mall)
        print (self.title)

    def content_modify(self):
        pg_support.funcname()

        if '[' in content_li[3]:
            name_des_li = title_modify(content_li[3]) #title
        else :
            return 0
        print("cm-5")

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


    def nb_post(self) : return


    def getShoplink(self): return self.shopLink
    def setShoplink(self, shopLink): self.shopLink = shopLink
    def getAfflink(self): return self.affLink
    def setAfflink(self, affLink): self.affLink = affLink
    def getProduct_inf(self): return self.product_inf
    def setProduct_inf(self, product_inf): self.product_inf = product_inf
    def getPrice(self): return self.price
    def setPrice(self, price): self.price = price
    def getDeliveryprice(self): return self.deliveryPrice
    def setDeliveryprice(self, deliveryPrice): self.deliveryPrice = deliveryPrice
    def getMall(self): return self.mall
    def setMall(self, mall): self.mall = mall
