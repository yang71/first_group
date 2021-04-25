#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/4/25 10:12
# @Author  : zqy
# @File    : Museum183.py
# @Software: PyCharm

from ..items import *
import re


class Museum183(scrapy.Spider):
    name = 'Museum183'
    allowed_domains = ['baike.baidu.com']
    start_urls = ['https://baike.baidu.com/item/%E8%A5%BF%E8%97%8F%E5%8D%9A%E7%89%A9%E9%A6%86/1627112?fr=aladdin']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.MuseumPipeLine': 300,
        }
    }

    def parse(self, response, **kwargs):
        r = re.compile(u"\\n|\\r|\\[.*?]|\\t|\\xa0")
        item = MuseumBasicInformationItem()
        item["museumID"] = 183
        item["museumName"] = "西藏博物馆"
        item["address"] = response.xpath("/html/body/div[3]/div[2]/div/div[1]/div[8]/dl[2]/dd[1]").xpath('string(.)').extract_first()
        item["address"] = re.sub(r, '', item["address"])

        item["openingTime"] = response.xpath("/html/body/div[3]/div[2]/div/div[1]/div[62]").xpath('string(.)').extract_first()
        item["openingTime"] += response.xpath("/html/body/div[3]/div[2]/div/div[1]/div[63]").xpath(
            'string(.)').extract_first()
        item["openingTime"] = re.sub(r, '', item["openingTime"])

        item["consultationTelephone"] = "0891-6835244 0891-6812210"
        item["consultationTelephone"] = re.sub(r, '', item["consultationTelephone"])

        item["publicityVideoLink"] = None
        item["longitude"] = "91.104815"
        item["latitude"] = "29.654906"

        item["introduction"] = response.xpath("/html/body/div[3]/div[2]/div/div[1]/div[4]").xpath('string(.)').extract_first()
        item["introduction"] = re.sub(r, '', item["introduction"])
        print(item)
        yield item