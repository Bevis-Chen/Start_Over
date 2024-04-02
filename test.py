import requests
from bs4 import BeautifulSoup

url = "https://www.ptt.cc/bbs/Gossiping/index1.html"
header = {"user-agent" : 
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}

resp = requests.get(url)