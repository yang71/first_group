#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/11 14:10
# @Author  : 10711
# @File    : Exhibition197.py
# @Software: PyCharm


from ..items import *
from ..str_filter import *
from ..auxiliary_files import Exhibition197_supporting

class Exhibition197(scrapy.Spider):
    name = "Exhibition197"
    allowed_domains = ['nxgybwg.com']
    start_urls = Exhibition197_supporting.Exhibition197Supporting.startUrl

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.ExhibitionPipeLine': 302,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.DefaultMiddleware': 0,
        },
    }

    def parse(self, response, **kwargs):
        li_list = response.xpath("//*[@id='body_wrap']/div/div[2]/div[2]/div[2]/dl")
        print(len(li_list))
        for li in li_list:
            item = ExhibitionItem()
            item["museumID"] = 197
            item["museumName"] = "固原博物馆"
            item["exhibitionImageLink"] = str(
                li.xpath("./dd[1]/a/img/@src").extract_first())
            if item["exhibitionImageLink"].startswith('/'):
                item["exhibitionImageLink"] = StrFilter.getDoamin(response) + item["exhibitionImageLink"]
            item["exhibitionName"] = StrFilter.filter(
                li.xpath("./dt/a").xpath('string(.)').extract_first())
            item["exhibitionTime"] = StrFilter.filter(
                li.xpath("./dt/span").xpath('string(.)').extract_first())
            url = StrFilter.getDoamin(response) + str(
                li.xpath("./dt/a/@href").extract_first())
            yield scrapy.Request(
                url,
                callback=self.parseAnotherPage,
                meta={"item": item}
            )

    def parseAnotherPage(self, response):
        item = response.meta["item"]
        item['exhibitionIntroduction'] = StrFilter.filter(
            response.xpath("//*[@id='body_wrap']/div/div[2]/div[2]/div/div[2]/div").xpath('string(.)').extract_first())
        print(item)
        yield item