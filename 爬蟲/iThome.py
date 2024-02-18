import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://www.ithome.com.tw/"
# AI
url1 = "https://www.ithome.com.tw/big-data"
# 雲端-新聞
url2 = "https://www.ithome.com.tw/cloud"
# 醫療IT >>他是這樣命名
url3 = "https://www.ithome.com.tw/healthit"

need_list = ["big-data", "cloud", "healthit"]
total = []
try:
    for need in need_list:
        r = requests.get(url + need)        
        if r.status_code == 200:
            soup = BeautifulSoup(r.text, "lxml")
            news = soup.find_all("div", class_ = "span4 channel-item")
            # print(news)
            # print(len(news))
            data = []
            for new in news:
                title = new.find("p", class_ = "title").find("a").text
                new_url = url[:-1] + new.find("p", class_ = "title").find("a").get("href")
                date = new.find("p", class_= "post-at").text
                data.append([title, new_url, date, need])
        total.extend(data)    
        # print(total)       
    df = pd.DataFrame(total, columns = ["Title", "URL", "Date", "Class"])
    print(df)
    # print(df.to_csv(r"./爬蟲/iThome_news.csv", encoding = "utf-8-sig"))
except Exception as e:
    print(e)
    print("那ㄟ安內~?")


# else:
#     print("Successful!!")