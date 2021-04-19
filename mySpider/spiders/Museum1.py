#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/4/18 21:52 
# @Author  : ana
# @File    : Museum1.py
# @Software: PyCharm

from ..items import *


class Museum1(scrapy.Spider):
    name = "Museum1"
    allowed_domains = ['cstm.cdstm.cn']
    start_urls = ['https://cstm.cdstm.cn/']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.MuseumPipeLine': 300,
        }
    }

    def parse(self, response, **kwargs):
        item = MuseumBasicInformationItem()
        item["museumID"] = 1
        item["museumName"] = "中国科学技术馆"
        item["address"] = "北京市朝阳区北辰东路5号"
        item["openingTime"] = response.xpath(
            "/html/body/div[6]/div[1]/div[2]/div/p[1]/span[2]/em/text()").extract_first()
        item["consultationTelephone"] = str(((response.xpath(
            "/html/body/div[8]/div/div[1]/p/text()[4]").extract_first()).replace("\xa0", '')).strip())
        item["publicityVideoLink"] = None
        item["longitude"] = "116.40504"
        item["latitude"] = "40.012384"
        url = 'https://cstm.cdstm.cn/bgs/kjghk/'
        yield scrapy.Request(url, callback=self.parseAnotherPage, meta={"item": item})

    # 切换页面
    def parseAnotherPage(self, response):
        item = response.meta["item"]
        item["introduction"] = response.xpath("/html/body/div[4]/div[3]/div/div[1]/div/p[2]/text()").extract_first()
        print(item)
        yield item
