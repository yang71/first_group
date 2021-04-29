#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/4/20 13:55 
# @Author  : ana
# @File    : Museum7.py
# @Software: PyCharm

from ..items import *


class Museum7(scrapy.Spider):
    name = "Museum7"
    allowed_domains = ['bmnh.org.cn']
    start_urls = ['http://www.bmnh.org.cn/']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.MuseumPipeLine': 300,
        }
    }

    def parse(self, response, **kwargs):
        item = MuseumBasicInformationItem()
        item["museumID"] = 7
        item["museumName"] = "北京自然博物馆"
        item["address"] = str(response.xpath("/html/body/div[10]/div[3]/p[2]/text()").extract_first()).split("电子")[0]
        item["openingTime"] = "开放时间为每天9:00～17:00（16:00停止入馆），周一例行闭馆（法定节假日除外）"
        item["consultationTelephone"] = \
            str(response.xpath("/html/body/div[10]/div[3]/p[2]/text()").extract_first()).split("cn ")[1]
        item["publicityVideoLink"] = None
        item["longitude"] = "116.406116"
        item["latitude"] = "39.889525"
        url = 'http://www.bmnh.org.cn/bwgjj/bwgjj/index.shtml'
        yield scrapy.Request(url, callback=self.parseAnotherPage, meta={"item": item})

    # 切换页面
    def parseAnotherPage(self, response):
        item = response.meta["item"]
        item["introduction"] = response.xpath(
            "/html/body/div[3]/div[2]/div[2]/div/p[3]/span/span/text()").extract_first()
        print(item)
        yield item
