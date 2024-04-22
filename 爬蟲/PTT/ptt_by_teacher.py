import requests
from datetime import datetime
from bs4 import BeautifulSoup

def pttNews():
    current_datetime = datetime.now()
    Date = str(current_datetime.month) + "/" + str(current_datetime.day)

    url = r"https://www.ptt.cc/ask/over18"
    header = {"user-agent" : 
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}
    data = { "from" : "/bbs/Gossiping/index.html",
            "yes" : "yes" }
    
    session = requests.Session()
    session.post(url, headers = header, data = data)
    url2 = "https://www.ptt.cc/bbs/Gossiping/index.html"

    while True:
        r = session.post(url2, data = data, headers = header)
        temp = r.text.split('<div class="r-list-sep"></div>')[0]
        soup = BeautifulSoup(temp, "html.parser")
        titles = soup.select("div.r-ent div.title a")
        dates = soup.select("div.r-ent div.meta div.date")
        # if dates[0].text != Date:
        #     return         
        url2 = "https://www.ptt.cc" + soup.select("div.btn-group.btn-group-paging a")[1].get("href")

        for title, time in zip(titles, dates):
            if "Re:" not in title.text:
                print(title.text)
                print("https://www.ptt.cc" + title.get("href"))
                print(time.text)
                
pttNews()