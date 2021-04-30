#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/4/24 10:58 
# @Author  : ana
# @File    : str_filter.py
# @Software: PyCharm

import re


class StrFilter:
    # 过滤\n,\r,\t,[xxxx]
    r1 = re.compile(u"\\n|\\r|\\[.*?]|\\t")

    @staticmethod
    def filter(src):
        res1 = re.sub(StrFilter.r1, "", str(src))
        res2 = str(''.join(res1).split())
        res3 = res2.replace(" ", "")
        return res3
