import requests
from bs4 import BeautifulSoup
import openpyxl

'''
< 21.05.03 >
혼자 힘으로 네이버 뉴스 기사 크롤링 후 엑셀 파일에 저장 까지 해보았다.
title은 뉴스 제목, info는 신문사 종류를 나타내는 두 정보를 각 컬럼에 할당하여 엑셀에 저장하는 코드이다.
보안해야할 점은 코드의 가독성을 위해 구조개선이 필요해 보인다. 특히 title, info의 경로가 거의 비슷한 것을 활용해
for css in [title, info]: 를 유사하게 넣어 개선할 수 있지않을까 생각한다.

'''

url = 'https://search.naver.com/search.naver?where=news&sm=tab_pge&query=%EC%B9%B4%EC%B9%B4%EC%98%A4&sort=0&photo=0&field=0&pd=0&ds=&de=&cluster_rank=45&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so:r,p:all,a:all&start='
title_css = "li > div.news_wrap.api_ani_send > div > a"
info_css = "li > div.news_wrap.api_ani_send > div > div.news_info > div > a.info.press"
num = 10

# crawling function
def crawling_news(url, title_css, num):
    news_titles = list()
    for i in range(1, num+1):
        res = requests.get(url + str(((i-1)*9)+i))
        soup = BeautifulSoup(res.content, 'html.parser')
        data = soup.select(title_css)
        
        for item in data:
            news_titles.append([item.get_text()])
    return news_titles

title = crawling_news(url, title_css, num)
info = crawling_news(url, info_css, num)

# combine lists using zip function
data_all = list()
for a, b in zip(title, info):
    data_all.append([a[0],b[0]])
# print(data_all)

def write_excel_template(filename, sheetname, listdata):
    excel_file = openpyxl.Workbook()
    excel_sheet = excel_file.active
    excel_sheet.column_dimensions['A'].width = 100
    excel_sheet.column_dimensions['B'].width = 20
    
    if sheetname != '':
        excel_sheet.title = sheetname
    
    for item in listdata:
        excel_sheet.append(item)
    excel_file.save(filename)
    excel_file.close()

write_excel_template('카카오_크롤링.xlsx','',data_all)