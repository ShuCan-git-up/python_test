#coding=utf-8


import xlrd
import xlwt
from bs4 import BeautifulSoup
import requests

def merge_two_dicts(x, y):
    """Given two dicts, merge them into a new dict as a shallow copy."""
    z = x.copy()
    z.update(y)
    return z

def request(url):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                            'Chrome/51.0.2704.63 Safari/537.36'}
    res = requests.get(url,headers = headers)
    res.encoding='utf-8'
    soup = BeautifulSoup(res.text, 'html.parser')
    return soup

def readfromxlsl(url):
    myWorkBook = xlrd.open_workbook(url)
    table = myWorkBook.sheet_by_name('province_url')
    return table

# 单个province里面所有可能的电视台列表值url
def channelTimeUrl(url, name):
    totalProgram = {}
    provinceNameBook = workbook.add_sheet(name)
    soup = request(url)
    channelsBig = soup.select('.chlsnav a')
    channelsSmall = soup.select('.chlsnav ul a')
    pbarName = ''
    pbar = soup.select('.pbar')
    if pbar.__len__() == 0:
        pbarName = '获取名称失败，进入链接获取名称'
    else:
        pbarName = pbar.pop().text
    programTable = {}
    for i in range(0, channelsBig.__len__()):
        programTable[channelsBig[i].get('title')] = 'https://www.tvmao.com' + channelsBig[i].get('href')
    for i in range(0, channelsSmall.__len__()):
        title = channelsSmall[i].get('title')
        if programTable.has_key(title):
            programTable.pop(title)
    programTable[pbarName] = url
    for key in programTable.keys():
        dict = channelTime(programTable[key])
        if dict is None:
            continue
        else:
            totalProgram = merge_two_dicts(dict, totalProgram)
    i = 0
    for key in totalProgram.keys():
        provinceNameBook.write(i, 0, key)
        provinceNameBook.write(i ,1, totalProgram[key])
        i = i + 1
    workbook.save(r'/Users/shucan/python_pachong/excel/'+ name +'.xlsx')

def channelTime(url):
    soup = request(url)
    channelSmall = soup.select('.chlsnav ul li')
    if channelSmall.__len__() == 0:
        return None
    programName = channelSmall.pop(0).text
    programTable = {}
    programTable[programName] = url
    for i in range(0, channelSmall.__len__()):
        try:
            programTable[channelSmall[i].select('a')[0].get('title')] = 'https://www.tvmao.com' + channelSmall[i].select('a')[0].get('href')
        except BaseException:
            print "插入异常，异常数据", channelSmall[i]
    programTable.__len__()
    return programTable


workbook = xlwt.Workbook(encoding='utf-8')
table = readfromxlsl('/Users/shucan/python_pachong/excel/province_url.xlsx')
for i in range(0, table.nrows):
    channelTimeUrl(table.cell(i, 1).value, table.cell(i, 0).value)
# for i in range(0, table.nrows):
#     name = table.cell(i, 0).value
#     url = table.cell(i, 1).value