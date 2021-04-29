#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/4/20 18:32 
# @Author  : ana
# @File    : Museum12.py
# @Software: PyCharm

from ..items import *


class Museum12(scrapy.Spider):
    name = "Museum12"
    allowed_domains = ['baike.baidu.com']
    start_urls = ['https://baike.baidu.com/item/%E5%8C%97%E4%BA%AC%E5%A4%A9%E6%96%87%E9%A6%86/1632709?fr=aladdin']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.MuseumPipeLine': 300,
        }
    }

    def parse(self, response, **kwargs):
        item = MuseumBasicInformationItem()
        item["museumID"] = 12
        item["museumName"] = str(response.xpath(
            "/html/body/div[3]/div[2]/div/div[1]/div[8]/dl[1]/dd[1]/text()").extract_first()).replace("\n", "")
        item["address"] = str(response.xpath(
            "/html/body/div[3]/div[2]/div/div[1]/div[8]/dl[2]/dd[2]/text()").extract_first()).replace("\n", "")
        item["openingTime"] = str(response.xpath(
            "/html/body/div[3]/div[2]/div/div[1]/div[8]/dl[1]/dd[5]/text()").extract_first()).replace("\n", "")
        item["consultationTelephone"] = "电话：010-68312517"
        item["publicityVideoLink"] = None
        item["longitude"] = "116.343208"
        item["latitude"] = "39.943273"
        item["introduction"] = str(response.xpath("/html/body/div[3]/div[2]/div/div[1]/div[4]/div[1]").xpath(
            "string(.)").extract_first()).split("\n")[0]

        print(item)
        yield item
