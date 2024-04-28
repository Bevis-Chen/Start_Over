import requests
from datetime import datetime
from bs4 import BeautifulSoup

try_url = "https://www.ptt.cc/bbs/Gossiping/M.1714235956.A.1E2.html"

header = {"user-agent" : 
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}
data = { "from" : "/bbs/Gossiping/M.1714235956.A.1E2.html",
        "yes" : "yes" }

session = requests.Session()
r = session.get(try_url, headers = header)
# url2 = "https://www.ptt.cc/bbs/Gossiping/index.html"

soup = BeautifulSoup(r.text, "html.parser")
# for text in soup.select_one("div.article-meta-tag"):
print(soup.find("div", class_ = "article-meta-tag"))
