#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/5/7 14:42 
# @Author  : ana
# @File    : Exhibition4.py
# @Software: PyCharm


from ..items import *
from ..str_filter import *


class Exhibition4(scrapy.Spider):
    name = "Exhibition4"
    allowed_domains = ['casc-spacemuseum.com']
    start_urls = ['http://www.casc-spacemuseum.com/exhibition.aspx?category=13']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.ExhibitionPipeLine': 302,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.DefaultMiddleware': 0,
        },
    }

    def parse(self, response, **kwargs):
        li_list = response.xpath("//*[@id='right']/div[2]/ul/li")
        print(len(li_list))
        for li in li_list:
            item = ExhibitionItem()
            item["museumID"] = 4
            item["museumName"] = "中国航天博物馆"
            item["exhibitionImageLink"] = StrFilter.getDoamin(response) + '/' + li.xpath("./a/img/@src").extract_first()
            item["exhibitionName"] = StrFilter.filter_2(li.xpath("./h3/a/text()").extract_first())
            item["exhibitionTime"] = "常设展览"
            url = StrFilter.getDoamin(response) + '/' + str(li.xpath("./a/@href").extract_first())
            print(url)
            yield scrapy.Request(
                url,
                callback=self.parseAnotherPage,
                meta={"item": item}
            )

    def parseAnotherPage(self, response):
        item = response.meta["item"]
        item['exhibitionIntroduction'] = StrFilter.filter_2(
            response.xpath("//*[@class='article']").xpath('string(.)').extract_first())
        print(item)
        yield item
