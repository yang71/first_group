#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/5/1 13:40 
# @Author  : ana
# @File    : Collection18.py
# @Software: PyCharm

from ..items import *
from ..str_filter import *


class Collection18(scrapy.Spider):
    name = "Collection18"
    allowed_domains = ['tjbwg.com']
    start_urls = ['https://www.tjbwg.com/cn/collectionInfo.aspx?Id=2673',
                  'https://www.tjbwg.com/cn/collectionInfo.aspx?Id=2672',
                  'https://www.tjbwg.com/cn/collectionInfo.aspx?Id=2668',
                  'https://www.tjbwg.com/cn/collectionInfo.aspx?Id=2667',
                  'https://www.tjbwg.com/cn/collectionInfo.aspx?Id=2632',
                  'https://www.tjbwg.com/cn/collectionInfo.aspx?Id=2631',
                  'https://www.tjbwg.com/cn/collectionInfo.aspx?Id=2630',
                  'https://www.tjbwg.com/cn/collectionInfo.aspx?Id=2550',
                  'https://www.tjbwg.com/cn/collectionInfo.aspx?Id=2538',
                  'https://www.tjbwg.com/cn/collectionInfo.aspx?Id=2618', ]

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.DefaultMiddleware': 0,
        },
    }

    def parse(self, response, **kwargs):
        item = CollectionItem()
        item["museumID"] = 18
        item["museumName"] = "天津博物馆"
        item['collectionName'] = StrFilter.filter(
            response.xpath(
                "/html/body/div/div[2]/div/div/div[2]/div[2]/div[1]/div[1]/h3/text()").extract_first()).replace(']',
                                                                                                                '').replace(
            '[', '')
        item['collectionImageLink'] = str(response.xpath(
            "//div[@class='collD clearfix']/div[@class='imgList_cd']/div[@class='imgList_in']/ul/li/img/@src").extract_first())
        item['collectionIntroduction'] = StrFilter.filter(
            response.xpath("/html/body/div/div[2]/div/div/div[2]/div[2]/div[1]/div[2]").xpath(
                'string(.)').extract_first()).replace(']', '').replace('[', '')
        print(item)
        yield item
