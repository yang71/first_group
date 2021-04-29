#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/4/19 12:42 
# @Author  : ana
# @File    : Museum3.py
# @Software: PyCharm

from ..items import *


class Museum3(scrapy.Spider):
    name = "Museum3"
    allowed_domains = ['jb.mil.cn']
    start_urls = ['http://www.jb.mil.cn/']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.MuseumPipeLine': 300,
        }
    }

    def parse(self, response, **kwargs):
        item = MuseumBasicInformationItem()
        item["museumID"] = 3
        item["museumName"] = "中国人民革命军事博物馆"
        item["address"] = "北京市海淀区复兴路9号"

        item["openingTime"] = response.xpath("/html/body/div[2]/ul[1]/li[3]/span/text()").extract_first()
        item["consultationTelephone"] = "010-66866244"
        item["publicityVideoLink"] = None
        item["longitude"] = "116.340208"
        item["latitude"] = "39.962924"
        url = 'http://www.jb.mil.cn/jbgk/jbjj/'
        yield scrapy.Request(url, callback=self.parseAnotherPage, meta={"item": item})

    # 切换页面
    def parseAnotherPage(self, response):
        item = response.meta["item"]
        item["introduction"] = response.xpath("/html/body/div[4]/p[1]/text()").extract_first()
        print(item)
        yield item
