import requests
from bs4 import BeautifulSoup

url = r"https://www.ptt.cc/ask/over18"
header = {"user-agent" : 
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}
data = { "from" : "/bbs/Gossiping/index1.html",
          "yes" : "yes" }


session = requests.Session()
resp =session.post(url, headers = header, data = data)
if resp.status_code == 200:
    # print(resp.text)
    soup = BeautifulSoup(resp.text, "html.parser")
    datas = soup.select("div.r-ent")    
    # print(datas)
    for a in datas:
        if a.select_one("div.title").text != None:
            if "Re: " not in a.select_one("div.title a").text:
                print(a.select_one("div.title a").text)