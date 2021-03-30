import urllib.request
from bs4 import BeautifulSoup
import urllib.parse
from selenium import webdriver
import time
import pandas as pd
import openpyxl
from tkinter import *
import os

root = Tk()
root.geometry('300x150')

e = Entry(root)
e.place(relx=0.3, rely=0.4)


def myClick():
    keyword = e.get()

    df = pd.read_excel('종목코드.xlsx')
    code = df.loc[df['name'] == keyword, 'code'].iloc[0]

    for i in range(6 - len(str(code))):
        code = '0' + str(code)

    url_annual = 'https://m.stock.naver.com/item/main.nhn#/stocks/{}/annual'.format(
        code)

    option = webdriver.ChromeOptions()
    option.add_argument('headless')
    browser = webdriver.Chrome(options=option)
    browser.get(url_annual)

    time.sleep(2)

    net_profit = browser.find_elements_by_xpath(
        '/html/body/div[2]/div[1]/div[2]/div[1]/div[2]/div/div/table/tbody/tr[2]/td/span')

    periods = browser.find_elements_by_xpath(
        '/html/body/div[2]/div[1]/div[2]/div[1]/div[2]/div/div/table/thead/tr/th/span/span[1]')

    actual_profit = browser.find_elements_by_xpath(
        '/html/body/div[2]/div[1]/div[2]/div[1]/div[2]/div/div/table/tbody/tr[3]/td/span')

    url_quarter = 'https://m.stock.naver.com/item/main.nhn#/stocks/{}/quarter'.format(
        code)

    wb = openpyxl.load_workbook("base_excel.xlsx")

    sh1 = wb['Sheet1']

    # 연간 기간
    sh1['C6'] = periods[0].text[:7]
    sh1['D6'] = periods[1].text[:7]
    sh1['E6'] = periods[2].text[:7]
    sh1['F6'] = periods[3].text[:7]

    # 연간 영업이익
    sh1['C7'] = net_profit[0].text
    sh1['D7'] = net_profit[1].text
    sh1['E7'] = net_profit[2].text
    sh1['F7'] = net_profit[3].text

    # 연간 영업이익 성장률
    # ( current - previous ) / previous
    # sh1['C8'] = 'N/A'

    if sh1['D7'].value != '' and sh1['C7'].value != '' and sh1['C7'].value != '0':
        sh1['D8'] = (int(sh1['D7'].value.replace(',', '')) -
                     int(sh1['C7'].value.replace(',', ''))) / abs(int(sh1['C7'].value.replace(',', '')))

    if sh1['E7'].value != '' and sh1['D7'].value != '' and sh1['D7'].value != '0':
        sh1['E8'] = (int(sh1['E7'].value.replace(',', '')) -
                     int(sh1['D7'].value.replace(',', ''))) / abs(int(sh1['D7'].value.replace(',', '')))

    if sh1['E7'].value != '' and sh1['F7'].value != '' and sh1['E7'].value != '0':
        sh1['F8'] = (int(sh1['F7'].value.replace(',', '')) -
                     int(sh1['E7'].value.replace(',', ''))) / abs(int(sh1['E7'].value.replace(',', '')))

    # 연간 당기순이익
    sh1['C9'] = actual_profit[0].text
    sh1['D9'] = actual_profit[1].text
    sh1['E9'] = actual_profit[2].text
    sh1['F9'] = actual_profit[3].text

    # 연간 당기순이익 성장률
    # sh1['C10'] = 'N/A'
    if sh1['D9'].value != '' and sh1['C9'].value != '' and sh1['C9'].value != '0':
        sh1['D10'] = (int(sh1['D9'].value.replace(',', '')) -
                      int(sh1['C9'].value.replace(',', ''))) / abs(int(sh1['C9'].value.replace(',', '')))

    if sh1['E9'].value != '' and sh1['D9'].value != '' and sh1['D9'].value != '0':
        sh1['E10'] = (int(sh1['E9'].value.replace(',', '')) -
                      int(sh1['D9'].value.replace(',', ''))) / abs(int(sh1['D9'].value.replace(',', '')))

    if sh1['F9'].value != '' and sh1['E9'].value != '' and sh1['E9'].value != '0':
        sh1['F10'] = (int(sh1['F9'].value.replace(',', '')) -
                      int(sh1['E9'].value.replace(',', ''))) / abs(int(sh1['E9'].value.replace(',', '')))

    browser.get(url_quarter)

    time.sleep(2)

    net_profit_quarter = browser.find_elements_by_xpath(
        '/html/body/div[2]/div[1]/div[2]/div[1]/div[2]/div/div/table/tbody/tr[2]/td/span')

    periods_quarter = browser.find_elements_by_xpath(
        '/html/body/div[2]/div[1]/div[2]/div[1]/div[2]/div/div/table/thead/tr/th/span/span[1]')

    actual_profit_quarter = browser.find_elements_by_xpath(
        '/html/body/div[2]/div[1]/div[2]/div[1]/div[2]/div/div/table/tbody/tr[3]/td/span')

    # 분기 기간
    sh1['C12'] = periods_quarter[2].text[:7]
    sh1['D12'] = periods_quarter[3].text[:7]
    sh1['E12'] = periods_quarter[4].text[:7]
    sh1['F12'] = periods_quarter[5].text[:7]

    # 분기 영업이익
    sh1['C13'] = net_profit_quarter[2].text
    sh1['D13'] = net_profit_quarter[3].text
    sh1['E13'] = net_profit_quarter[4].text
    sh1['F13'] = net_profit_quarter[5].text

    # 분기 영업이익 성장률
    # sh1['C14'] = 'N/A'
    if sh1['D13'].value != '' and sh1['C13'].value != '' and sh1['C13'].value != '0':
        sh1['D14'] = (int(sh1['D13'].value.replace(',', '')) -
                      int(sh1['C13'].value.replace(',', ''))) / abs(int(sh1['C13'].value.replace(',', '')))

    if sh1['E13'].value != '' and sh1['D13'].value != '' and sh1['D13'].value != '0':
        sh1['E14'] = (int(sh1['E13'].value.replace(',', '')) -
                      int(sh1['D13'].value.replace(',', ''))) / abs(int(sh1['D13'].value.replace(',', '')))

    if sh1['F13'].value != '' and sh1['E13'].value != '' and sh1['E13'].value != '0':
        sh1['F14'] = (int(sh1['F13'].value.replace(',', '')) -
                      int(sh1['E13'].value.replace(',', ''))) / abs(int(sh1['E13'].value.replace(',', '')))

    # 분기 당기순이익
    sh1['C15'] = actual_profit_quarter[2].text
    sh1['D15'] = actual_profit_quarter[3].text
    sh1['E15'] = actual_profit_quarter[4].text
    sh1['F15'] = actual_profit_quarter[5].text

    # 분기 당기순이익 성장률
    # sh1['C16'] = 'N/A'

    if sh1['D15'].value != '' and sh1['C15'].value != '' and sh1['C15'].value != '0':
        sh1['D16'] = (int(sh1['D15'].value.replace(',', '')) -
                      int(sh1['C15'].value.replace(',', ''))) / abs(int(sh1['C15'].value.replace(',', '')))

    if sh1['D15'].value != '' and sh1['E15'].value != '' and sh1['D15'].value != '0':
        sh1['E16'] = (int(sh1['E15'].value.replace(',', '')) -
                      int(sh1['D15'].value.replace(',', ''))) / abs(int(sh1['D15'].value.replace(',', '')))

    if sh1['F15'].value != '' and sh1['E15'].value != '' and sh1['E15'].value != '0':
        sh1['F16'] = (int(sh1['F15'].value.replace(',', '')) -
                      int(sh1['E15'].value.replace(',', ''))) / abs(int(sh1['E15'].value.replace(',', '')))

    if os.path.exists("{}.xlsx".format(keyword)):
        os.remove("{}.xlsx".format(keyword))

    wb.save('{}.xlsx'.format(keyword))


myLabel1 = Label(root, text="종목명을 정확히 입력해주세요.")
myButton = Button(root, text="시작", command=myClick)

# Label_middle.place(relx=0.5,
#                    rely=0.5,
#                    anchor='center')

myLabel1.place(relx=0.25, rely=0.1)
myButton.place(relx=0.5, rely=0.7)


root.mainloop()
