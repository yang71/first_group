#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/4/25 10:12
# @Author  : zqy
# @File    : Museum141.py
# @Software: PyCharm

from ..items import *
import re


class Museum141(scrapy.Spider):
    name = 'Museum141'
    allowed_domains = ['baike.baidu.com']
    start_urls = ['https://baike.baidu.com/item/%E5%88%98%E5%B0%91%E5%A5%87%E6%95%85%E5%B1%85%E7%BA%AA%E5%BF%B5%E9%A6%86/12769149?fr=aladdin']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.MuseumPipeLine': 300,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.DefaultMiddleware': 0,
        },
    }

    def parse(self, response, **kwargs):
        r = re.compile(u"\\n|\\r|\\[.*?]|\\t|\\xa0")
        item = MuseumBasicInformationItem()
        item["museumID"] = 141
        item["museumName"] = "刘少奇故居纪念馆"
        item["address"] = "长沙市宁乡市幸福大道(花明楼景区)"

        item["openingTime"] = "09:00-17:00"
        item["consultationTelephone"] = "0731-87094027"
        item["consultationTelephone"] = re.sub(r, '', item["consultationTelephone"])

        item["publicityVideoLink"] = None
        item["longitude"] = "114.302243"
        item["latitude"] = "30.597028"

        item["introduction"] = response.xpath("/html/body/div[3]/div[2]/div/div[1]/div[4]").xpath('string(.)').extract_first()
        item["introduction"] = re.sub(r, '', item["introduction"])
        print(item)
        yield item