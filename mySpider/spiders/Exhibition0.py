#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/5/7 10:42 
# @Author  : ana
# @File    : Exhibition0.py
# @Software: PyCharm

from ..items import *
from ..str_filter import *


class Exhibition0(scrapy.Spider):
    name = "Exhibition0"
    allowed_domains = ['dpm.org.cn']
    start_urls = ['https://www.dpm.org.cn/classify/exhibition.html']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.ExhibitionPipeLine': 302,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.DefaultMiddleware': 0,
        },
    }

    def parse(self, response, **kwargs):
        li_list = response.xpath("//*[@id='lists']/div[1]/div/div")
        print(len(li_list))
        for li in li_list:
            item = ExhibitionItem()
            item["museumID"] = 0
            item["museumName"] = "故宫博物院"
            item["exhibitionImageLink"] = StrFilter.getDoamin(response) + li.xpath(
                "./div[1]/a/img/@src").extract_first()
            item["exhibitionName"] = StrFilter.filter_2(li.xpath("./div[2]/div[1]/div[1]/a/text()").extract_first())
            item["exhibitionTime"] = StrFilter.filter_2(li.xpath("./div[2]/div[1]/div[2]/p[2]/text()").extract_first())
            url = str(li.xpath("./div[1]/a/@href").extract_first())
            print(item)
            yield scrapy.Request(
                url,
                callback=self.parseAnotherPage,
                meta={"item": item}
            )

    def parseAnotherPage(self, response):
        item = response.meta["item"]
        item['exhibitionIntroduction'] = StrFilter.filter_2(
            response.xpath("//div[@class='text_info']").xpath('string(.)').extract_first())
        print(item)
        yield item
