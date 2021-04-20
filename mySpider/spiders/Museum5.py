#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/4/20 9:54
# @Author  : ana
# @File    : Museum5.py
# @Software: PyCharm

from ..items import *


class Museum5(scrapy.Spider):
    name = "Museum5"
    allowed_domains = ['luxunmuseum.com.cn']
    start_urls = ['http://www.luxunmuseum.com.cn/']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.MuseumPipeLine': 300,
        }
    }

    def parse(self, response, **kwargs):
        item = MuseumBasicInformationItem()
        item["museumID"] = 5
        item["museumName"] = "北京鲁迅博物馆"
        item["address"] = response.xpath("/html/body/div[3]/div[5]/div[1]/p[4]/text()").extract_first()
        item["openingTime"] = response.xpath("/html/body/div[3]/div[5]/div[1]/p[1]").xpath(
            'string(.)').extract_first().replace("\t", '').replace("\n", '').strip() + " " + response.xpath(
            "/html/body/div[3]/div[5]/div[1]/p[2]").xpath('string(.)').extract_first().replace("\t", '').replace("\n",
                                                                                                                 '').strip() + " " + response.xpath(
            "/html/body/div[3]/div[5]/div[1]/p[3]").xpath(
            'string(.)').extract_first().replace("\t", '').replace("\n", '').strip()
        item["consultationTelephone"] = str(((response.xpath(
            "/html/body/div[3]/div[5]/div[3]/p[3]/span[1]/text()").extract_first()).replace("\xa0", '')).strip())
        item["publicityVideoLink"] = None
        item["longitude"] = "116.365314"
        item["latitude"] = "39.931656"
        url = 'http://www.luxunmuseum.com.cn/bowuguanjieshao/'
        yield scrapy.Request(url, callback=self.parseAnotherPage, meta={"item": item})

    # 切换页面
    def parseAnotherPage(self, response):
        item = response.meta["item"]
        item["introduction"] = response.xpath(
            "/html/body/div[3]/div[2]/div[2]/div/div[3]/text()[1]").extract_first().replace("\xa0", '').strip()
        print(item)
        yield item
