#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/4/25 10:12
# @Author  : zqy
# @File    : Museum158.py
# @Software: PyCharm

from ..items import *
import re


class Museum158(scrapy.Spider):
    name = 'Museum158'
    allowed_domains = ['baike.baidu.com']
    start_urls = ['https://baike.baidu.com/item/%E6%B5%B7%E5%8D%97%E7%9C%81%E5%8D%9A%E7%89%A9%E9%A6%86/4169415?fr=aladdin']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.MuseumPipeLine': 300,
        }
    }

    def parse(self, response, **kwargs):
        r = re.compile(u"\\n|\\r|\\[.*?]|\\t|\\xa0")
        item = MuseumBasicInformationItem()
        item["museumID"] = 158
        item["museumName"] = "海南省博物馆"
        item["address"] = response.xpath("/html/body/div[3]/div[2]/div/div[1]/div[8]/dl[2]/dd[2]").xpath('string(.)').extract_first()
        item["address"] = re.sub(r, '', item["address"])

        item["openingTime"] = response.xpath("/html/body/div[3]/div[2]/div/div[1]/div[8]/dl[2]/dd[4]").xpath('string(.)').extract_first()
        item["openingTime"] = re.sub(r, '', item["openingTime"])

        item["consultationTelephone"] = "0898-65238880"
        item["consultationTelephone"] = re.sub(r, '', item["consultationTelephone"])

        item["publicityVideoLink"] = None
        item["longitude"] = "109.587456"
        item["latitude"] = "19.527146"

        item["introduction"] = response.xpath("/html/body/div[3]/div[2]/div/div[1]/div[4]").xpath('string(.)').extract_first()
        item["introduction"] = re.sub(r, '', item["introduction"])
        print(item)
        yield item