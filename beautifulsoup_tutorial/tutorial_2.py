import urllib.request
from bs4 import BeautifulSoup
import urllib.parse

base_url = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query='
keyword = input('검색어를 입력하세요:')
keyword = urllib.parse.quote_plus(keyword)
# url = 'https://www.google.com/search?q={}&sxsrf=ALeKk01J4QxRUq50rddwmDnVJ_9QKvOfIA:1612279428436&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiU0fD0wMvuAhXFMN4KHdRVAucQ_AUoAXoECAgQAw&biw=768&bih=720'.format(keyword)
url = base_url + keyword
print(url)
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
# print(soup)
images = soup.find_all(class_='_image _listImage')
print(images)
# print(title)

# for i in images:
#     print(i['src'])
#     print()
