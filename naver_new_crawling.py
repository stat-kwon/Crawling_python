import requests
from bs4 import BeautifulSoup

client_id = 'uyUlZSJr9DFaokmRGARv'
client_pwd = '8ySfZ6fo2w'

start, num = 1, 0
for i in range(10):
    start_num = start + ( num*100 )
    naver_open_api = 'https://openapi.naver.com/v1/search/shop.json?query=샤오미&display=100&start=' + str(start_num)
    header_params = {"X-Naver-Client-Id":client_id,
                     "X-Naver-Client-Secret":client_pwd}
    res = requests.get(naver_open_api, headers=header_params)
    
    if res.status_code == 200:
        data = res.json()
        for num, item in data['items']:
            num += 1
            print(num, item['title'], item['link'])
    else:
        print('Error code:',res.status_code)