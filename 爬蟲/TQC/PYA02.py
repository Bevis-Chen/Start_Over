import requests, re
from bs4 import BeautifulSoup

url = "https://www.codejudger.com/target/5201.html"
# 使用 GET 請求
resp = requests.get(url)
# 驗證HTTP Status Code
if resp.status_code == 200:
    # 欲搜尋的字串
    key = input("請輸入欲搜尋的字串 : ")
    ans1 = re.findall(key, resp.text)
    if key in resp.text:
        print(key, "搜尋成功")
        print(key, "出現 %d 次" % len(ans1))
    else:
        print(key, "搜尋失敗")
        print(key, "出現 0 次")
else:
    print("網頁下載失敗") 
    print()
