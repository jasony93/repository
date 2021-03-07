# import os
# import sys
import urllib.request
import json
import re
# from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import pandas as pd
# import pandas.DataFrame

client_id = "PGRfCTKzm4hKNt5VyMWv"
client_secret = "oVQoKJxgTV"
keywords = input("검색할 단어들을 입력해주세요: ")

keyword_arr = keywords.split(',')

for keyword in keyword_arr:
    phone_numbers = []
    encText = urllib.parse.quote(keyword)

    for i in range(1, 50, 99):
        print('start index: ', i)
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
                # print(response_body.decode('utf-8'))
                json_data = json.loads(response_body.decode('utf-8'))
            else:
                print("Error Code:" + rescode)

            links = [i['link'] for i in json_data['items']]

            for link in links:

                try:

                    link = link.replace('amp;', "")
                    blog_post_url = link
                    get_blog_post_content_code = requests.get(blog_post_url)
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
                    print(match[match_index:match_index + 13])
                    phone_numbers.append(match[match_index:match_index + 13])

        except:
            pass

    for i in range(1, 50, 99):
        print('start index: ', i)
        url_blog = "https://openapi.naver.com/v1/search/blog?query=" + \
            encText + "&display=100&start={}&sort=date".format(i)  # json 결과

        try:

            request = urllib.request.Request(url_blog)
            request.add_header("X-Naver-Client-Id", client_id)
            request.add_header("X-Naver-Client-Secret", client_secret)
            response = urllib.request.urlopen(request)
            rescode = response.getcode()
            if(rescode == 200):
                response_body = response.read()
                # print(response_body.decode('utf-8'))
                json_data = json.loads(response_body.decode('utf-8'))
            else:
                print("Error Code:" + rescode)

            links = [i['link'] for i in json_data['items']]

            for link in links:

                try:

                    link = link.replace('amp;', "")
                    blog_post_url = link
                    get_blog_post_content_code = requests.get(blog_post_url)
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
                    print(match[match_index:match_index + 13])
                    phone_numbers.append(match[match_index:match_index + 13])

        except:
            pass

    df = pd.DataFrame(phone_numbers, columns=['phone_numbers'])
    df.to_csv("{}.csv".format(keyword), index=False)

# for i in range(1, 500, 99):
#     print('start index: ', i)
#     url_caffe = "https://openapi.naver.com/v1/search/cafearticle.json?query=" + \
#         encText + "&display=30&start={}".format(i)

#     request = urllib.request.Request(url_caffe)
#     request.add_header("X-Naver-Client-Id", client_id)
#     request.add_header("X-Naver-Client-Secret", client_secret)
#     response = urllib.request.urlopen(request)
#     rescode = response.getcode()
#     if(rescode == 200):
#         response_body = response.read()
#         # print(response_body)
#         # print(response_body.decode('utf-8'))
#         json_data = json.loads(response_body.decode('utf-8'))
#         # print(json_data)
#     else:
#         print("Error Code:" + rescode)

#     links = [i['link'] for i in json_data['items']]

#     # print(links)

#     for link in links:

#         link = link.replace('amp;', "")
#         blog_post_url = link
#         get_blog_post_content_code = requests.get(blog_post_url)
#         get_blog_post_content_text = get_blog_post_content_code.text
#         # print(get_blog_post_content_text)
#         # print(get_blog_post_content_text)
#         get_blog_post_content_soup = BeautifulSoup(
#             get_blog_post_content_text, 'lxml')
#         # print(get_blog_post_content_soup)
#         select = get_blog_post_content_soup.find(
#             'input', attrs={'name': 'clubid'})

#         link_split = link.split('/')
#         article_id = link_split[-1]
#         # print('article_id: ', article_id, '  club_id: ', select['value'])
#         # print(select)
#         new_link = 'https://cafe.naver.com/ArticleRead.nhn?articleid={}&clubid={}'.format(
#             article_id, select['value'])
#         # print(new_link)
#         html = urllib.request.urlopen(new_link)
#         soup = BeautifulSoup(html, 'html.parser')
#         # print(soup)
#         matches = soup.find_all(string=re.compile('010-\d{4}-\d{4}'))

#         for match in matches:
#             match_index = match.find('010')
#             print(match[match_index:])
#             phone_numbers.append(match[match_index:])


# //cafe.naver.com/ArticleRead.nhn?articleid=1830954&clubid=21031223
