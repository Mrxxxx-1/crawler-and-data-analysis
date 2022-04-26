'''
Author: Mrx
Date: 2022-03-26 20:05:29
LastEditors: Mrx
LastEditTime: 2022-03-26 20:51:20
FilePath: \pcode\crawler\testurllib.py
Description: 

Copyright (c) 2022 by Mrx, All Rights Reserved. 
'''


from urllib import response
import urllib.request

# 获取一个get请求,(超时处理)
# try : 
#     response = urllib.request.urlopen('http://httpbin.org/get')
#     print(response.read().decode('utf-8'))
# except urllib.error.URLError as e:
#     print("time out!")


# 获取一个post请求

import urllib.parse
# data = bytes(urllib.parse.urlencode({"hello":"world"}),encoding="utf-8")
# response = urllib.request.urlopen("http://httpbin.org/post", data = data)
# print(response.read().decode("utf-8"))

# post请求，浏览器req请求加入浏览器信息封装，以伪装不是爬虫
data = bytes(urllib.parse.urlencode({'hello there':'yep'}),encoding='utf-8')
url = 'http://httpbin.org/post'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36 Edg/99.0.1150.46'
}
req = urllib.request.Request(url = url, data = data, headers = headers, method = 'POST')
response = urllib.request.urlopen(req)
print(response.read().decode('utf-8'))