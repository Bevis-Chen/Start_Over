import requests
from bs4 import BeautifulSoup

r = requests.get("https://yahoo.com.tw/")

try:
    if r.status_code == 200:
        soup = BeautifulSoup(r.text, "lxml")
        print(soup)

except Exception as e:
    print(e)
    print("那ㄟ安內~?")
else:
    print("Successful!!")