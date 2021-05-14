#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/5/9 14:34 
# @Author  : ana
# @File    : update_collection.py
# @Software: PyCharm

import pymysql
# 下述的路径可能每个人不同,我是使mySpider文件夹为源
from str_filter import *


def getConnection():
    conn = pymysql.connect(host='localhost', port=3306, user='root', password='ana', db='spider_test')
    return conn


# row[0] - collectionID
# row[1] - museumID
# row[2] - collectionIntroduction
# row[3] - collectionImageLink
# row[4] - collectionName
# row[5] - museumName

def updateAll(sql):
    conn = getConnection()
    cur = conn.cursor()
    cur.execute(sql)
    res = cur.fetchall()
    for row in res:

        # 修改collectionIntroduction
        collectionIntroduction = StrFilter.filter_2(row[2])
        if len(collectionIntroduction) <= 8:
            collectionIntroduction = "暂无简介"
        if collectionIntroduction[0] == ',':
            collectionIntroduction = collectionIntroduction[1:]
        collectionIntroduction = collectionIntroduction.replace("返回上页故宫博物院版权所有，查看详情。", "").replace(
            "相关推荐展子虔游春图卷王希孟千里江山图卷张择端清明上河图卷分享", "").split("发布日期")[0].replace(
            "'收','藏','相关推荐','展子虔游春图卷王希孟千里江山图卷张择端清明上河图卷','分享','", "").replace("','", "")
        # print(collectionIntroduction)

        # 修改collectionImageLink
        collectionImageLink = StrFilter.filter_2(row[3])
        if len(collectionImageLink) <= 8 or 'None' in collectionImageLink:
            collectionImageLink = "http://bucttalk.online/first_group/default.jpg"
        # print(collectionImageLink)

        # 修改collectionName
        collectionName = StrFilter.filter_2(row[4]).strip("'")
        print(collectionName)

        # 修改museumName
        museumName = StrFilter.filter_2(row[5])

        replace_sql = """replace into collection(collectionID,museumID,collectionIntroduction,collectionImageLink,collectionName,museumName) VALUES (%s,%s,%s,%s,%s,%s) """

        cur.execute(replace_sql,
                    (
                        str(row[0]), str(row[1]), collectionIntroduction,
                        collectionImageLink, collectionName, museumName))

    conn.commit()
    cur.close()
    conn.close()


if __name__ == '__main__':
    select_sql = 'select * from collection'
    updateAll(select_sql)
