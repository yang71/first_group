#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/4/25 10:12
# @Author  : zqy
# @File    : Museum000.py
# @Software: PyCharm

from ..items import *
import re


class Museum113(scrapy.Spider):
    name = 'Museum113'
    allowed_domains = ['baike.baidu.com']
    start_urls = ['https://baike.baidu.com/item/%E5%B1%B1%E4%B8%9C%E5%A4%A7%E5%AD%A6%E5%8D%9A%E7%89%A9%E9%A6%86/195087?fr=aladdin']

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
        item["museumID"] = 113
        item["museumName"] = "山东大学博物馆"
        item["address"] = "山东省济南市山大南路27号山东大学中心校区知新楼A座27层"

        item["openingTime"] = "周一至周五  上午9:30-11:30；下午14:00-17:00"

        item["consultationTelephone"] = "0531-88366337"
        item["consultationTelephone"] = re.sub(r, '', item["consultationTelephone"])

        item["publicityVideoLink"] = None
        item["longitude"] = "117.066691"
        item["latitude"] = "36.682305"

        item["introduction"] = response.xpath("/html/body/div[3]/div[2]/div/div[1]/div[4]").xpath('string(.)').extract_first()
        item["introduction"] = re.sub(r, '', item["introduction"])
        print(item)
        yield item