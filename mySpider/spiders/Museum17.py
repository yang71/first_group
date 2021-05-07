#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/4/21 10:22 
# @Author  : ana
# @File    : Museum17.py
# @Software: PyCharm

from ..items import *


class Museum17(scrapy.Spider):
    name = "Museum17"
    allowed_domains = ['baike.baidu.com']
    start_urls = [
        'https://baike.baidu.com/item/%E6%B8%85%E5%8D%8E%E5%A4%A7%E5%AD%A6%E8%89%BA%E6%9C%AF%E5%8D%9A%E7%89%A9%E9%A6%86']

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
        item["museumID"] = 17
        item["museumName"] = str(response.xpath("/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[1]/dd[1]").xpath(
            'string(.)').extract_first()).replace("\n", "")
        item["address"] = str(response.xpath(
            "/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[1]/dd[3]").xpath('string(.)').extract_first()).replace("\n",
                                                                                                                  "")
        item["openingTime"] = str(response.xpath(
            "/html/body/div[3]/div[2]/div/div[1]/div[4]/div[2]").xpath('string(.)').extract_first()).replace("\n",
                                                                                                             "")
        item["consultationTelephone"] = "010-62781012"
        item["publicityVideoLink"] = None
        item["longitude"] = "116.342213"
        item["latitude"] = "40.00764"
        item["introduction"] = str(response.xpath("/html/body/div[3]/div[2]/div/div[1]/div[4]/div[1]").xpath(
            'string(.)').extract_first()).strip(' ').split("\n")[0].replace(" ", "").split("[2]")[0]
        print(item)
        yield item
