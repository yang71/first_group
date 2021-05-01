#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/4/30 15:38 
# @Author  : ana
# @File    : Collection0.py
# @Software: PyCharm
import re

from ..items import *
from ..str_filter import *


class Collection0(scrapy.Spider):
    name = "Collection0"
    allowed_domains = ['dpm.org.cn']
    start_urls = ['https://zm-digicol.dpm.org.cn/cultural/list?page=2&category=17', ]

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        }
    }

    def parse(self, response, **kwargs):
        li_list = response.xpath("/html/body/div[2]/div[4]/div[@class='table']")
        for li in li_list:
            item = CollectionItem()
            item["museumID"] = 0
            item["museumName"] = "故宫博物院"
            print(li.xpath("./div[1]/a/@href/text()").extract_first())
            url = str(li.xpath("./div[@class='table_info']/a/@href").extract_first())
            yield scrapy.Request(
                url,
                callback=self.parseAnotherPage,
                meta={"item": item}
            )

    def parseAnotherPage(self, response):
        item = response.meta["item"]
        item['collectionName'] = response.xpath(
            "/html/body/div[1]/div/div[2]/div/div[1]/div[2]/div/h2/text()").extract_first()
        item['collectionImageLink'] = response.xpath(
            "/html/body/div[2]/div[1]/div/div/img/@src").extract_first()
        item['collectionIntroduction'] = StrFilter.filter(
            str(response.xpath("/html/body/div[1]/div/div[2]/div/div[2]/div[1]/p/text()[2]/text()").extract_first()))
        print(item)
        yield item
