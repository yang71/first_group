#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/4/20 14:21 
# @Author  : ana
# @File    : Museum8.py
# @Software: PyCharm

from ..items import *


class Museum8(scrapy.Spider):
    name = "Museum8"
    allowed_domains = ['baike.baidu.com']
    start_urls = [
        'https://baike.baidu.com/item/%E4%B8%AD%E5%9B%BD%E4%BA%BA%E6%B0%91%E6%8A%97%E6%97%A5%E6%88%98%E4%BA%89%E7%BA%AA%E5%BF%B5%E9%A6%86/1777646?fr=aladdin']

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
        item["museumID"] = 8
        item["museumName"] = "中国人民抗日战争纪念馆"
        item["address"] = str(response.xpath(
            "/html/body/div[3]/div[2]/div/div[1]/div[8]/dl[1]/dd[6]/text()").extract_first()).replace("\n", "")
        item["openingTime"] = str(
            response.xpath("/html/body/div[3]/div[2]/div/div[1]/div[143]/text()").extract_first())[2:] + str(
            response.xpath("/html/body/div[3]/div[2]/div/div[1]/div[144]/text()").extract_first())[2:]
        item["consultationTelephone"] = "预约电话:010-63777088,010-63777188"
        item["publicityVideoLink"] = None
        item["longitude"] = "116.232474"
        item["latitude"] = "39.857753"
        item["introduction"] = str(
            response.xpath("/html/body/div[3]/div[2]/div/div[1]/div[4]/div[2]/text()[1]").extract_first())[:-2]
        print(item)
        yield item
