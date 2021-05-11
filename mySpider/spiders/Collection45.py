#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/5/1 20:03 
# @Author  : ana
# @File    : Collection45.py
# @Software: PyCharm

from ..items import *
from ..str_filter import *


class Collection45(scrapy.Spider):
    name = "Collection45"
    allowed_domains = ['aihuihistorymuseum.org.cn']
    start_urls = ['http://www.aihuihistorymuseum.org.cn/imglist.aspx?type=377']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.DefaultMiddleware': 0,
        },
    }

    def parse(self, response, **kwargs):
        li_list = response.xpath("//*[@id='form1']/div[4]/div[1]/div/div[2]/div")
        print(len(li_list))
        for li in li_list:
            item = CollectionItem()
            item["museumID"] = 45
            item["museumName"] = "爱辉历史陈列馆"
            item['collectionImageLink'] = 'http://www.aihuihistorymuseum.org.cn/' + str(li.xpath(
                "./a/div[1]/img/@src").extract_first())
            url = "http://www.aihuihistorymuseum.org.cn/" + str(li.xpath("./a/@href").extract_first())
            yield scrapy.Request(
                url,
                callback=self.parseAnotherPage,
                meta={"item": item}
            )

    def parseAnotherPage(self, response):
        item = response.meta["item"]
        item['collectionName'] = StrFilter.filter(
            response.xpath("//*[@id='ContentPlaceHolder1_title']/text()").extract_first()).replace('[', '').replace(']',
                                                                                                                    '')
        item['collectionIntroduction'] = StrFilter.filter(
            response.xpath("//*[@id='form1']/div[4]/div[1]/div/div[2]/div[2]/div[3]").xpath(
                'string(.)').extract_first()).replace('[', '').replace(
            ']', '').split("主编")[0]
        print(item)
        yield item
