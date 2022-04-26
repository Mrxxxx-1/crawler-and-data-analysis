'''
Author: Mrx
Date: 2022-03-28 16:30:25
LastEditors: Mrx
LastEditTime: 2022-03-28 16:47:02
FilePath: \pcode\crawler\testre.py
Description: 

Copyright (c) 2022 by Mrx, All Rights Reserved. 
'''

import re

# 创建模式对象
pat = re.compile("AA")
result = pat.search("AAVVVDDDFSLJA")
print(result)

# 没有模式对象
m = re.findall("[a-z]","as34dafdjfa2133lfas")
print(m)

# sub ("被替换对象"，"替换对象"，"作用字符串")
print(re.sub("a","A","ajfaldjla"))