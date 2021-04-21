#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/4/21 10:33 
# @Author  : ana
# @File    : Museum18.py
# @Software: PyCharm

from ..items import *


class Museum18(scrapy.Spider):
    name = "Museum18"
    allowed_domains = ['www.tjbwg.com']
    start_urls = ['https://www.tjbwg.com/cn/Index.aspx']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.MuseumPipeLine': 300,
        }
    }

    def parse(self, response, **kwargs):
        item = MuseumBasicInformationItem()
        item["museumID"] = 18
        item["museumName"] = "天津博物馆"
        item["address"] = response.xpath("/html/body/div/div[6]/div/div[3]/div[3]/text()").extract_first()
        item["openingTime"] = str(response.xpath(
            "/html/body/div/div[3]/div[1]/div/div[2]/div[3]/div[1]").xpath("string(.)").extract_first()).replace(
            "\t", "").replace("\n", "").replace("\r", "").replace(" ", "")
        item["consultationTelephone"] = str(((response.xpath(
            "/html/body/div/div[6]/div/div[3]/div[1]/text()").extract_first()).replace("\xa0", '')).strip())
        item["publicityVideoLink"] = None
        item["longitude"] = "117.218282"
        item["latitude"] = "39.091039"
        url = 'https://www.tjbwg.com/cn/about.aspx?TypeId=10921'
        yield scrapy.Request(url, callback=self.parseAnotherPage, meta={"item": item})

    # 切换页面
    def parseAnotherPage(self, response):
        item = response.meta["item"]
        item["introduction"] = str(
            response.xpath("/html/body/div/div[3]/div/div/div[2]/div[2]/div/div[1]/p/text()").extract_first()).replace(
            "\t", "").replace("\n", "").replace("\r", "").strip(' ')
        print(item)
        yield item
