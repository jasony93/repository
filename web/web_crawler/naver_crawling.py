import urllib.request
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver
import time

SCROLL_PAUSE_SEC = 1


def scroll_down():
    global driver
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(SCROLL_PAUSE_SEC)
        new_height = driver.execute_script("return document.body.scrollHeight")

        if new_height == last_height:
            time.sleep(SCROLL_PAUSE_SEC)
            new_height = driver.execute_script(
                "return document.body.scrollHeight")

            if new_height == last_height:
                print('SCROLLED TO BOTTOM!!!')
                break

        last_height = new_height


keyword = input('검색할 태그를 입력하세요 : ')
url = 'https://search.naver.com/search.naver?where=view&sm=tab_jum&query={}'.format(
    keyword)

option = webdriver.ChromeOptions()
# option.add_argument('headless')
driver = webdriver.Chrome()
driver.get(url)

time.sleep(1)
scroll_down()

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
links = soup.find_all('a', attrs={'class': 'api_txt_lines total_tit'})


print('number of link: ', len(links))

# n = 1
# for i in images:
#     try:
#         imgUrl = i["src"]
#     except:
#         imgUrl = i["data-src"]
#     # imgUrl = i["data-src"]
#     # print(imgUrl)
#     with urllib.request.urlopen(imgUrl) as f:
#         with open('./img/' + keyword + str(n) + '.jpg', 'wb') as h:
#             img = f.read()
#             h.write(img)

#     n += 1

# driver.close()
