import requests
from bs4 import BeautifulSoup

# urlのセット
url = 'https://www.python.org/'
r = requests.get(url)

# パース用オブジェクト
soup = BeautifulSoup(r.content,"lxml")

# aタグを抽出・出力
for a in soup.select('.blog-widget > .shrubbery > ul > li > a'):
    string = a.string
    print(string)
