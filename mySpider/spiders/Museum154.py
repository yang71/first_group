#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/4/25 10:12
# @Author  : zqy
# @File    : Museum154.py
# @Software: PyCharm

from ..items import *
import re


class Museum154(scrapy.Spider):
    name = 'Museum154'
    allowed_domains = ['baike.baidu.com']
    start_urls = ['https://baike.baidu.com/item/%E5%B9%BF%E4%B8%9C%E6%B5%B7%E4%B8%8A%E4%B8%9D%E7%BB%B8%E4%B9%8B%E8%B7%AF%E5%8D%9A%E7%89%A9%E9%A6%86/6021987?fr=aladdin']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.MuseumPipeLine': 300,
        }
    }

    def parse(self, response, **kwargs):
        r = re.compile(u"\\n|\\r|\\[.*?]|\\t|\\xa0")
        item = MuseumBasicInformationItem()
        item["museumID"] = 154
        item["museumName"] = "广东海上丝绸之路博物馆"
        item["address"] = response.xpath("/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[2]/dd[2]").xpath('string(.)').extract_first()
        item["address"] = re.sub(r, '', item["address"])

        item["openingTime"] = response.xpath("/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[1]/dd[5]").xpath('string(.)').extract_first()
        item["openingTime"] = re.sub(r, '', item["openingTime"])

        item["consultationTelephone"] = "0662-3681111"
        item["consultationTelephone"] = re.sub(r, '', item["consultationTelephone"])

        item["publicityVideoLink"] = None
        item["longitude"] = "111.880444"
        item["latitude"] = "21.578157"

        item["introduction"] = response.xpath("/html/body/div[3]/div[2]/div/div[1]/div[4]").xpath('string(.)').extract_first()
        item["introduction"] = re.sub(r, '', item["introduction"])
        print(item)
        yield item