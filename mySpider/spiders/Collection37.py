#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/5/1 18:21 
# @Author  : ana
# @File    : Collection37.py
# @Software: PyCharm

from ..items import *
from ..str_filter import *
from ..auxiliary_files import Collection37_supporting


class Collection37(scrapy.Spider):
    name = "Collection37"
    allowed_domains = ['sypm.org.cn']
    start_urls = Collection37_supporting.Collection37Supporting.startUrl

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        }
    }

    def parse(self, response, **kwargs):
        li_list = response.xpath("//*[@id='FrontProducts_list01-0042']/ul/li")
        print(len(li_list))
        for li in li_list:
            item = CollectionItem()
            item["museumID"] = 37
            item["museumName"] = "沈阳故宫博物院"
            item['collectionName'] = StrFilter.filter(li.xpath("./div[1]/div[1]/a/@title").extract_first()).replace('[',
                                                                                                                    '').replace(
                ']', '')
            item['collectionImageLink'] = 'http://www.sypm.org.cn' + str(li.xpath(
                "./div[1]/div[1]/a/img/@src").extract_first())
            url = "http://www.sypm.org.cn" + str(li.xpath("./div[1]/div[1]/a/@href").extract_first())
            yield scrapy.Request(
                url,
                callback=self.parseAnotherPage,
                meta={"item": item}
            )

    def parseAnotherPage(self, response):
        item = response.meta["item"]
        item['collectionIntroduction'] = StrFilter.filter(
            response.xpath("//*[@class='detail']").xpath('string(.)').extract_first()).replace('[', '').replace(
            ']', '')
        print(item)
        yield item
