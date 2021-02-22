import urllib.request
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import os

ID = 'junkoony93'
PWD = 'Wnsdud93@'
SCROLL_PAUSE_SEC = 2
SCROLL_FLAG = True

def scroll_down():
    global driver
    last_height = driver.execute_script("return document.body.scrollHeight")
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(SCROLL_PAUSE_SEC)
    new_height = driver.execute_script("return document.body.scrollHeight")
    print("scroll down")

    if new_height == last_height:
        return False
        print("set scroll down false")
    
    return True


def insta_login(id=ID, pwd=PWD):
    global driver
    driver.get("https://www.instagram.com/")
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

def prompt_id():
    global driver
    id = input('크롤링할 아이디를 입력하세요 : ')
    url = 'https://www.instagram.com/{}/'.format(id)
    driver.get(url)
    time.sleep(1)
    return id

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
    follows_arr = [f.text for f in follows]
    return follows_arr

def first_download(id):
    global driver

    if not os.path.exists('img/{}'.format(id)):
        os.makedirs('img/{}'.format(id))
    
    driver.get("https://www.instagram.com/{}".format(id))

    SCROLL_FLAG = True
    time.sleep(1)

    while SCROLL_FLAG:

        if scroll_down() is not True:
            SCROLL_FLAG = False
        
        print(SCROLL_FLAG)

        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')   
        pics = soup.find_all('img', attrs={'class':'FFVAD'})

        for p in pics:
            
            try:
                imgUrl = p['src']
                # print(imgUrl)
            except:
                print('no src')
                pass
            
            with urllib.request.urlopen(imgUrl) as f:
                with open('./img/{}/'.format(id) + imgUrl[-8:] + '.jpg', 'wb') as h:
                    img = f.read()
                    h.write(img)



def download_realtime(id):
    global driver

    while True:

        driver.refresh()
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')   
        pics = soup.find_all('img', attrs={'class':'FFVAD'})

        for p in pics:
            
            try:
                imgUrl = p['src']
                # print(imgUrl)
            except:
                print('no src')
                pass
            
            with urllib.request.urlopen(imgUrl) as f:
                with open('./img/{}/'.format(id) + imgUrl[-8:] + '.jpg', 'wb') as h:
                    img = f.read()
                    h.write(img)

        time.sleep(30)
        
    
driver = webdriver.Chrome()  
id = input('크롤링할 아이디를 입력하세요 : ')
insta_login()
first_download(id)
download_realtime(id)
