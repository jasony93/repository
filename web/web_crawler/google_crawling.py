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

            try:
                driver.find_element_by_class_name("mye4qd").click()
            except:

                if new_height == last_height:
                    break

        last_height = new_height


def google_login(id, pwd):
    global driver
    driver.get("https://accounts.google.com/signin/v2/identifier?hl=ko&passive=true&continue=https%3A%2F%2Fwww.google.com%2F&ec=GAZAAQ&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
    driver.find_element_by_id("identifierId").send_keys(id)
    driver.find_element_by_class_name("VfPpkd-RLmnJb").click()

    # elem = driver.find_element_by_class_name("gb_be gb_4 gb_5c")
    # elem.click()


keyword = input('검색할 태그를 입력하세요 : ')
url = 'https://www.google.com/search?q={}&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjgwPKzqtXuAhWW62EKHRjtBvcQ_AUoAXoECBEQAw&biw=768&bih=712'.format(
    keyword)

option = webdriver.ChromeOptions()
option.add_argument('headless')
driver = webdriver.Chrome(options=option)
driver.get(url)

time.sleep(1)

# google_login('jasony9393@gmail.com','b')
scroll_down()

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
images = soup.find_all('img', attrs={'class': 'rg_i Q4LuWd'})

print('number of img tags: ', len(images))

n = 1
for i in images:
    try:
        imgUrl = i["src"]
    except:
        imgUrl = i["data-src"]
    # imgUrl = i["data-src"]
    # print(imgUrl)
    with urllib.request.urlopen(imgUrl) as f:
        with open('./img/' + keyword + str(n) + '.jpg', 'wb') as h:
            img = f.read()
            h.write(img)

    n += 1

# driver.close()
