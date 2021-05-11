#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/4/20 11:47 
# @Author  : ana
# @File    : Museum6.py
# @Software: PyCharm

from ..items import *


class Museum6(scrapy.Spider):
    name = "Museum6"
    allowed_domains = ['capitalmuseum.org.cn']
    start_urls = ['http://www.capitalmuseum.org.cn/index.htm']

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
        item["museumID"] = 6
        item["museumName"] = "首都博物馆"
        item["address"] = "北京市西城区复兴门外大街16号"
        item["openingTime"] = "09:00—17:00(16:00停止入馆，周一闭馆)"
        item["consultationTelephone"] = "010-63370491/63370492"
        item["publicityVideoLink"] = None
        item["longitude"] = "116.348822"
        item["latitude"] = "39.912174"
        item[
            "introduction"] = "首都博物馆于1953年开始筹备，1981年正式对外开放，原馆址在全国重点文物保护单位——北京孔庙。作为北京市“十五”期间重点文化建设工程，首都博物馆新馆建设项目的立项申请，于1999年得到北京市委、市政府批准，2001年经国家发改委报国务院批准实施，2001年12月正式奠基兴建。"
        print(item)
        yield item
