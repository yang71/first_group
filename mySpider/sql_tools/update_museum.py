#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/5/6 17:46 
# @Author  : ana
# @File    : update_museum.py
# @Software: PyCharm

import pymysql
# 下述的路径可能每个人不同,我是使mySpider文件夹为源
from str_filter import *


def getConnection():
    conn = pymysql.connect(host='localhost', port=3306, user='root', password='ana', db='spider_test')
    return conn


# row[0] - museumID
# row[1] - museumName
# row[2] - openingTime
# row[3] - address
# row[4] - consultationTelephone
# row[5] - introduction
# row[6] - longitude
# row[7] - latitude
# row[8] - publicVideoLink

def updateAll(sql):
    conn = getConnection()
    cur = conn.cursor()
    cur.execute(sql)
    res = cur.fetchall()
    for row in res:

        # 修改openingTime
        openingTime = StrFilter.filter_2(row[2])
        if len(openingTime) <= 4:
            openingTime = None
        # print(openingTime)

        # 修改address
        address = StrFilter.filter_2(row[3]).replace("地址：", "")
        if len(address) <= 4:
            address = None
        # print(address)

        # 修改consultationTelephone
        conTelephone = StrFilter.filter_Telephone(row[4])
        if len(conTelephone) <= 4:
            conTelephone = None
        # print(conTelephone)

        # 修改introduction
        introduction = StrFilter.filter_2(row[5])
        if len(introduction) <= 4:
            introduction = None
        # print(introduction)

        # 修改videoLink
        videoLink = str(row[8])
        if len(videoLink) <= 4:
            videoLink = None
        # print(videoLink)

        # replace_sql = """replace into museumbasicinformation(museumID,museumName,openingTime,address,
        # consultationTelephone,introduction,longitude,latitude,publicityVideoLink) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,
        # %s) """
        #
        # cur.execute(replace_sql, (str(row[0]), str(row[1]), openingTime, address, conTelephone, introduction,
        #                           str(row[6]), str(row[7]), videoLink))

    conn.commit()
    cur.close()
    conn.close()


if __name__ == '__main__':
    select_sql = 'select * from museumbasicinformation'
    updateAll(select_sql)
