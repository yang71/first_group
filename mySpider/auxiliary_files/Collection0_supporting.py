#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/5/2 11:42 
# @Author  : ana
# @File    : Collection0_supporting.py
# @Software: PyCharm

urls = []
for i in range(2, 1000):
    urls.append("https://zm-digicol.dpm.org.cn/cultural/list?page=" + str(i) + "&category=17");

print(urls)
