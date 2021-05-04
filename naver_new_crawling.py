import requests
from bs4 import BeautifulSoup
import openpyxl

client_id = 'uyUlZSJr9DFaokmRGARv'
client_pwd = '8ySfZ6fo2w'

excel_file = openpyxl.Workbook()
excel_sheet = excel_file.active
excel_sheet.column_dimensions['B'].witdth = 100
excel_sheet.column_dimensions['B'].witdth = 100
excel_sheet.append(['순위','상품 제목','링크'])

start, num = 1, 0
for i in range(10):
    start_num = start + ( i*100 )
    naver_open_api = 'https://openapi.naver.com/v1/search/shop.json?query=갤럭시&display=100&start=' + str(start_num)
    print(naver_open_api)
    header_params = {"X-Naver-Client-Id":client_id,
                     "X-Naver-Client-Secret":client_pwd}
    res = requests.get(naver_open_api, headers=header_params)
    
    if res.status_code == 200:
        data = res.json()
        for item in data['items']:
            num += 1
            print(num, item['title'], item['link'])
            excel_sheet.append([num, item['title'], item['link']])
    else:
        print('Error code:',res.status_code)

excel_file.save('naver_shopping1000.xlsx')
excel_file.close()