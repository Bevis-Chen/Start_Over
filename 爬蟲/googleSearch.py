import pandas as pd
import requests
from bs4 import BeautifulSoup

# url = r"https://www.google.com/search?q=android&sca_esv=100a8d72724cfbcd&ei=mvT-Zf6jC77d1e8P68Gq2A4&ved=0ahUKEwj-2Nb-2IqFAxW-bvUHHeugCusQ4dUDCBA&oq=andorid&gs_lp=Egxnd3Mtd2l6LXNlcnAiB2FuZG9yaWQyBBAAGEcyBBAAGEcyBBAAGEcyBBAAGEcyBBAAGEcyBBAAGEcyBBAAGEcyBBAAGEcyBBAAGEcyBBAAGEdIwglQAFgAcAB4ApABAJgBAKABAKoBALgBDMgBAJgCAaACBZgDAOIDBRIBMSBAiAYBkAYKkgcBMaAHAA&sclient=gws-wiz-serp"
url = r"https://www.google.com/search"
header = {"user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}

resp = requests.get(url, headers = header, params = {"q" : "android"})

if resp.status_code == 200:
    # print(resp.text)
    soup = BeautifulSoup(resp.text, "html.parser")
    datas = soup.select("div.yuRUbf")
    for i in datas:
        print(i.find("h3").text)
        print(i.find("a").get("href"))
        print("*" * 60)
