#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/11 14:11
# @Author  : 10711
# @File    : Exhibition80.py
# @Software: PyCharm


from ..items import *
from ..str_filter import *
from ..auxiliary_files import Exhibition80_supporting

class Exhibition80(scrapy.Spider):
    name = "Exhibition80"
    allowed_domains = ['nanhujng.com']
    start_urls = Exhibition80_supporting.Exhibition80Supporting.startUrl

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.ExhibitionPipeLine': 302,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.DefaultMiddleware': 0,
        },
    }

    def parse(self, response, **kwargs):
        li_list = response.xpath("/html/body/div[6]/div[1]/div[2]/div[2]/ul/li")
        print(len(li_list))
        for li in li_list:
            item = ExhibitionItem()
            item["museumID"] = 80
            item["museumName"] = "南湖革命纪念馆"
            item["exhibitionName"] = StrFilter.filter(
                li.xpath("./a").xpath('string(.)').extract_first())
            item["exhibitionTime"] = StrFilter.filter(
                li.xpath("./div").xpath('string(.)').extract_first())
            t=str(
                li.xpath("./a/@href").extract_first())
            t1=t.replace('./20','/20')
            url = StrFilter.getDoamin(response) +"/clzl/lszl" + t1
            print(url)
            yield scrapy.Request(
                url,
                callback=self.parseAnotherPage,
                meta={"item": item}
            )

    def parseAnotherPage(self, response):
        item = response.meta["item"]
        item["exhibitionImageLink"] = "NULL"
        item['exhibitionIntroduction'] = StrFilter.filter(
            response.xpath("/html/body/div[6]/div[1]/div[2]/div[2]/div/div[5]/div").xpath('string(.)').extract_first())

        print(item)
        yield item