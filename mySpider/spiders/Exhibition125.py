#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/11 14:11
# @Author  : 10711
# @File    : Exhibition125.py
# @Software: PyCharm


from ..items import *
from ..str_filter import *
from ..auxiliary_files import Exhibition125_supporting

class Exhibition125(scrapy.Spider):
    name = "Exhibition125"
    allowed_domains = ['nyhhg.com']
    start_urls = Exhibition125_supporting.Exhibition125Supporting.startUrl

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.ExhibitionPipeLine': 302,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.DefaultMiddleware': 0,
        },
    }

    def parse(self, response, **kwargs):
        li_list = response.xpath("/html/body/div[4]/div[2]/div[2]/ul/li")
        print(len(li_list))
        for li in li_list:
            item = ExhibitionItem()
            item["museumID"] = 125
            item["museumName"] = "南阳汉画馆"
            item["exhibitionName"] = StrFilter.filter(
                li.xpath("./div[2]/h2/a").xpath('string(.)').extract_first())
            item["exhibitionImageLink"] = StrFilter.getDoamin(response) + str(
                li.xpath("./div[1]/a/img/@src").extract_first())
            url = StrFilter.getDoamin(response) + str(
                li.xpath("./div[2]/h2/a/@href").extract_first())
            yield scrapy.Request(
                url,
                callback=self.parseAnotherPage,
                meta={"item": item}
            )

    def parseAnotherPage(self, response):
        item = response.meta["item"]

        item['exhibitionIntroduction'] = StrFilter.filter(
            response.xpath("/html/body/div[4]/div[2]/div[2]").xpath('string(.)').extract_first())
        t=StrFilter.filter(
            response.xpath("/html/body/div[4]/div[2]/div[2]/div[2]").xpath('string(.)').extract_first())
        t1=t.replace('浏览：发布日期：','')
        item["exhibitionTime"] = t1
        print(item)
        yield item