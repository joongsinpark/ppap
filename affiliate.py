import requests

target_url = ""
affiliated_url = ""

def affiliating_link(tag_file):
    global target_url
    global affiliated_url
    # 본문에 있는 링크를 어필리에이트 링크로 바꿔주는 코

    for link in tag_file.find_all('a'):
        target_url = link.string
        affiliated_url = make_affiliate_link(target_url)

        link['href'] = affiliated_url


    return tag_file




def make_affiliate_link(t_url):

    host = 'https://api.linkprice.com'
    path = '/ci/service/custom_link_xml'
    params = {
            'a_id' : 'A100665008', #어필레이션 id
            'url' : t_url, #변환할 링크
            #'url' : 'http://www.gmarket.co.kr/',
            'mode' : 'json' #응답 모드
            }

    url = host + path

    response = requests.get(url, params=params)

    # print ("req url : "+response.url)

    data = response.json()

    try :
        if data["result"] == 'S':
            print("ans url : "+data["url"])
            return data["url"]

        elif data["result"] == 'F':
            print("no ans")
            faff_link = open("no_affiliated_list.txt","a", encoding='UTF8')
            faff_link.write("%s\n"%(t_url))
            faff_link.close()
            return t_url
    except:
        return t_url
