import requests, time
from bs4 import BeautifulSoup

url = r"https://www.ptt.cc/ask/over18"

header = {"user-agent" : 
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}
data = { "from" : "/bbs/Gossiping/index.html",
          "yes" : "yes" }

session = requests.Session()
resp = session.post(url, headers = header, data = data)
if resp.status_code == 200:
    # print(resp.text)
    soup = BeautifulSoup(resp.text, "html.parser")
    btn = soup.select("div.btn-group>a.btn")
    for b in btn : 
        print(b)

# try:
    # for p in range(39319, 39322):
    # pages = "/bbs/Gossiping/index{}.html".format(p)
    # data = {
    #     "from" : pages,
    #     "yes" : "yes"}
    # session = requests.Session()
    # resp = session.post(url, headers = header, data = data)
    # time.sleep(2)
    # if resp.status_code == 200:
            # print(resp.text)
            # soup = BeautifulSoup(resp.text, "html.parser")
            # datas = soup.select("div.r-ent")
            # print(datas)
            # for data in datas:
            #     if data.select_one("title").text != None:
            #         if "Re: " not in data.select_one("title a").text:
            #             print(data.select_one("title a").text)
            #             print("https://www.ptt.cc" + data.select_one("a").get("href"))                        
            # datas = soup.select("div.yuRUbf")
            # for i in datas:
            #     print(i.select_one("h3").text)
            #     print(i.select_one("a").get("href"))
            #     print("*" * 60)
# except Exception as e:
#     print(e, "哪尼~~~?")
    # print(data)