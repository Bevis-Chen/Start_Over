import re
import requests
import pandas as pd
from datetime import datetime, timedelta
from bs4 import BeautifulSoup

def pttNews(key = None):
    header = {"user-agent" : 
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}
    data = { "from" : "/bbs/Beauty/index.html",
            "yes" : "yes" }
    
    current_datetime = datetime.now()
    delta = timedelta(days = -1)
    need_date = current_datetime + delta
    Date = str(need_date.month) + "/" + str(need_date.day)

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
            # if time.text.split()[0] == Date:
            #     return             
            if key != None:
                if "Re:" not in title.text and (key in title.text):
                    title_name = title.text
                    title_url = "https://www.ptt.cc" + title.get("href")
                    title_date = time.text.split()[0]
                    r1 = session.post(title_url, data = data, headers = header)
                    soup = BeautifulSoup(r1.text, "html.parser")
                    imgs = soup.select("img")
                    for img in imgs:
                        img_src = img.get("src")
                        program = r".com/(\w*.\w*)?"
                        program1 = r".tw/(\w*.\w*)"
                        try:
                            file_name = re.findall(program, img_src)[0]
                        except Exception as e:
                            file_name = re.findall(program1, img_src)[0]                        
                        # print(img_src)
                        # print(file_name)
                        # print("*" * 60)
                        r2 = session.get(img_src, headers = header)
                        beautys_folder_name = r"爬蟲/PTT/beauty_imgs/"
                        with open(beautys_folder_name + file_name, "wb") as pic:
                            for i in r2:
                                pic.write(i)    
                        # return                
                    # text1 = soup.find("div", id = "main-content").text
                    # text2 = text1.split("※ 發信站: 批踢踢實業坊(ptt.cc),")[0].split("\n")[1:]
                    # content = "\n".join(text2)                    
                    # print(title_date, title_name)                    
                    # print(content)
                    # print("-" * 60)
                    # temp_list.append([title_date, title_name, content])
                    # list1.extend(temp_list)
                    return                    
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
                    temp_list.append([title_date, title_name, content])
                    list1.extend(temp_list)                                     
                    # print(title_date, title_name)                    
                    # print(content)
                    # print("-" * 60)
            # return list1
pttNews("忍野")
# list_data = pttNews("正妹")
# df = pd.DataFrame(list_data, columns = ["Date", "Name", "Content"])
# print(df)
# print(list_data)
# df.to_csv(r"爬蟲\PTT\PTT.csv", encoding = "utf-8-sig")