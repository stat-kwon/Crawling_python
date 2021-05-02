import requests
from bs4 import BeautifulSoup
URL = 'https://sports.news.naver.com/news.nhn?oid=076&aid=0003724055'
res = requests.get(URL,verify=False)
soup = BeautifulSoup(res.content, "html.parser")
print(soup)