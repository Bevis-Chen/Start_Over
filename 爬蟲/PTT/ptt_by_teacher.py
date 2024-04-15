import requests
from bs4 import BeautifulSoup
# import pandas as pd

url = r"https://www.ptt.cc/ask/over18"

header = {"user-agent" : 
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}
data = { "from" : "/bbs/Gossiping/index.html",
          "yes" : "yes" }

session = requests.Session()
session.post(url, headers = header, data = data)
url2 = "https://www.ptt.cc/bbs/Gossiping/index.html"

while True:
    r = session.post(url, data = data, headers = header)
    temp = r.text.split('<div class="r-list-sep"></div>')[0]
    soup = BeautifulSoup(temp, "html.parser")
    title = soup.select("div.r-ent div.title a")
    date = soup.select("div.r-ent div.title div.meta div.date")
    ptt_url = "https://www.ptt.cc" + soup.select("div.btn-group.btn-group-paging a")[1].get("href")

    for i, n in enumerate(title):
        if "Re:" not in n:
            print(n.text)
