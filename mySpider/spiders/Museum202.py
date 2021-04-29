#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/4/25 10:12
# @Author  : zqy
# @File    : Museum202.py
# @Software: PyCharm

from ..items import *
import re


class Museum202(scrapy.Spider):
    name = 'Museum202'
    allowed_domains = ['baike.baidu.com']
    start_urls = ['https://baike.baidu.com/item/%E5%90%90%E9%B2%81%E7%95%AA%E5%8D%9A%E7%89%A9%E9%A6%86/4800605?fr=aladdin']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.MuseumPipeLine': 300,
        }
    }

    def parse(self, response, **kwargs):
        r = re.compile(u"\\n|\\r|\\[.*?]|\\t|\\xa0")
        item = MuseumBasicInformationItem()
        item["museumID"] = 202
        item["museumName"] = "吐鲁番博物馆"
        item["address"] = response.xpath("/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[2]/dd[1]").xpath('string(.)').extract_first()
        item["address"] = re.sub(r, '', item["address"])

        item["openingTime"] = response.xpath("/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[1]/dd[5]").xpath('string(.)').extract_first()
        item["openingTime"] = re.sub(r, '', item["openingTime"])

        item["consultationTelephone"] = "0995-7619644"
        item["consultationTelephone"] = re.sub(r, '', item["consultationTelephone"])

        item["publicityVideoLink"] = None
        item["longitude"] = "89.197715"
        item["latitude"] = "42.948874"

        item["introduction"] = response.xpath("/html/body/div[3]/div[2]/div/div[1]/div[4]").xpath('string(.)').extract_first()
        item["introduction"] = re.sub(r, '', item["introduction"])
        print(item)
        yield item