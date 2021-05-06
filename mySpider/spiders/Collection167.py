#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/4 22:35
# @Author  : 10711
# @File    : Collection167.py
# @Software: PyCharm


from ..items import *
from ..str_filter import *
from ..auxiliary_files import Collection167_supporting


class Collection167(scrapy.Spider):
    name = "Collection167"
    allowed_domains = ['zgshm.cn']
    start_urls = Collection167_supporting.Collection167Supporting.startUrl

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        }
    }
    def parse(self, response, **kwargs):
        li_list = response.xpath("/html/body/ul/li")
        print(len(li_list))
        for li in li_list:
            item = CollectionItem()
            item["museumID"] = 167
            item["museumName"] = "自贡市盐业历史博物馆"
            item['collectionImageLink'] = StrFilter.getDoamin(response) + str(
                li.xpath("./img/@src").extract_first())
            url = StrFilter.getDoamin(response) + '/' + str(
                li.xpath("./a/@href").extract_first())
            yield scrapy.Request(
                url,
                callback=self.parseAnotherPage,
                meta={"item": item}
            )

    def parseAnotherPage(self, response):
        item = response.meta["item"]
        item['collectionName'] = StrFilter.filter(
            response.xpath("/html/body/div[3]/div/div[1]/div").xpath('string(.)').extract_first())
        item['collectionIntroduction'] = StrFilter.filter(
            response.xpath("//*[@id='news_conent_two_text']").xpath('string(.)').extract_first())
        print(item)
        yield(item)