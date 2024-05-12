import requests, re
from bs4 import BeautifulSoup

url = "https://www.codejudger.com/target/5201.html"
# session = requests.Session()
resp = requests.get(url)
# print(resp.text)
# for i in resp.text:
#     print(i)
soup = BeautifulSoup(resp.text, "html.parser")
# print(type(soup))
# for i in soup:
#     print(i)
