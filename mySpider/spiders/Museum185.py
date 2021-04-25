#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/4/25 10:12
# @Author  : zqy
# @File    : Museum185.py
# @Software: PyCharm

from ..items import *
import re


class Museum185(scrapy.Spider):
    name = 'Museum185'
    allowed_domains = ['baike.baidu.com']
    start_urls = ['https://baike.baidu.com/item/%E7%A7%A6%E5%A7%8B%E7%9A%87%E5%85%B5%E9%A9%AC%E4%BF%91%E5%8D%9A%E7%89%A9%E9%A6%86/1509704?fr=aladdin']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.MuseumPipeLine': 300,
        }
    }

    def parse(self, response, **kwargs):
        r = re.compile(u"\\n|\\r|\\[.*?]|\\t|\\xa0")
        item = MuseumBasicInformationItem()
        item["museumID"] = 185
        item["museumName"] = "秦始皇兵马俑博物馆"
        item["address"] = response.xpath("/html/body/div[3]/div[4]/div/div[1]/div[1]/div[2]/dl[1]/dd[4]").xpath('string(.)').extract_first()
        item["address"] = re.sub(r, '', item["address"])

        item["openingTime"] = response.xpath("/html/body/div[3]/div[4]/div/div[1]/div[1]/div[2]/dl[1]/dd[6]").xpath('string(.)').extract_first()
        item["openingTime"] = re.sub(r, '', item["openingTime"])

        item["consultationTelephone"] = "029-81399174"
        item["consultationTelephone"] = re.sub(r, '', item["consultationTelephone"])

        item["publicityVideoLink"] = None
        item["longitude"] = "109.2851"
        item["latitude"] = "34.389417"

        item["introduction"] = response.xpath("/html/body/div[3]/div[2]/div/div[1]/div[1]/div[3]").xpath('string(.)').extract_first()
        item["introduction"] = re.sub(r, '', item["introduction"])
        print(item)
        yield item