import requests, time, re
from bs4 import BeautifulSoup
import pandas as pd

url = r"https://www.ptt.cc/ask/over18"

header = {"user-agent" : 
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}
data = { "from" : "/bbs/Gossiping/index.html",
          "yes" : "yes" }

session = requests.Session()
try:
    resp = session.post(url, headers = header, data = data)
    if resp.status_code == 200:
        # print(resp.text)
        soup = BeautifulSoup(resp.text, "html.parser")
        btn = soup.select("div.btn-group>a.btn")
        for i, b in enumerate(btn) : 
            page_max = 0
            if i == 3:
                url_get = b.get("href")
                re_page = r"\d"
                page_max_str = re.findall(re_page, url_get)
                page_max = eval("".join(page_max_str))
                break
    datas_list = []        
    for p in range(1, page_max):
        pages = "/bbs/Gossiping/index{}.html".format(p)
        data1 = {
            "from" : pages,
            "yes" : "yes"}
        session = requests.Session()
        resp = session.post(url, headers = header, data = data1)
        # time.sleep(2)
        if resp.status_code == 200:
                soup = BeautifulSoup(resp.text, "html.parser")
                datas = soup.select("div.r-ent")                
                for a in datas:
                    if a.select_one("div.title").text != None:
                        if "Re: " not in a.select_one("div.title a").text:
                            date = a.select_one("div.date").text
                            title = a.select_one("div.title a").text
                            ptt_url = "https://www.ptt.cc" + a.select_one("a").get("href")
                            datas_list.append([date, title, ptt_url])
                            # print(date, end = ", ")
                            # print(title)
                            # print(ptt_url)
                            # print()                        
    df = pd.DataFrame(datas_list, columns = ["Date", "Title", "URL"])
    df.to_csv(r"爬蟲\PTT_Gossiping_Info.csv", encoding = "utf-8-sig")
except Exception as e:
    print(e, "哪尼~~~?")
    print(data)

'''
datas = soup.select("div.yuRUbf")
for i in datas:
    print(i.select_one("h3").text)
    print(i.select_one("a").get("href"))
    print("*" * 60)
'''