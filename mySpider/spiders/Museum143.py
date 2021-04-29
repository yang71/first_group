#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/4/25 10:12
# @Author  : zqy
# @File    : Museum143.py
# @Software: PyCharm

from ..items import *
import re


class Museum143(scrapy.Spider):
    name = 'Museum143'
    allowed_domains = ['baike.baidu.com']
    start_urls = ['https://baike.baidu.com/item/%E9%95%BF%E6%B2%99%E5%B8%82%E5%8D%9A%E7%89%A9%E9%A6%86/8711557?fr=aladdin']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.MuseumPipeLine': 300,
        }
    }

    def parse(self, response, **kwargs):
        r = re.compile(u"\\n|\\r|\\[.*?]|\\t|\\xa0")
        item = MuseumBasicInformationItem()
        item["museumID"] = 143
        item["museumName"] = "长沙市博物馆"
        item["address"] = response.xpath("/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[2]/dd[2]").xpath('string(.)').extract_first()
        item["address"] = re.sub(r, '', item["address"])

        item["openingTime"] = response.xpath("/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[1]/dd[5]").xpath('string(.)').extract_first()
        item["openingTime"] = re.sub(r, '', item["openingTime"])

        item["consultationTelephone"] = "0731-82892360"
        item["consultationTelephone"] = re.sub(r, '', item["consultationTelephone"])

        item["publicityVideoLink"] = None
        item["longitude"] = "112.945473"
        item["latitude"] = "28.234889"

        item["introduction"] = response.xpath("/html/body/div[3]/div[2]/div/div[1]/div[4]").xpath('string(.)').extract_first()
        item["introduction"] = re.sub(r, '', item["introduction"])
        print(item)
        yield item