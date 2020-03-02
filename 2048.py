#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import requests
import time
import json
from lxml import etree  #一种解析方式
from bs4 import BeautifulSoup #另一种解析方式

#打开网页函数，返里网页文字

#网址，字符串前加f传递变量
url = 'http://hjd.fxgrt2048.net/2048/thread.php?fid-57-page-1.html'
#伪装浏览器
header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'}
#访问网页
Response = requests.get(url, headers=header).text

#soup = BeautifulSoup(Response.text, 'lxml')
page = etree.HTML(Response)
print(page)
# titles = page.xpath("//*[@id="a_ajax_1835600"]")
# print(titles)




#for i in range(9, 11):
    #titles = soup.select(f'#ajaxtable > tbody:nth-child(2) > tr:nth-child({i}) > td > a ')[0]

    #// *[ @ id = "a_ajax_1840683"]
    #// *[ @ id = "a_ajax_1838435"]
    #// *[ @ id = "a_ajax_1835600"]

   # html = titles.get_text()
    # print(titles, type(titles))
    #print(html)





