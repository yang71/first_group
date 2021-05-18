#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/4/25 10:12
# @Author  : zqy
# @File    : Museum182.py
# @Software: PyCharm

from ..items import *
import re


class Museum182(scrapy.Spider):
    name = 'Museum182'
    allowed_domains = ['baike.baidu.com']
    start_urls = ['https://baike.baidu.com/item/%E9%87%8D%E5%BA%86%E5%A4%A7%E8%B6%B3%E7%9F%B3%E5%88%BB%E8%89%BA%E6%9C%AF%E5%8D%9A%E7%89%A9%E9%A6%86/4222631?fr=aladdin']

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
        item["museumID"] = 182
        item["museumName"] = "大足石刻博物馆"
        item["address"] = response.xpath("/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[2]/dd[1]").xpath('string(.)').extract_first()
        item["address"] = re.sub(r, '', item["address"])

        item["openingTime"] = "周二至周日 每日09:00—17:00 周一闭馆（法定节假日除外）"
        item["openingTime"] = re.sub(r, '', item["openingTime"])

        item["consultationTelephone"] = "023-43760250"
        item["consultationTelephone"] = re.sub(r, '', item["consultationTelephone"])

        item["publicityVideoLink"] = None
        item["longitude"] = "105.759517"
        item["latitude"] = "29.585463"

        item["introduction"] = response.xpath("/html/body/div[3]/div[2]/div/div[1]/div[4]").xpath('string(.)').extract_first()
        item["introduction"] = re.sub(r, '', item["introduction"])
        print(item)
        yield item