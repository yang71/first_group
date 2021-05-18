#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/4/25 10:12
# @Author  : zqy
# @File    : Museum170.py
# @Software: PyCharm

from ..items import *
import re


class Museum170(scrapy.Spider):
    name = 'Museum170'
    allowed_domains = ['baike.baidu.com']
    start_urls = ['https://baike.baidu.com/item/5%C2%B712%E6%B1%B6%E5%B7%9D%E7%89%B9%E5%A4%A7%E5%9C%B0%E9%9C%87%E7%BA%AA%E5%BF%B5%E9%A6%86/15421377?fr=aladdin']

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
        item["museumID"] = 170
        item["museumName"] = "5·12汶川特大地震纪念馆"
        item["address"] = response.xpath("/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[1]/dd[3]").xpath('string(.)').extract_first()
        item["address"] = re.sub(r, '', item["address"])

        item["openingTime"] = response.xpath("/html/body/div[3]/div[2]/div/div[1]/div[28]").xpath('string(.)').extract_first()
        item["openingTime"] += response.xpath("/html/body/div[3]/div[2]/div/div[1]/div[29]").xpath(
            'string(.)').extract_first()
        item["openingTime"] += response.xpath("/html/body/div[3]/div[2]/div/div[1]/div[30]").xpath(
            'string(.)').extract_first()
        item["openingTime"] += response.xpath("/html/body/div[3]/div[2]/div/div[1]/div[31]").xpath(
            'string(.)').extract_first()
        item["openingTime"] = re.sub(r, '', item["openingTime"])

        item["consultationTelephone"] = "0816-6191016"
        item["consultationTelephone"] = re.sub(r, '', item["consultationTelephone"])

        item["publicityVideoLink"] = None
        item["longitude"] = "103.492751"
        item["latitude"] = "31.060144"

        item["introduction"] = response.xpath("/html/body/div[3]/div[2]/div/div[1]/div[4]").xpath('string(.)').extract_first()
        item["introduction"] = re.sub(r, '', item["introduction"])
        print(item)
        yield item