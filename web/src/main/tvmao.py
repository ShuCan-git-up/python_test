#coding=utf-8

import requests
import xlwt
from bs4 import BeautifulSoup
import urllib3,random
from Tkinter import *
import sys

#
# my_headers=[
#     "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",
#     "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36",
#     "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0",
#     "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14",
#     "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)"
# ]

def getIndex(url):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                            'Chrome/51.0.2704.63 Safari/537.36'}
    res = requests.get(url,headers = headers)
    res.encoding='utf-8'
    soup = BeautifulSoup(res.text, 'html.parser')
    provinceContentUrl = soup.select('.ml20')
    province_url_dictionary = {}
    for i in range(0, provinceContentUrl.__len__()):
        workbook1.write(i, 0, provinceContentUrl[i].text)
        workbook1.write(i, 1, 'https://www.tvmao.com' + provinceContentUrl[i].get('href'))
        province_url_dictionary[provinceContentUrl[i].text] = 'https://www.tvmao.com' + provinceContentUrl[i].get('href')
    workbook1.write(provinceContentUrl.__len__(), 0 , '中央台')
    workbook1.write(provinceContentUrl.__len__(), 1 , 'https://www.tvmao.com' + '/program/CCTV1')
    workbook.save(r'/Users/shucan/python_pachong/excel/province_url.xlsx')
    print soup

def getLocation(url):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                            'Chrome/51.0.2704.63 Safari/537.36'}
    res = requests.get(url,headers = headers)
    res.encoding='utf-8'
    soup = BeautifulSoup(res.text, 'html.parser')
    print soup

def tkinter_window():
    root = Tk()
    label = Label(root,text="Hello Tkinter")
    label.pack()
    root.mainloop()

workbook = xlwt.Workbook(encoding='utf-8')
workbook1 = workbook.add_sheet("province_url")
getIndex('https://www.tvmao.com')
# getLocation('https://m.tvmao.com/program/playing/cctv')
