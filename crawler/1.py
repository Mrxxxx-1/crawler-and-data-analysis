'''
Author: Mrx
Date: 2022-03-26 15:18:52
LastEditors: Mrx
LastEditTime: 2022-04-05 21:48:38
FilePath: \pcode\crawler\1.py
Description: 

Copyright (c) 2022 by Mrx, All Rights Reserved. 
'''

import sys
from urllib import response
from aiohttp import request
# 数据获取，网页解析
from bs4 import BeautifulSoup
# 正则表达式，进行文字匹配
import re
# 指定URL，获取网页数据
import urllib.error,urllib.request
from pyparsing import col
# 进行Excel操作
import xlwt

# 全局变量,正则表达式对象，即规则
# 电影链接
# 正则表达式前"r",即忽视表达式中的特殊符号
findLink = re.compile(r'<a href="(.*?)">')
findtitle = re.compile(r'<span class="title">(.*?)</span>')
findinfo = re.compile(r'<p class="">(.*?)</p>',re.S)
findrating = re.compile(r'<span class="rating_num" property="v:average">(.*?)</span>')
findintro = re.compile(r'<span class="inq">(.*?)</span>')
# 计数器
count = 0
def main() :
    baseurl = 'https://movie.douban.com/top250?start='
    # 1.爬取网页
    datalist = getData(baseurl)
    savepath = '.\\douban_top250.xls'
    # 2.解析数据
    # for item in datalist :
    #     print(item)
    # print(datalist)
    # 3.保存数据
    saveData(datalist,savepath)
    print('爬虫结束')


# 爬取网页
def getData(baseurl) :
    datalist = []
    for i in range(0, 10) :
        url = baseurl + str(i*25) + "&filter="
        print(url)
        html = askURL(url)
        soup = BeautifulSoup(html, "html.parser")
        for item in soup.find_all('div', class_= "item") :
            # print(item) 
            data = []
            global count
            count = count + 1
            item = str(item)
            # 通过正则表达式查找相应字符串
            link = re.findall(findLink, item)[0]
            data.append(link)
            title = re.findall(findtitle, item)
            if(len(title)==2) :
                ctitle = title[0]
                ftitle = title[1]
                f = ftitle[3:]
                # 去除外文名前三个字符“ / ”
                data.append(ctitle)
                data.append(f)
            else :
                ctitle = title[0]
                data.append(ctitle)
                data.append('none')
            # 只取列表第一项，作为字符串，便于后续操作
            info = re.findall(findinfo,item)[0]
            rating = re.findall(findrating,item)[0]
            intro = re.findall(findintro,item)
            if (len(intro)==0) :
                intro = 'empty'
            else :
                intro = intro[0]
            info = re.sub('\xa0','', info)
            info = re.sub(' ','',info)
            info = re.sub('...<br/>','',info)
            info = re.sub('\n','',info)
            data.append(info)
            data.append(rating)
            data.append(intro)
            datalist.append(data)
        #     print(info)
        #     print(rating)
        #     print(intro)
        print(count)
    # print(datalist)
    return datalist



    return datalist

# 得到指定一个URL的网页内容
def askURL(url) :
    head = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36 Edg/99.0.1150.52"}
    request = urllib.request.Request(url, headers=head)
    html = ""
    try :
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
    except urllib.error.URLError as e:
        if hasattr(e,"code") :
            print(e.code)
        if hasattr(e,"reason") :
            print(e.reason)
    finally :
        return html
# 保存数据
def saveData(datalist,savepath) :
    book = xlwt.Workbook(encoding="utf-8")
    sheet = book.add_sheet('top250')
    column = ("电影链接","影片中文名","影片外文名","相关信息","评分","简介")
    for i in range(0,6) :
        sheet.write(0,i,column[i])
    for i in range(0,250) :
        print("写入第{0}个电影".format(i+1))
        data = datalist[i]
        for j in range(0,6) :
            sheet.write(i+1,j,data[j])
    book.save(savepath)


if __name__ == '__main__' :
    main()