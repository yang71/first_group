#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/5/1 17:28 
# @Author  : ana
# @File    : Collection36.py
# @Software: PyCharm

from ..items import *
from ..str_filter import *
from ..auxiliary_files import Collection36_supporting


class Collection36(scrapy.Spider):
    name = "Collection36"
    allowed_domains = ['lvshunmuseum.org']
    start_urls = Collection36_supporting.Collection36Supporting.startUrl

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        }
    }

    def parse(self, response, **kwargs):
        li_list = response.xpath("//*[@id='tab']/div/div/div[2]/ul/li")
        print(len(li_list))
        for li in li_list:
            item = CollectionItem()
            item["museumID"] = 36
            item["museumName"] = "旅顺博物馆"
            item['collectionName'] = StrFilter.filter(li.xpath("./a/div[1]/img/@alt").extract_first()).replace('[',
                                                                                                               '').replace(
                ']', '')
            item['collectionImageLink'] = 'http://www.lvshunmuseum.org' + str(li.xpath(
                "./a/div[1]/img/@src").extract_first())[1:]
            url = "http://www.lvshunmuseum.org" + str(li.xpath("./a/@href").extract_first())[1:]
            yield scrapy.Request(
                url,
                callback=self.parseAnotherPage,
                meta={"item": item}
            )

    def parseAnotherPage(self, response):
        item = response.meta["item"]
        item['collectionIntroduction'] = StrFilter.filter(
            response.xpath("//*[@id='showcasescontent']/div/div[3]/p").xpath('string(.)').extract_first()).replace('[',
                                                                                                                   '').replace(
            ']', '')
        print(item)
        yield item
