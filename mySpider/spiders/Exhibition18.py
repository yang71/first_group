#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/5/7 19:28 
# @Author  : ana
# @File    : Exhibition18.py
# @Software: PyCharm


from ..items import *
from ..str_filter import *


class Exhibition18(scrapy.Spider):
    name = "Exhibition18"
    allowed_domains = ['tjbwg.com']
    start_urls = ['https://www.tjbwg.com/cn/ExhibitionList.aspx?TypeId=10938']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.ExhibitionPipeLine': 302,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.DefaultMiddleware': 0,
        },
    }

    def parse(self, response, **kwargs):
        li_list = response.xpath("/html/body/div/div[3]/div/div/div[2]/div[2]/div/div/ul/li")
        print(len(li_list))
        for li in li_list:
            item = ExhibitionItem()
            item["museumID"] = 18
            item["museumName"] = "天津博物馆"
            item["exhibitionImageLink"] = StrFilter.getDoamin(response) + '/cn/' + str(li.xpath(
                "./div[1]/a/div[1]/img/@src").extract_first())
            item["exhibitionName"] = StrFilter.filter_2(li.xpath("./div[1]/a/div[2]/h3/text()").extract_first())
            item["exhibitionTime"] = StrFilter.filter_2(li.xpath("./div[1]/a/div[2]/div/p[2]/text()").extract_first())
            url = StrFilter.getDoamin(response) + '/cn/' + str(li.xpath("./div[1]/a/@href").extract_first())
            print(url)
            yield scrapy.Request(
                url,
                callback=self.parseAnotherPage,
                meta={"item": item}
            )

    def parseAnotherPage(self, response):
        item = response.meta["item"]
        item['exhibitionIntroduction'] = StrFilter.filter_2(
            response.xpath("//div[@class='exhUs_r']").xpath('string(.)').extract_first())
        print(item)
        yield item
