#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/4/24 10:58 
# @Author  : ana
# @File    : str_filter.py
# @Software: PyCharm

import re
from urllib.parse import urlparse


class StrFilter:
    # 过滤\n,\r,\t,[xxxx]
    r1 = re.compile(u"\\n|\\r|\\[.*?]|\\t")

    # 过滤中文
    r2 = re.compile(r"[\u4e00-\u9fa5]|\\(.*?)|（.*?）")

    @staticmethod
    def filter(src):
        res1 = re.sub(StrFilter.r1, "", str(src))
        res2 = str(''.join(res1.split()))
        res3 = res2.replace(" ", "")
        return res3

    @staticmethod
    def filter_2(src):
        return StrFilter.filter(src).replace('[', '').replace(']', '')

    # 获取域名，用于相对url拼接为完整url
    @staticmethod
    def getDoamin(response):
        parsed_uri = urlparse(response.url)
        domain = '{uri.scheme}://{uri.netloc}'.format(uri=parsed_uri)
        return domain

    # Museum表consultationTelephone
    @staticmethod
    def filter_Telephone(src):
        res = re.sub(StrFilter.r2, "", str(src)).replace('：', '').replace(' ', '')
        if len(res[0]) >= 1 and res[0] == ':':
            return res[1:]
        return res
