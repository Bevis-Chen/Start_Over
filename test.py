import requests
from bs4 import BeautifulSoup
url = "https://www.ithome.com.tw/"

r = requests.get(url)

try:
    if r.status_code == 200:
        soup = BeautifulSoup(r.text, "lxml")
        news = soup.find_all("div", class_ = "item span4")
        print(len(news))
        for new in news:
            print(new.find("p", class_ = "title").find("a").text)
            print(url + new.find("p", class_ = "title").find("a").get("href"))
            print(new.find("p", class_= "post-at").text)
except Exception as e:
    print(e)
    print("那ㄟ安內~?")
# else:
#     print("Successful!!")