#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/4/20 19:52 
# @Author  : ana
# @File    : Museum16.py
# @Software: PyCharm

from ..items import *


class Museum16(scrapy.Spider):
    name = "Museum16"
    allowed_domains = ['baike.baidu.com']
    start_urls = [
        'https://baike.baidu.com/item/%E5%8C%97%E4%BA%AC%E6%B1%BD%E8%BD%A6%E5%8D%9A%E7%89%A9%E9%A6%86/3169875?fr=aladdin']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.MuseumPipeLine': 300,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.DefaultMiddleware': 0,
        },
    }

    def parse(self, response, **kwargs):
        item = MuseumBasicInformationItem()
        item["museumID"] = 16
        item["museumName"] = str(response.xpath("/html/body/div[3]/div[2]/div/div[1]/div[8]/dl[1]/dd[1]").xpath(
            'string(.)').extract_first()).replace("\n", "")
        item["address"] = str(response.xpath(
            "/html/body/div[3]/div[2]/div/div[1]/div[8]/dl[1]/dd[3]").xpath('string(.)').extract_first()).replace("\n",
                                                                                                                  "")
        item["openingTime"] = str(response.xpath(
            "/html/body/div[3]/div[2]/div/div[1]/div[8]/dl[2]/dd[3]").xpath('string(.)').extract_first()).replace("\n",
                                                                                                                  "")
        item["consultationTelephone"] = "010-63756666"
        item["publicityVideoLink"] = None
        item["longitude"] = "116.308469"
        item["latitude"] = "39.834959"
        item["introduction"] = str(response.xpath("/html/body/div[3]/div[2]/div/div[1]/div[5]/div[1]").xpath(
            'string(.)').extract_first()).strip(' ').split("\n")[0].replace(" ", "")
        print(item)
        yield item
