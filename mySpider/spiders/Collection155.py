#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/5 0:47
# @Author  : 10711
# @File    : Collection155.py
# @Software: PyCharm


from ..items import *
from ..str_filter import *
from ..auxiliary_files import Collection155_supporting


class Collection155(scrapy.Spider):
    name = "Collection155"
    allowed_domains = ['gxmuseum.cn']
    start_urls = Collection155_supporting.Collection155Supporting.startUrl

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        }
    }
    def parse(self, response, **kwargs):
        li_list = response.xpath("/html/body/div/div[2]/div[2]/div[2]/dl/dd/ul/li")
        print(len(li_list))
        for li in li_list:
            item = CollectionItem()
            item["museumID"] = 155
            item["museumName"] = "广西壮族自治区博物馆"
            item['collectionName'] = StrFilter.filter(
                li.xpath("./a[2]").xpath('string(.)').extract_first())
            item['collectionImageLink'] = StrFilter.getDoamin(response) + str(
                li.xpath("./a[1]/img/@src").extract_first())
            url = StrFilter.getDoamin(response) + str(
                li.xpath("./a[2]/@href").extract_first())
            yield scrapy.Request(
                url,
                callback=self.parseAnotherPage,
                meta={"item": item}
            )

    def parseAnotherPage(self, response):
        item = response.meta["item"]
        item['collectionIntroduction'] = StrFilter.filter(
            response.xpath("//*[@id='contentText']/div/p").xpath('string(.)').extract_first())
        print(item)
        yield(item)