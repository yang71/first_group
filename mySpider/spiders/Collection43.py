#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/5/2 15:41 
# @Author  : ana
# @File    : Collection43.py
# @Software: PyCharm

from ..items import *
from ..str_filter import *


class Collection43(scrapy.Spider):
    name = "Collection43"
    allowed_domains = ['baike.baidu.com']
    start_urls = ['https://baike.baidu.com/item/%E4%B8%9C%E5%8C%97%E7%83%88%E5%A3%AB%E7%BA%AA%E5%BF%B5%E9%A6%86']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        }
    }

    def parse(self, response, **kwargs):
        li_list = response.xpath("/html/body/div[3]/div[2]/div/div[1]/table[1]//tr")
        print(len(li_list))
        for li in li_list:
            if li == li_list[-1]:
                continue
            item = CollectionItem()
            item["museumID"] = 43
            item["museumName"] = "东北烈士纪念馆"
            item['collectionName'] = StrFilter.filter(
                li.xpath(".//td[2]/div[1]/text()").extract_first()).replace('[', '').replace(']', '')
            item['collectionIntroduction'] = StrFilter.filter(
                li.xpath(".//td[2]/div[1]/text()").extract_first()).replace('[',
                                                                            '').replace(
                ']', '')
            item['collectionImageLink'] = 'https://baike.baidu.com' + str(li.xpath(
                "./td[1]/div[1]/div[1]/a/@href").extract_first())
            print(item)
            yield item
