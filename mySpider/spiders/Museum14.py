#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/4/20 18:45 
# @Author  : ana
# @File    : Museum14.py
# @Software: PyCharm

from ..items import *


class Museum14(scrapy.Spider):
    name = "Museum14"
    allowed_domains = ['www.printingmuseum.cn']
    start_urls = ['http://www.printingmuseum.cn/Home/Index']

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
        item["museumID"] = 14
        item["museumName"] = "中国印刷博物馆"
        item["address"] = response.xpath("/html/body/div[8]/div[2]/div[1]/a/p[3]/text()").extract_first()
        item["openingTime"] = response.xpath(
            "/html/body/div[8]/div[2]/div[1]/a/p[1]/text()").extract_first()
        item["consultationTelephone"] = str(((response.xpath(
            "/html/body/div[11]/div/div[1]/p[3]/text()[2]").extract_first()).replace("\xa0", '')).strip())
        item["publicityVideoLink"] = None
        item["longitude"] = "116.356228"
        item["latitude"] = "39.939043"
        url = 'http://www.printingmuseum.cn/News/Details/BGJS#comehere'
        yield scrapy.Request(url, callback=self.parseAnotherPage, meta={"item": item})

    # 切换页面
    def parseAnotherPage(self, response):
        item = response.meta["item"]
        item["introduction"] = str(response.xpath("//*[@id='divContent']/p[1]/text()").extract_first()).strip(' ')

        print(item)
        yield item
