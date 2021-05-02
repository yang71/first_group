#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/5/1 20:33 
# @Author  : ana
# @File    : Collection40.py
# @Software: PyCharm

from ..items import *
from ..str_filter import StrFilter


class Collection40(scrapy.Spider):
    name = "Collection40"
    allowed_domains = ['baike.baidu.com']
    start_urls = [
        'https://baike.baidu.com/item/%E5%90%89%E6%9E%97%E7%9C%81%E8%87%AA%E7%84%B6%E5%8D%9A%E7%89%A9%E9%A6%86/7701684?fr=aladdin']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        }
    }

    def parse(self, response, **kwargs):
        item = CollectionItem()
        item["museumID"] = 40
        li_list = response.xpath("//div[@class='content']//table")
        print(len(li_list))
        for li in li_list:
            sub_list = li.xpath(".//tr")
            for sli in sub_list:
                item["collectionImageLink"] = 'https://baike.baidu.com' + str(sli.xpath(
                    "./td[2]/div/div/a/@href").extract_first()).strip()
                item["collectionName"] = str(sli.xpath(
                    "./td[1]/div/b/text()").extract_first())
                item["collectionIntroduction"] = StrFilter.filter(sli.xpath(
                    "./td[1]/div/text()").extract_first()).replace('[', '').replace(']', '').replace('——', '')
                print(item)
                yield item
