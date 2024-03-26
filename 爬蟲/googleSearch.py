import pandas as pd
import requests
from bs4 import BeautifulSoup

url = r"https://www.google.com/search?q=android"

header = {"user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}

resp = requests.get(url, headers = header)

if resp.status_code == 200:
    # print(resp.text)
    soup = BeautifulSoup(resp.text, "html.parser")
    datas = soup.select("div.yuRUbf")
    for i in datas:
        print(i.select_one("h3").text)
        print(i.select_one("a").get("href"))
        print("*" * 60)
