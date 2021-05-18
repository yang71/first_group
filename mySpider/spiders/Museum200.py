#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/4/25 10:12
# @Author  : zqy
# @File    : Museum200.py
# @Software: PyCharm

from ..items import *
import re


class Museum200(scrapy.Spider):
    name = 'Museum200'
    allowed_domains = ['baike.baidu.com']
    start_urls = ['https://baike.baidu.com/item/%E4%B8%AD%E5%9B%BD%E8%97%8F%E5%8C%BB%E8%8D%AF%E6%96%87%E5%8C%96%E5%8D%9A%E7%89%A9%E9%A6%86/6076705?fr=aladdin']

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
        item["museumID"] = 200
        item["museumName"] = "中国藏医药文化博物馆"
        item["address"] = response.xpath("/html/body/div[3]/div[2]/div/div[1]/div[27]/b").xpath('string(.)').extract_first().replace('地址：' ,'')
        item["address"] = re.sub(r, '', item["address"])

        item["openingTime"] = '4月16日-10月15日，9：00-18：00；10月16日-次年4月15日，9：00-16：00.周六日不休息'
        item["openingTime"] = re.sub(r, '', item["openingTime"])

        item["consultationTelephone"] = "0971-5317881"
        item["consultationTelephone"] = re.sub(r, '', item["consultationTelephone"])

        item["publicityVideoLink"] = None
        item["longitude"] = "103.916945"
        item["latitude"] = "30.580199"

        item["introduction"] = response.xpath("/html/body/div[3]/div[2]/div/div[1]/div[4]").xpath('string(.)').extract_first()
        item["introduction"] = re.sub(r, '', item["introduction"])
        print(item)
        yield item