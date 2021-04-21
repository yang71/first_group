#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/4/21 10:42 
# @Author  : ana
# @File    : Museum19.py
# @Software: PyCharm

from ..items import *


class Museum19(scrapy.Spider):
    name = "Museum19"
    allowed_domains = ['baike.baidu.com']
    start_urls = ['https://baike.baidu.com/item/%E5%A4%A9%E6%B4%A5%E8%87%AA%E7%84%B6%E5%8D%9A%E7%89%A9%E9%A6%86']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.MuseumPipeLine': 300,
        }
    }

    def parse(self, response, **kwargs):
        item = MuseumBasicInformationItem()
        item["museumID"] = 19
        item["museumName"] = str(response.xpath("/html/body/div[3]/div[2]/div/div[1]/div[8]/dl[1]/dd[1]").xpath(
            'string(.)').extract_first()).replace("\n", "")
        item["address"] = str(response.xpath(
            "/html/body/div[3]/div[2]/div/div[1]/div[8]/dl[2]/dd[2]").xpath('string(.)').extract_first()).replace("\n",
                                                                                                                  "")
        item["openingTime"] = str(response.xpath(
            "/html/body/div[3]/div[2]/div/div[1]/div[8]/dl[2]/dd[1]").xpath('string(.)').extract_first()).replace("\n",
                                                                                                                  "")
        item["consultationTelephone"] = "02283881997"
        item["publicityVideoLink"] = None
        item["longitude"] = "117.208093"
        item["latitude"] = "39.091103"
        item["introduction"] = str(response.xpath("/html/body/div[3]/div[2]/div/div[1]/div[4]").xpath(
            'string(.)').extract_first()).replace(" ", "").split("[1]")[0].replace("\n", "")
        print(item)
        yield item
