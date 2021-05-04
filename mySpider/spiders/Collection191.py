#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/4 12:16
# @Author  : 10711
# @File    : Collection191.py
# @software: PyCharm

from ..items import *
from ..str_filter import *
from ..auxiliary_files import Collection191_supporting


class Collection191(scrapy.Spider):
    name = "Collection191"
    allowed_domains = ['bjqtm.com']
    start_urls = Collection191_supporting.Collection191Supporting.startUrl

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        }
    }
    def parse(self, response, **kwargs):
        li_list = response.xpath("/html/body/div[4]/div/div[2]/div[2]/div[1]/ul/li")
        print(len(li_list))
        for li in li_list:
            item = CollectionItem()
            item["museumID"] = 191
            item["museumName"] = "宝鸡青铜器博物院"
            item['collectionName'] = StrFilter.filter(
                li.xpath("./h2").xpath('string(.)').extract_first())
            item['collectionImageLink'] = StrFilter.getDoamin(response) + str(
                li.xpath("./div/@style").extract_first().replace("background:url('", '')).replace("') no-repeat center center/cover",'')
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
            response.xpath("/html/body/div[4]/div/div[2]/div[2]/div[1]").xpath('string(.)').extract_first())
        print(item)
        yield(item)