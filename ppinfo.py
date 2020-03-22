import pg_support
import doneListControl
import time
from bs4 import BeautifulSoup
import affiliate
import re

class ppomppu:
    boardlist_link = ""
    link_header = "http://www.ppomppu.co.kr/zboard/view.php?id=ppomppu&page=2&divpage=60&no="
    link_content = ""
    id = ""
    type = ""
    author = ""
    title = ""
    time = ""
    numRecommend = ""
    numClick = ""

    mainText = ""

    done = 0
    hashTag=[]

    driver=""

    def __init__(self, driver):

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

                    print("lc-3")
                    self.link_content = self.link_header + self.id
                    print(self.link_content)
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
                    self.numRecommend = soup.select(selector_header +'td:nth-child(6)')[0].text.split(" - ")[0]
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
            self.affLink = affiliate.make_affiliate_link(self.shopLink)
            print("pd_link : " + self.shopLink)
            print(self.shopLink)
            print(self.affLink)

            self.mainText = soup.find('td', {'class':'board-contents'})

            self.mainText = affiliate.affiliating_link(self.mainText)

            self.mainText = str(self.mainText.prettify())

            print("cc-5")

        #        print("here?")
    def nb_post(self) :
        pg_support.funcname()
        driver = self.driver
        #print(content_li)
        #content_li = [no_title, type_title, writer_title, name_title, time_title, recommend_title, link_title, content]

    #    [실시간 뽐뿌] 심플 논슬립 옷걸이 30P (6,900원/무료배송) - 페이코 쿠폰 소진용/인터파크)

        #---------------- 글쓰기 창 진입 / 작성 ----------------
        type_li = ["","","","","","","","","","컴퓨터", "디지털", "식품/건강", "서적", "가전/가구", "육아", "상품권", "의류/잡화", "화장품", "등산/캠핑", "기타"]
        type_footer = str(type_li.index(self.type))
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

        driver.find_element_by_name('post.title').send_keys(self.title)
        print("4")

        #---------------- iframe이 사용된 에디터 처리 ----------------

        # 현재 웹페이지에서 iframe이 몇개가 있는지 변수에 넣고 확인해 봅니다.

        #driver.find_element_by_xpath('//*[@id="se2_iframe"]').click()

        driver.find_element_by_xpath('//*[@id="smart_editor2_content"]/div[5]/ul/li[2]/button').click()
        driver.find_element_by_xpath('//*[@id="smart_editor2_content"]/div[4]/textarea[1]').send_keys(self.mainText)
        time.sleep(10)
        driver.find_element_by_xpath('//*[@id="btn_submit"]/img').click()
        time.sleep(1)
        try:
            chk_alert(driver)
        except:
            print("no alert")

        doneListControl.done_listing(self.id)



class ppboard(ppomppu):

    boardlist_link = "http://www.ppomppu.co.kr/zboard/zboard.php?id=ppomppu&page=%d&divpage=60"
    # self.link_header = ""
    shopLink = ""
    affLink = ""

    product_inf = ""
    price = ""
    deliveryPrice = ""
    mall = ""

    driver=""

    def __init__(self, driver):

        self.driver = driver

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
        self.deliveryPrice = price_inf[1].strip(" ").strip(")")
    #    ['  아미노에너지 585g 포도맛 [유통기한 6월 1일 까지', '개근질마트)']
        self.title = "[실시간 뽐뿌] %s (%s / %s / %s)" %(self.product_inf, self.price, self.deliveryPrice, self.mall)
        print (self.title)

    def content_modify(self):
        pg_support.funcname()
        hash_string = self.hash_modify()
        #본문 편집
        print("cm_1")
        product_info = "<p>가격 : %s </p><p>배송비 : %s </p><p>분류 : %s </p> <p>조회수 : %s </p><p>링크 : <a href=%s\" target=\"_blank\" class=\"con_link\"> %s </a></p><br>" %(self.price, self.deliveryPrice, self.type, self.numClick, self.affLink, self.shopLink)
        #나중에 추천수 작업 필se
        greeting = "<p></p><p>안녕하세요! 핫티입니다.</p> <p>나만 알기 아까운 뽐뿌 핫딜정보를 실시간으로 전해 드리는 '핫티의 쇼핑 셀렉트'</p>"
        introduce = "<p>%s에서 구매 가능한 '%s' 정보를 전해드립니다.</p><p></p><p>시간은 금이죠! 필요한 물품 얼른 구매하시고 가족들과 함께 시간 보내는건 어떨까요?</p><p></p><p>자, 그럼 정보 확인하시죠!</p><br>" %(self.mall, self.product_inf)
        print("cm_2")
        last_link = "<br><p><a href=%s\" target=\"_blank\" class=\"con_link\"><span style=\"font-size: 18pt;\"> 지금 구매하러 가기(링크) </a></p><br><br>" %(self.affLink)
        print("cm_3")
        self.mainText = product_info + greeting + introduce + self.mainText + last_link + hash_string
        print("cm_4")

        print(self.mainText)


    #@nb_post ---> content_li = [no_title, type_title, writer_title, name_title, time_title, recommend_title, link_title, content]


    def hash_modify(self):

        pg_support.funcname()
        hash_source = pg_support.cleanText(self.product_inf)

        self.hashTag = hash_source.replace('  ', ' ').replace('  ', ' ').strip(' ').split(' ')
        h_string = ""

        d = re.compile('\d+')
        e = re.compile('[a-zA-Z]+')

        for string in self.hashTag:
            if not d.match(string) and not e.match(string): h_string += "#"+string+" "

        h_string += "#%s #뽐뿌" % self.mall

        return h_string



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
