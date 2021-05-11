#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/4/19 16:38 
# @Author  : ana
# @File    : Museum4.py
# @Software: PyCharm

from ..items import *


class Museum4(scrapy.Spider):
    name = "Museum4"
    allowed_domains = ['casc-spacemuseum.com']
    start_urls = ['http://www.casc-spacemuseum.com/']

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
        item["museumID"] = 4
        item["museumName"] = "中国航天博物馆"
        item["address"] = response.xpath("//*[@id='service']/div[1]/div[2]/p[1]/span/text()[1]").extract_first()

        item["openingTime"] = response.xpath("/html/body/div[2]/ul[1]/li[3]/span/text()").extract_first()
        item["consultationTelephone"] = response.xpath(
            "//*[@id='service']/div[1]/div[2]/p[1]/span/text()[2]").extract_first().replace("电话：", "")
        item["publicityVideoLink"] = None
        item["longitude"] = "116.256319"
        item["latitude"] = "40.074645"
        item["openingTime"] = "8:30-17:30（周一闭馆，法定节假日除外）"
        url = 'http://www.casc-spacemuseum.com/about.aspx?id=1'
        yield scrapy.Request(url, callback=self.parseAnotherPage, meta={"item": item})

    # 切换页面
    def parseAnotherPage(self, response):
        item = response.meta["item"]
        item["introduction"] = response.xpath("//*[@id='right']/div[2]/p[5]").xpath('string(.)').extract_first()
        print(item)
        yield item
