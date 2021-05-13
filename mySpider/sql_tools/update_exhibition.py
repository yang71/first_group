#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/5/13 16:29 
# @Author  : ana
# @File    : update_exhibition.py
# @Software: PyCharm


import pymysql
# 下述的路径可能每个人不同,我是使mySpider文件夹为源
from str_filter import *


def getConnection():
    conn = pymysql.connect(host='localhost', port=3306, user='root', password='ana', db='spider_test')
    return conn


# row[0] - collectionID
# row[1] - exhibitionName
# row[2] - exhibitionTime
# row[3] - exhibitionIntroduction
# row[4] - museumID
# row[5] - museumName
# row[6] - exhibitionImageLink

def updateAll(sql):
    conn = getConnection()
    cur = conn.cursor()
    cur.execute(sql)
    res = cur.fetchall()
    for row in res:
        print(row[5])
        # 修改exhibitionName
        exhibitionName = StrFilter.filter_2(row[1])
        # print(exhibitionName)

        # 修改exhibitionTime
        exhibitionTime = StrFilter.filter_2(row[2])
        if len(exhibitionTime) <= 4 and exhibitionTime is not "临时展览":
            exhibitionTime = "常设展览"
        exhibitionTime = exhibitionTime.replace("~", "").replace(" 结束时间：", "").replace("展览时间：", "").replace(
            "展览地点：銮驾库展品数量：81件", "").split("地址")[0]
        # print(exhibitionTime)

        # 修改exhibitionIntroduction
        exhibitionIntroduction = StrFilter.filter_2(row[3])
        if len(exhibitionIntroduction) <= 4:
            exhibitionIntroduction = "暂无介绍"
        # print(exhibitionIntroduction)

        # 修改exhibitionImageLink
        exhibitionImageLink = StrFilter.filter_2(row[6])
        if len(exhibitionImageLink) <= 6 or 'None' in exhibitionImageLink:
            exhibitionImageLink = "http://bucttalk.online/first_group/default.jpg"
        print(exhibitionImageLink)

        # 修改museumName
        museumName = StrFilter.filter_2(row[5])
        #
        # replace_sql = """replace into collection(collectionID,museumID,collectionIntroduction,collectionImageLink,collectionName,museumName) VALUES (%s,%s,%s,%s,%s,%s) """
        #
        # cur.execute(replace_sql,
        #             (
        #                 str(row[0]), str(row[1]), collectionIntroduction,
        #                 collectionImageLink, collectionName, museumName))

    conn.commit()
    cur.close()
    conn.close()


if __name__ == '__main__':
    select_sql = 'select * from exhibition'
    updateAll(select_sql)
