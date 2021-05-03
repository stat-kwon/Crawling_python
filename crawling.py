import requests
from bs4 import BeautifulSoup
URL = 'https://news.v.daum.net/v/20210502202020111'
res = requests.get(URL)
soup = BeautifulSoup(res.content, "html.parser")
data = soup.find_all('div','layer_util layer_summary')

print(data.get_text())