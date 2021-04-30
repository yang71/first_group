#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/4/30 19:28 
# @Author  : ana
# @File    : Collection6.py
# @Software: PyCharm

from ..items import *
from ..str_filter import *
from ..auxiliary_files import Collection6_supporting


class Collection6(scrapy.Spider):
    name = "Collection6"
    allowed_domains = ['capitalmuseum.org.cn']
    start_urls = Collection6_supporting.Collection6Supporting.startUrl

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        }
    }

    def parse(self, response, **kwargs):
        img_list = response.xpath("//td[@height='108']/a/img/@src").extract()
        name_list = response.xpath("//td[@height='21']/a/text()").extract()
        url_list = response.xpath("//td[@height='21']/a/@href").extract()
        for i in range(12):
            item = CollectionItem()
            item["museumID"] = 6
            item["museumName"] = "首都博物馆"
            item['collectionName'] = name_list[i]
            item['collectionImageLink'] = 'http://www.capitalmuseum.org.cn/jpdc/' + img_list[i]
            url = 'http://www.capitalmuseum.org.cn/jpdc/' + url_list[i]
            yield scrapy.Request(
                url,
                callback=self.parseAnotherPage,
                meta={"item": item}
            )

    def parseAnotherPage(self, response):
        item = response.meta["item"]
        p_list = response.xpath("//div[@style='TEXT-ALIGN: left']/p/text()").extract()
        content = ""
        for p in p_list:
            content += p
        item['collectionIntroduction'] = StrFilter.filter(content).replace("[", "").replace("]", "")
        print(item)
        yield item
