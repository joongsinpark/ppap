import pg_support
import time

# class doneList:

# def __init__(self):
done_li = []
today = today = time.strftime('%Y-%m-%d', time.localtime(time.time()))
yesterday = time.strftime('%Y-%m-%d', time.localtime(time.time()-86400))

def sync_done_li():

    pg_support.funcname()

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


def is_done_li(id):
    pg_support.funcname()
    if id in done_li:
        print("This is in done_li. Skipped ")
        return 1
    else:
        print("not posted yet. continued")
        return 0

def yesterday_chk(t):
    pg_support.funcname()
    today_day = time.strftime('%d', time.localtime(time.time()))
    today_chk = int(today_day) - int(t.split("/")[2])
    if today_chk > 1 :
        print("too old information. waiting new data")
        #자료가 없을 경우 어떻게 기다릴지 ?
        return 1

def done_listing(id):
    pg_support.funcname()
    global done_li
    done_li.insert(0, id)
    fout = open("done_list_%s.txt" %(today),"a", encoding='UTF8') #게시글 리스트 기록파일 오픈
    fout.write("%s\n"%(id))
    fout.close()
