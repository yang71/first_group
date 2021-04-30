#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/4/30 16:19 
# @Author  : ana
# @File    : Collection1.py
# @Software: PyCharm

from ..items import *
from ..str_filter import *


class Collection1(scrapy.Spider):
    name = "Collection1"
    allowed_domains = ['cstm.cdstm.cn']
    start_urls = ['https://cstm.cdstm.cn/cszl/kxts/', ]

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        }
    }

    def parse(self, response, **kwargs):
        li_list = response.xpath("/html/body/div[4]/div[3]/div[2]/ul/li")
        for li in li_list:
            item = CollectionItem()
            item["museumID"] = 1
            item["museumName"] = "中国科学技术馆"
            item["collectionImageLink"] = 'cstm.cdstm.cn/cszl/kxts/' + str(li.xpath(
                "./a[1]/img/@src").extract_first())[1:]
            url = 'https://cstm.cdstm.cn/cszl/kxts' + str(li.xpath("./a[2]/@href").extract_first())[1:]
            yield scrapy.Request(
                url,
                callback=self.parseAnotherPage,
                meta={"item": item}
            )

    def parseAnotherPage(self, response):
        item = response.meta["item"]
        item['collectionName'] = response.xpath("/html/body/div[4]/div[3]/div[1]/h2/text()").extract_first()
        item['collectionIntroduction'] = ''.join(re.sub(StrFilter.r1, "", str(
            response.xpath("/html/body/div[4]/div[3]/div[1]/div[1]/p[1]/text()").extract_first())).split())
        print(item)
        yield item
