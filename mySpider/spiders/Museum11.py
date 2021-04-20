#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/4/20 18:21 
# @Author  : ana
# @File    : Museum11.py
# @Software: PyCharm

from ..items import *


class Museum11(scrapy.Spider):
    name = "Museum11"
    allowed_domains = ['baike.baidu.com']
    start_urls = [
        'https://baike.baidu.com/item/%E4%B8%AD%E5%9B%BD%E5%86%9C%E4%B8%9A%E5%8D%9A%E7%89%A9%E9%A6%86/1751870?fr=aladdin#9_2']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.MuseumPipeLine': 300,
        }
    }

    def parse(self, response, **kwargs):
        item = MuseumBasicInformationItem()
        item["museumID"] = 11
        item["museumName"] = str(response.xpath(
            "/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[1]/dd[1]/text()").extract_first()).replace("\n", "")
        item["address"] = str(response.xpath(
            "/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[2]/dd[2]/text()").extract_first()).replace("\n", "")
        item["openingTime"] = str(response.xpath(
            "/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[1]/dd[5]/text()").extract_first()).replace("\n", "")
        item["consultationTelephone"] = "展览咨询电话:010-65096688"
        item["publicityVideoLink"] = None
        item["longitude"] = "116.47137"
        item["latitude"] = "39.947016"
        item["introduction"] = str(response.xpath("/html/body/div[3]/div[2]/div/div[1]/div[11]").xpath(
            "string(.)").extract_first()).split("\n")[0]

        print(item)
        yield item
