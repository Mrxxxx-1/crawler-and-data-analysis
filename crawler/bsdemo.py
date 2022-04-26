'''
Author: Mrx
Date: 2022-03-27 19:09:00
LastEditors: Mrx
LastEditTime: 2022-03-28 16:34:04
FilePath: \pcode\crawler\bsdemo.py
Description: 

Copyright (c) 2022 by Mrx, All Rights Reserved. 
'''

from bs4 import BeautifulSoup

file = open("crawler\\baidu.html","rb")
html = file.read()
bs = BeautifulSoup(html,"html.parser")

# tag,标签及其内容：拿到它所找到的第一个内容
print(bs.title)
print(bs.head)
print(type(bs.head))
print(bs.a)

# 仅打印标签内容
print(bs.title.string) # 字符串
print(bs.a.attrs) # 标签内属性
print(bs.a.string)

# html文档的遍历
print(bs.head.contents) 
# .content将tag的子节点以列表的方式输出
print(bs.head.contents[1])
# 用列表索引来获取它的某一元素

# html文档的搜索
# 字符串过滤，查找与字符串完全匹配的内容

t_list = bs.find_all("a")
print(t_list)

# # 正则表达式搜索
import re
t_list1 = bs.find_all(re.compile("a"))

print(t_list1)

# 传入一个函数(方法)，根据函数要求来搜索
def name(tag) :
    return tag.has_attr("name")

t_list2 = bs.find_all(name)
print(t_list2)
# 打印列表方式
for item in t_list2 :
    print(item)

# keywords 参数搜索

t_list = bs.find_all(id = "head")
t_list = bs.find_all(class_=True)
for item in t_list :
    print(item)

# text 参数
import re
t_list = bs.find_all(text = ["hao123","地图"])
t_list = bs.find_all(text = re.compile("\d")) # 应用正则表达式
t_list = bs.find_all("a",limit=3)
for item in t_list :
    print(item)

# css 选择器
t_list = bs.select("title") # 标签查找
t_list = bs.select("#u1")     # id查找
t_list = bs.select(".mnav")     # 类名查找
t_list = bs.select("a[class='bri']") # 通过属性查找
t_list = bs.select("head > title") # 通过子标签来查找
t_list = bs.select(".mnav ~ .bri") # 通过兄弟标签查找
for item in t_list :
    print(item)