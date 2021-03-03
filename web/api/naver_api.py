import os
import sys
import urllib.request
import json
import re
from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests

client_id = "PGRfCTKzm4hKNt5VyMWv"
client_secret = "oVQoKJxgTV"
keyword = input("검색할 단어를 입력해주세요: ")
encText = urllib.parse.quote(keyword)
url = "https://openapi.naver.com/v1/search/blog?query=" + \
    encText + "&display=100"  # json 결과
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
request = urllib.request.Request(url)
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
# for i in json_data['items']:
# print(i['link'])
# print(json_data['items'])
# print(links)

# soup = BeautifulSoup(urllib.request.urlopen(
#     'http://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20161120').read(), 'html.parser')
# res = soup.find_all('div', 'tit5')
# print(res)

for link in links:

    link = link.replace('amp;', "")
    # get_blog_post_content_code = requests.get(link)
    # get_blog_post_content_text = get_blog_post_content_code.text

    # # print(get_blog_post_content_text)

    # get_blog_post_content_soup = BeautifulSoup(
    #     get_blog_post_content_text, 'lxml')

    # select = get_blog_post_content_soup.select('frame#mainFrame')
    # print(select)

    blog_post_url = link

    get_blog_post_content_code = requests.get(blog_post_url)
    get_blog_post_content_text = get_blog_post_content_code.text

    get_blog_post_content_soup = BeautifulSoup(
        get_blog_post_content_text, 'lxml')

    select = get_blog_post_content_soup.find('iframe')
    # print(select.extract())
    new_link = 'https://blog.naver.com' + select['src']

    html = urlopen(new_link)
    # print(html)
    soup = BeautifulSoup(html, 'html.parser')
    # print(soup)
    # for link in get_blog_post_content_soup.select('frame#mainFrame'):
    #     real_blog_post_url = "http://blog.naver.com" + link.get('src')

    #     get_real_blog_post_content_code = requests.get(real_blog_post_url)
    #     print(get_real_blog_post_content_code)
    #     get_real_blog_post_content_text = get_real_blog_post_content_code.text
    #     print(get_real_blog_post_content_text)
    #     get_real_blog_post_content_soup = BeautifulSoup(
    #         get_real_blog_post_content_text, 'lxml')
    # print(get_blog_post_content_soup)
    # html = urlopen(link)
    # # request = urllib.request.urlopen(link)
    # print(html)
    # soup = BeautifulSoup(html, 'html.parser')
    # print(soup)
    matches = soup.find_all(string=re.compile('/^\d{3}-\d{3,4}-\d{4}$/'))
    print(matches)
