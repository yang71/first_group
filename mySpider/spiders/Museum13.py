#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/4/20 18:40 
# @Author  : ana
# @File    : Museum13.py
# @Software: PyCharm

from ..items import *


class Museum13(scrapy.Spider):
    name = "Museum13"
    allowed_domains = ['baike.baidu.com']
    start_urls = ['https://baike.baidu.com/item/%E6%81%AD%E7%8E%8B%E5%BA%9C%E5%8D%9A%E7%89%A9%E9%A6%86']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.MuseumPipeLine': 300,
        }
    }

    def parse(self, response, **kwargs):
        item = MuseumBasicInformationItem()
        item["museumID"] = 13
        item["museumName"] = str(response.xpath(
            "/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[1]/dd[1]/text()").extract_first()).replace("\n", "")
        item["address"] = str(response.xpath(
            "/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[1]/dd[3]/text()").extract_first()).replace("\n", "")
        item["openingTime"] = str(response.xpath(
            "/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[2]/dd[3]/text()").extract_first()).replace("\n", "")
        item["consultationTelephone"] = "联系电话：010-83288149"
        item["publicityVideoLink"] = None
        item["longitude"] = "116.392599"
        item["latitude"] = "39.943381"
        item["introduction"] = str(response.xpath("/html/body/div[3]/div[2]/div/div[1]/div[4]/div[2]").xpath(
            "string(.)").extract_first()).split("\n")[0]

        print(item)
        yield item
