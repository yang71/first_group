#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/5/7 22:41 
# @Author  : ana
# @File    : Exhibition29.py
# @Software: PyCharm


from ..items import *
from ..str_filter import *


class Exhibition29(scrapy.Spider):
    name = "Exhibition29"
    allowed_domains = ['sxgm.org']
    start_urls = ['http://www.sxgm.org/home/picnews/index/c_id/94/lanmu/59.html',
                  'http://www.sxgm.org/home/picnews/index/c_id/95/lanmu/59.html', ]

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.ExhibitionPipeLine': 302,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.DefaultMiddleware': 0,
        },
    }

    def parse(self, response, **kwargs):
        item = ExhibitionItem()
        item["museumID"] = 29
        item["museumName"] = "故宫博物院"
        item["exhibitionImageLink"] = StrFilter.getDoamin(response) + str(response.xpath(
            "//div[@class='center_right']//img/@src").extract_first())
        item["exhibitionName"] = StrFilter.filter_2(
            response.xpath("//div[@class='center_right']//img/@title").extract_first())
        item["exhibitionTime"] = "常设展览"
        url = StrFilter.getDoamin(response) + '/' + str(
            response.xpath("/html/body/div[5]/div/div[2]/ul/li/a/@href").extract_first())
        print(url)
        yield scrapy.Request(
            url,
            callback=self.parseAnotherPage,
            meta={"item": item}
        )

    def parseAnotherPage(self, response):
        item = response.meta["item"]
        item['exhibitionIntroduction'] = StrFilter.filter_2(
            response.xpath("/html/body/div[5]/div/div[2]/div[4]/table//tr[2]/td/div").xpath(
                'string(.)').extract_first())
        print(item)
        yield item
