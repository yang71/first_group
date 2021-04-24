#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/4/20 17:50 
# @Author  : ana
# @File    : Museum10.py
# @Software: PyCharm
import re

from ..items import *
from ..str_filter import StrFilter


class Museum10(scrapy.Spider):
    name = "Museum10"
    allowed_domains = ['baike.baidu.com']
    start_urls = [
        'https://baike.baidu.com/item/%E4%B8%AD%E5%9B%BD%E5%9B%BD%E5%AE%B6%E5%8D%9A%E7%89%A9%E9%A6%86/567902?fr=aladdin']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.MuseumPipeLine': 300,
        }
    }

    def parse(self, response, **kwargs):
        item = MuseumBasicInformationItem()
        item["museumID"] = 10
        name = str(response.xpath("/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[1]/dd[1]").xpath(
            "string(.)").extract_first())
        item["museumName"] = re.sub(StrFilter.r1, "", name)
        item["address"] = "北京市中心天安门广场东侧，东长安街南侧"
        time = str(response.xpath("/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[1]/dd[4]").xpath(
            'string(.)').extract_first())
        item["openingTime"] = re.sub(StrFilter.r1, "", time)
        item["consultationTelephone"] = "参观咨询热线：010-65116400（9:00-16:00）"
        item["publicityVideoLink"] = None
        item["longitude"] = "116.408016"
        item["latitude"] = "39.91146"
        intr = str(
            response.xpath("/html/body/div[3]/div[2]/div/div[1]/div[4]/div[1]").xpath("string(.)").extract_first())
        item["introduction"] = re.sub(StrFilter.r1, "", intr).replace(" ", "").replace("\xa0", "")
        print(item)
        yield item
