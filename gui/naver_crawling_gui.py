from tkinter import *
import urllib.request
import json
import re
# from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import pandas as pd

client_id = "PGRfCTKzm4hKNt5VyMWv"
client_secret = "oVQoKJxgTV"


root = Tk()

e = Entry(root)
e.grid(row=3, column=0)


def myClick():

    text = e.get()
    keyword_arr = text.split(',')

    for keyword in keyword_arr:
        phone_numbers = []
        encText = urllib.parse.quote(keyword)

        for i in range(1, 1000, 99):

            url_blog = "https://openapi.naver.com/v1/search/blog?query=" + \
                encText + "&display=100&start={}&sort=sim".format(i)  # json 결과

            try:

                request = urllib.request.Request(url_blog)
                request.add_header("X-Naver-Client-Id", client_id)
                request.add_header("X-Naver-Client-Secret", client_secret)
                response = urllib.request.urlopen(request)
                rescode = response.getcode()
                if(rescode == 200):
                    response_body = response.read()
                    json_data = json.loads(response_body.decode('utf-8'))

                links = [i['link'] for i in json_data['items']]

                for link in links:

                    try:

                        link = link.replace('amp;', "")
                        blog_post_url = link
                        get_blog_post_content_code = requests.get(
                            blog_post_url)
                        get_blog_post_content_text = get_blog_post_content_code.text
                        get_blog_post_content_soup = BeautifulSoup(
                            get_blog_post_content_text, 'lxml')

                        select = get_blog_post_content_soup.find('iframe')
                        new_link = 'https://blog.naver.com' + select['src']
                        html = urllib.request.urlopen(new_link)
                        soup = BeautifulSoup(html, 'html.parser')
                        matches = soup.find_all(
                            string=re.compile('010-\d{4}-\d{4}'))

                    except:
                        pass

                    for match in matches:
                        match_index = match.find('010')
                        phone_numbers.append(
                            match[match_index:match_index + 13])

            except:
                pass

        for i in range(1, 1000, 99):
            url_blog = "https://openapi.naver.com/v1/search/blog?query=" + \
                encText + \
                "&display=100&start={}&sort=date".format(i)  # json 결과

            try:

                request = urllib.request.Request(url_blog)
                request.add_header("X-Naver-Client-Id", client_id)
                request.add_header("X-Naver-Client-Secret", client_secret)
                response = urllib.request.urlopen(request)
                rescode = response.getcode()
                if(rescode == 200):
                    response_body = response.read()
                    json_data = json.loads(response_body.decode('utf-8'))

                links = [i['link'] for i in json_data['items']]

                for link in links:

                    try:

                        link = link.replace('amp;', "")
                        blog_post_url = link
                        get_blog_post_content_code = requests.get(
                            blog_post_url)
                        get_blog_post_content_text = get_blog_post_content_code.text
                        get_blog_post_content_soup = BeautifulSoup(
                            get_blog_post_content_text, 'lxml')

                        select = get_blog_post_content_soup.find('iframe')
                        new_link = 'https://blog.naver.com' + select['src']
                        html = urllib.request.urlopen(new_link)
                        soup = BeautifulSoup(html, 'html.parser')
                        matches = soup.find_all(
                            string=re.compile('010-\d{4}-\d{4}'))

                    except:
                        pass

                    for match in matches:
                        match_index = match.find('010')
                        phone_numbers.append(
                            match[match_index:match_index + 13])

            except:
                pass

        df = pd.DataFrame(phone_numbers, columns=['phone_numbers'])
        df.to_csv("{}.csv".format(keyword), index=False)


myLabel1 = Label(root, text="여러 검색어를 입력할시 ,로 구분하여 입력해주세요.")
myLabel2 = Label(root, text="예시) 맛집,족발집,배달집")
myButton = Button(root, text="Start Crawling", command=myClick)


myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=0)
myButton.grid(row=2, column=0)


root.mainloop()
