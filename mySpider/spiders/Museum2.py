#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/4/19 12:00 
# @Author  : ana
# @File    : Museum2.py
# @Software: PyCharm

from ..items import *


class Museum2(scrapy.Spider):
    name = "Museum2"
    allowed_domains = ['gmc.org.cn']
    start_urls = ['http://www.gmc.org.cn/']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.MuseumPipeLine': 300,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.DefaultMiddleware': 0,
        },
    }

    def parse(self, response, **kwargs):
        item = MuseumBasicInformationItem()
        item["museumID"] = 2
        item["museumName"] = "中国地质博物馆"
        item["address"] = "北京市西城区西四羊肉胡同15号"
        entryTime = response.xpath(
            "/html/body/div[4]/div[3]/div/div/div[1]/div[1]/div[3]/div[1]/div[1]/text()").extract_first()
        stopEntryTime = response.xpath(
            "/html/body/div[4]/div[3]/div/div/div[1]/div[1]/div[3]/div[2]/div[1]/text()").extract_first()
        closeTime = response.xpath(
            "/html/body/div[4]/div[3]/div/div/div[1]/div[1]/div[3]/div[3]/div[1]/text()").extract_first()
        item["openingTime"] = "开放进馆时间：" + str(entryTime) + " 停止入馆时间：" + str(stopEntryTime) + " 闭馆时间：" + str(closeTime)
        item["consultationTelephone"] = (response.xpath(
            "/html/body/div[4]/div[3]/div/div/div[1]/div[2]/a/div[4]/span/text()").extract_first()).replace("\n", "")
        item["introduction"] = (response.xpath("//meta[@name='description']/@content").extract_first()) \
            .replace("\n", "").replace("\r", "")
        item["publicityVideoLink"] = "http://www.gmc.org.cn/Uploads/Picture/2020/12/31/u5fed93d60dff3.mp4"
        item["longitude"] = "116.378653"
        item["latitude"] = "39.929518"
        print(item)
        yield item
