#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/4/20 11:47 
# @Author  : ana
# @File    : Museum6.py
# @Software: PyCharm

from ..items import *


class Museum6(scrapy.Spider):
    name = "Museum6"
    allowed_domains = ['capitalmuseum.org.cn']
    start_urls = ['http://www.capitalmuseum.org.cn/index.htm']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.MuseumPipeLine': 300,
        }
    }

    def parse(self, response, **kwargs):
        item = MuseumBasicInformationItem()
        item["museumID"] = 6
        item["museumName"] = "首都博物馆"
        print(response.xpath("/html/body/table/tbody/tr[1]/td[1]/table/tbody/tr/td/text()").xpath('string(.)').extract_first())
        informationList = str(
            response.xpath("/html/body/table/tbody/tr[1]/td[1]/table/tbody/tr/td/text()").extract_first()).split("|", 3)
        print(len(informationList))
        item["address"] = informationList[3]
        item["openingTime"] = informationList[0]
        item["consultationTelephone"] = informationList[1]
        item["publicityVideoLink"] = None
        item["longitude"] = "116.348822"
        item["latitude"] = "39.912174"
        url = 'http://www.capitalmuseum.org.cn/zjsb/sbjj.htm'
        yield scrapy.Request(url, callback=self.parseAnotherPage, meta={"item": item})

    # 切换页面
    def parseAnotherPage(self, response):
        item = response.meta["item"]
        item["introduction"] = response.xpath(
            "//*[@id='__01']/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr[2]/td/table/tbody/tr[2]/td/span/p[1]/text()[1]").extract_first()
        print(item)
        yield item
