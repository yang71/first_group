#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/4 16:41
# @Author  : 10711
# @File    : Collection172.py
# @Software: PyCharm


from ..items import *
from ..str_filter import *
from ..auxiliary_files import Collection172_supporting


class Collection172(scrapy.Spider):
    name = "Collection172"
    allowed_domains = ['zunyihy.cn']
    start_urls = Collection172_supporting.Collection172Supporting.startUrl

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        }
    }
    def parse(self, response, **kwargs):
        li_list = response.xpath("//*[@id='list_wenchuang']/div")
        print(len(li_list))
        for li in li_list:
            item = CollectionItem()
            item["museumID"] = 172
            item["museumName"] = "遵义会议纪念馆"
            item['collectionName'] = StrFilter.filter(
                li.xpath("./a/div[2]").xpath('string(.)').extract_first())
            item['collectionImageLink'] = StrFilter.getDoamin(response) + str(
                li.xpath("./a/div[1]/img/@src").extract_first())
            url = StrFilter.getDoamin(response) + str(
                li.xpath("./a/@href").extract_first())
            yield scrapy.Request(
                url,
                callback=self.parseAnotherPage,
                meta={"item": item}
            )

    def parseAnotherPage(self, response):
        item = response.meta["item"]
        item['collectionIntroduction'] = StrFilter.filter(
            response.xpath("/html/body/div[4]/div[3]/div/div[3]").xpath('string(.)').extract_first())
        print(item)
        #yield(item)