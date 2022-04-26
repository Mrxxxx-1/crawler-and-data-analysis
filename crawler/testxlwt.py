'''
Author: Mrx
Date: 2022-04-02 14:49:03
LastEditors: Mrx
LastEditTime: 2022-04-05 16:30:00
FilePath: \pcode\crawler\testxlwt.py
Description: 

Copyright (c) 2022 by Mrx, All Rights Reserved. 
'''

import xlwt

# 创建Workbook对象
workbook = xlwt.Workbook(encoding="utf-8")
# 创建工作表
worksheet = workbook.add_sheet('sheet1')
# (行，列，'嵌入内容')
# worksheet.write(0,0,'how you doing')
# 写入九九乘法表
for i in range(1,10) :
    for j in range(i, 10) :
        worksheet.write(j-1, i-1, '{0}*{1}={2}'.format(i, j, i*j))
workbook.save('student.xls')