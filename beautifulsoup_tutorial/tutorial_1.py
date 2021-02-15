import urllib.request
from bs4 import BeautifulSoup
import urllib.parse

base_url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query='
plus_url = input('검색어를 입력하세요: ')
url = base_url + urllib.parse.quote_plus(plus_url)
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
print(soup)
title = soup.find_all(class_='api_txt_lines total_tit')

# print(title)

# for i in title:
#     print(i.text)
