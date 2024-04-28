import requests
from datetime import datetime
from bs4 import BeautifulSoup

def pttNews(key = None):
    header = {"user-agent" : 
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}
    data = { "from" : "/bbs/Gossiping/index.html",
            "yes" : "yes" }

    current_datetime = datetime.now()
    Date = str(current_datetime.month) + "/" + str(current_datetime.day - 1)
    url = r"https://www.ptt.cc/ask/over18"    
    session = requests.Session()
    session.post(url, headers = header, data = data)
    url2 = "https://www.ptt.cc/bbs/Gossiping/index.html"
    while True:
        r = session.post(url2, data = data, headers = header)
        temp = r.text.split('<div class="r-list-sep"></div>')[0]
        soup = BeautifulSoup(temp, "html.parser")
        titles = soup.select("div.r-ent div.title a")
        dates = soup.select("div.r-ent div.meta div.date")
        url2 = "https://www.ptt.cc" + soup.select("div.btn-group.btn-group-paging a")[1].get("href")

        for title, time in zip(titles, dates):
            if time.text.split()[0] == Date:
                return             
            if key != None:
                if "Re:" not in title.text and (key in title.text):
                    title_name = title.text
                    title_url = "https://www.ptt.cc" + title.get("href")
                    title_date = time.text.split()[0]
                    print(title_name)
                    print(title_url)
                    print(title_date)
            else:
                if "Re:" not in title.text :
                    title_name = title.text
                    title_url = "https://www.ptt.cc" + title.get("href")
                    title_date = time.text.split()[0]
                    r1 = session.post(title_url, data = data, headers = header)
                    soup = BeautifulSoup(r1.text, "html.parser")
                    text1 = soup.find("div", id = "main-content").text
                    text2 = text1.split("--")[0].split("\n")[1:]
                    content = "\n".join(text2)
                    
                    print(title_date, title_name)                    
                    print(content)
                    print("-" * 60)
                    return 
              
pttNews()