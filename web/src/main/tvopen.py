#coding=utf-8

import requests
import xlwt
from bs4 import BeautifulSoup

def tvopen():
    res = requests.get('http://www.tvyan.com')
    # 爬取下来的编码是ISO-8859-1格式，需要转化为utf-8格式
    res.encoding= 'utf-8'
    soup = BeautifulSoup(res.text, 'html.parser')
    # tai = soup.select('.tai a')
    # for i in range(0, tai.__len__()):
    #     singleTv(i, tai[i]['href'])
    list = soup.select('.listclass a')
    # for i in range(0, list.__len__()):
    out_list = []
    for i in range(0, list.__len__()):
        out_list += listTv(list[i]['href'])

    for j in range(0, out_list.__len__()):
        singleTv(j, out_list[j])
    # print tai
    # print soup

def singleTv(i, url):
    # res = requests.get('http://www.tvyan.com' + url)
    res = requests.get('http://' + url)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'html.parser')
    tv_icon = soup.select('div .content img')[0].get("src")
    # print tv_icon
    introduction = soup.select('div .content').pop().text
    # print introduction
    name = soup.select('.place h1').pop().text
    print name
    print i
    saveTvInforma(i, name, introduction, tv_icon)
    # print soup

def listTv(url):
    realUrl = 'http://www.tvyan.com' + url
    res = requests.get(realUrl)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'html.parser')
    pageList = soup.select('.pagelist li a')[:-2]
    tvUrl = []
    tvUrl += listSinglePage(realUrl)
    for i in range(0, pageList.__len__()):
        tvUrl = tvUrl + listSinglePage(realUrl + pageList[i].get('href'))
        # pageListUrl.append(realUrl + pageList[0].get('href'))
    # print 111
    # print tvUrl
    newTvUrl = list(set(tvUrl))
    return newTvUrl

def listSinglePage(url):
    res = requests.get(url)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'html.parser')
    tvList = soup.select('.tv li a')
    tvListUrl = []
    for i in range(0,tvList.__len__()):
        tvListUrl.append(tvList[i].get('href')[2:])
    return tvListUrl


def saveTvInforma(i, name, introduction, icon):
    workbook1.write(i, 0, name)
    workbook1.write(i, 1 , introduction)
    link = 'HYPERLINK("%s";"%s")' % ( 'http://www.tvyan.com' + icon, 'http://www.tvyan.com' + icon )
    workbook1.write(i, 2, xlwt.Formula(link))
    workbook.save(r'/Users/shucan/python_pachong/excel/tv.xlsx')

workbook = xlwt.Workbook(encoding='utf-8')
workbook1 = workbook.add_sheet("tv")
tvopen()
