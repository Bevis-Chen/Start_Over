import requests
import pandas as pd
from datetime import datetime
from bs4 import BeautifulSoup

def pttNews(key = None):
    header = {"user-agent" : 
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}
    data = { "from" : "/bbs/Gossiping/index.html",
            "yes" : "yes" }
    current_datetime = datetime.now()
    Date = str(current_datetime.month) + "/" + str(current_datetime.day - 2)
    url = r"https://www.ptt.cc/ask/over18"    
    session = requests.Session()
    session.post(url, headers = header, data = data)
    url2 = "https://www.ptt.cc/bbs/Beauty/index.html"
    list1 = []
    while True:
        r = session.post(url2, data = data, headers = header)
        temp = r.text.split('<div class="r-list-sep"></div>')[0]
        soup = BeautifulSoup(temp, "html.parser")
        titles = soup.select("div.r-ent div.title a")
        dates = soup.select("div.r-ent div.meta div.date")
        url2 = "https://www.ptt.cc" + soup.select("div.btn-group.btn-group-paging a")[1].get("href")

        for title, time in zip(titles, dates):
            temp_list = []
            if time.text.split()[0] == Date:
                return             
            if key != None:
                if "Re:" not in title.text and (key in title.text):
                    title_name = title.text
                    title_url = "https://www.ptt.cc" + title.get("href")
                    title_date = time.text.split()[0]
                    r1 = session.post(title_url, data = data, headers = header)
                    soup = BeautifulSoup(r1.text, "html.parser")
                    text1 = soup.find("div", id = "main-content").text
                    text2 = text1.split("※ 發信站: 批踢踢實業坊(ptt.cc),")[0].split("\n")[1:]
                    content = "\n".join(text2)                    
                    # print(title_date, title_name)                    
                    # print(content)
                    # print("-" * 60)
                    temp_list.append([title_date, title_name, content])
                    list1.extend(temp_list)
                    # return 
            else:
                if "Re:" not in title.text :
                    title_name = title.text
                    title_url = "https://www.ptt.cc" + title.get("href")
                    title_date = time.text.split()[0]
                    r1 = session.post(title_url, data = data, headers = header)
                    soup = BeautifulSoup(r1.text, "html.parser")
                    text1 = soup.find("div", id = "main-content").text
                    text2 = text1.split("※ 發信站: 批踢踢實業坊(ptt.cc),")[0].split("\n")[1:]
                    content = "\n".join(text2)                    
                    print(title_date, title_name)                    
                    print(content)
                    print("-" * 60)
                    # return 
        return list1

list_data = pttNews("正妹")
df = pd.DataFrame(list_data, columns = ["Date", "Name", "Content"])
print(df)
# print(list_data)
# df.to_csv(r"爬蟲\PTT\PTT.csv", encoding = "utf-8-sig")