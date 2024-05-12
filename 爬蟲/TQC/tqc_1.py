import requests
from bs4 import BeautifulSoup

url = "https://www.codejudger.com/target/5201.html"
# session = requests.Session()
resp = requests.get(url)
soup = BeautifulSoup(resp.text, "html.parser")
# print(soup)





