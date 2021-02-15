import urllib.request
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver
import time

ID = 'junkoony93'
PWD = 'Wnsdud93@'

def insta_login(id=ID, pwd=PWD):
    global driver
    driver.get("https://www.instagram.com/")
    # driver.find_elemnt_by_name
    # driver.find_element_by_id("identifierId").send_keys(id)
    time.sleep(2)
    driver.find_element_by_name("username").send_keys(id)
    driver.find_element_by_name("password").send_keys(pwd)
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button').click()
    time.sleep(8)
    try:
        driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()
    except:
        print('passed')
        pass

def profile():
    global driver
    driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[5]/span/img').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[5]/div[2]/div[2]/div[2]/a[1]').click()
    time.sleep(1)

def get_follows():
    global driver
    driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a').click()
    time.sleep(3)
    follows = driver.find_elements_by_xpath('/html/body/div[4]/div/div/div[2]/ul/div/li/div/div[2]/div[1]/div/div/span/a')
    for f in follows:
        print(f.text)
    

# /html/body/div[4]/div/div/div[2]/ul/div/li[1]/div/div[2]/div[1]/div/div/span/a
# /html/body/div[4]/div/div/div[2]/ul/div/li[2]/div/div[2]/div[1]/div/div/span/a
driver = webdriver.Chrome()  
insta_login()
profile()
get_follows()
# driver.close()

# base_url = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query='
# # keyword = input('검색할 태그를 입력하세요 : ')
# url = base_url + quote_plus(keyword)


# driver.get(url)

# time.sleep(5)

# html = driver.page_source
# soup = BeautifulSoup(html, 'html.parser')
# insta = soup.select('._image._listImage')
# print(len(insta))
# n = 1
# for i in insta:
#     imgUrl = i['src']
#     with urllib.request.urlopen(imgUrl) as f:
#         with open('./img/' + keyword + str(n) + '.jpg', 'wb') as h:
#             img = f.read()
#             h.write(img)

#     n += 1

# driver.close()