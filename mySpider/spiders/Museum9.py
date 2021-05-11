#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/4/24 10:10 
# @Author  : ana
# @File    : Museum9.py
# @Software: PyCharm

from ..items import *
import re


class Museum9(scrapy.Spider):
    name = "Museum9"
    allowed_domains = ['baike.baidu.com']
    start_urls = [
        'https://baike.baidu.com/item/%E5%91%A8%E5%8F%A3%E5%BA%97%E9%81%97%E5%9D%80%E5%8D%9A%E7%89%A9%E9%A6%86/1632300?fr=aladdin']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.MuseumPipeLine': 300,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.DefaultMiddleware': 0,
        },
    }

    def parse(self, response, **kwargs):
        r = re.compile(u"\\n|\\r|\\[.*?]|\\t")
        item = MuseumBasicInformationItem()
        item["museumID"] = 9
        item["museumName"] = str(response.xpath("/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[1]/dd[1]").xpath(
            "string(.)").extract_first())
        item["museumName"] = re.sub(r, '', item["museumName"])
        item["address"] = str(response.xpath("/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[1]/dd[4]").xpath(
            "string(.)").extract_first())
        item["address"] = re.sub(r, '', item["address"])
        item["openingTime"] = response.xpath(
            "/html/body/div[3]/div[2]/div/div[1]/div[83]").xpath("string(.)").extract_first()
        item["consultationTelephone"] = "010-53230037"
        item["consultationTelephone"] = re.sub(r, '', item["consultationTelephone"])
        item["publicityVideoLink"] = None
        item["longitude"] = "115.94298"
        item["latitude"] = "39.693776"
        item["introduction"] = str(
            response.xpath("/html/body/div[3]/div[2]/div/div[1]/div[4]/div").xpath("string(.)").extract_first()).strip(
            ' ')
        print(item)
        yield item
