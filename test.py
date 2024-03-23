import requests
from bs4 import BeautifulSoup

html_doc = '''
<html>
<head>
<title>這是HTML文件標題</title>
</head>
<body>
<h1 id="article" class="banner">網頁標題１</h1>
<p data-author='aaron' class="reqular text-normal">文章段落１</p>
<a class="link no btn" href="https://www.aaronlife.com/ref1">參考<b>資料</b>連結１</a>
<a class="link btn" href="https://www.aaronlife.com/ref2">參考<b>資料</b>連結２</a>
<a class="link btn" href="https://www.aaronlife.com/ref2">參考資料連結３</a>
<a class="link btn" href="https://www.aaronlife.com/ref2">參考資料連結４</a>
<p>這是一份<b class="boldtext">HTML文件</b>。</p>
<h2 id="article1" class="banner">網頁標題２</h2>
<p data-author='andy' class="reqular text-normal">文章段落２</p>
<h2 id="article2" class="title normal">網頁標題３</h2>
<p data-author='william' class="reqular text-normal">文章段落３</p>
</body>
</html>
'''

# 建立BeautifulSoup物件解析HTML文件
soup = BeautifulSoup(html_doc, 'html.parser')

# 透過標籤來定位元素
result = soup.select('a')
print('select a:', result)
print("*" * 60)
result = soup.select('body p b')
print('select p b:', result)
