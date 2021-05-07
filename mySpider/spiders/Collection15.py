#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/5/1 12:34 
# @Author  : ana
# @File    : Collection15.py
# @Software: PyCharm

from ..items import *


class Collection15(scrapy.Spider):
    name = "Collection15"
    allowed_domains = ['cnfm.org.cn']
    start_urls = ['http://www.cnfm.org.cn/gcjp/gcjp.shtml',
                  ]

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.DefaultMiddleware': 0,
        },
    }

    def parse(self, response, **kwargs):
        tr_list = response.xpath(
            "//tr[@height=160]")
        print(len(tr_list))
        for tr in tr_list:
            li_list = tr.xpath('./td')
            print(len(li_list))
            for li in li_list:
                item = CollectionItem()
                item["museumID"] = 15
                item["museumName"] = "中国电影博物馆"
                item['collectionName'] = li.xpath("./div[1]/p/a/text()").extract_first()
                item['collectionImageLink'] = 'http://www.cnfm.org.cn' + str(li.xpath(
                    "./div[1]/a/img/@src").extract_first())

                # introduction都是图片
                item['collectionIntroduction'] = None
                print(item)
                yield item
