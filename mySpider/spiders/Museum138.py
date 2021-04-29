#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/4/25 10:12
# @Author  : zqy
# @File    : Museum138.py
# @Software: PyCharm

from ..items import *
import re


class Museum138(scrapy.Spider):
    name = 'Museum138'
    allowed_domains = ['baike.baidu.com']
    start_urls = ['https://baike.baidu.com/item/%E9%9A%8F%E5%B7%9E%E5%8D%9A%E7%89%A9%E9%A6%86/5654130?fr=aladdin']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.MuseumPipeLine': 300,
        }
    }

    def parse(self, response, **kwargs):
        r = re.compile(u"\\n|\\r|\\[.*?]|\\t|\\xa0")
        item = MuseumBasicInformationItem()
        item["museumID"] = 138
        item["museumName"] = "随州博物馆"
        item["address"] = response.xpath("/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[1]/dd[5]").xpath('string(.)').extract_first()
        item["address"] = re.sub(r, '', item["address"])

        item["openingTime"] = "每天"
        item["consultationTelephone"] = "0722-3810518"
        item["consultationTelephone"] = re.sub(r, '', item["consultationTelephone"])

        item["publicityVideoLink"] = None
        item["longitude"] = "113.363078"
        item["latitude"] = "31.732426"

        item["introduction"] = response.xpath("/html/body/div[3]/div[2]/div/div[1]/div[4]").xpath('string(.)').extract_first()
        item["introduction"] = re.sub(r, '', item["introduction"])
        print(item)
        yield item