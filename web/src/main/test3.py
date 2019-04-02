#coding=utf-8


import requests
from bs4 import BeautifulSoup

def imgurl(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    page = int(soup.select('.pagenavi span')[-2].text)  #获取总页数，-2为去掉上下页
    src = soup.select('.main-image a img')[0].get('src')
    beautifulgirlid = src[-9:-6]
    print ('开始下载妹子:' , format(beautifulgirlid))  # 输出窗口提示下载
    for i in range(1, page + 1):
        i = '%02d' % i
        img = src.replace('01.jpg', str(i)+'.jpg')
        headers = { 'User-Agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)', 'Referer': 'http://www.mzitu.com' }
        response = requests.get(img, headers=headers)
        f = open('/Users/shucan/python_pachong/beautiful_girl/'+ beautifulgirlid +'%s.jpg' % i, 'wb')
        f.write(response.content)
        print( beautifulgirlid + i)
    print '输出妹子id'
    print(beautifulgirlid)

def imgpage(page):
    res = requests.get('http://www.mzitu.com/page/' + str(page))
    soup = BeautifulSoup(res.text, 'html.parser')
    print soup
    href = soup.select('#pins a')
    # print '开始挑选'
    # print href
    list = set([i.get('href') for i in href])
    print list
    # [imgurl(i) for i in list]
    # imgpage_select_one(list.pop())


def imgpage_select_one(url):
    print url
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    print soup
    page = int(soup.select('.pagenavi span')[-2].text)
    print page

result = input('下载那一页:')
imgpage(result)

