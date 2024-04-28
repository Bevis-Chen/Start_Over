import requests
from datetime import datetime
from bs4 import BeautifulSoup

header = {"user-agent" : 
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}
data = { "from" : "/bbs/Gossiping/index.html",
        "yes" : "yes" }

url = r"https://www.ptt.cc/ask/over18"

session = requests.Session()
session.post(url, headers = header, data = data)
url2 = "https://www.ptt.cc/bbs/Gossiping/index.html"
try_url = "https://www.ptt.cc/bbs/Gossiping/M.1714235956.A.1E2.html"
r = session.post(try_url, data = data, headers = header)

soup = BeautifulSoup(r.text, "html.parser")
text1 = soup.find("div", id = "main-content").text
text2 = text1.split("--")[0].split("\n")[1:]
content = "\n".join(text2)
print(content)
