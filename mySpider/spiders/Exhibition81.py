#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/11 14:11
# @Author  : 10711
# @File    : Exhibition81.py
# @Software: PyCharm


from ..items import *
from ..str_filter import *
from ..auxiliary_files import Exhibition81_supporting

class Exhibition81(scrapy.Spider):
    name = "Exhibition81"
    allowed_domains = ['njmuseumadmin.com']
    start_urls = Exhibition81_supporting.Exhibition81Supporting.startUrl

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.ExhibitionPipeLine': 302,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.DefaultMiddleware': 0,
        },
    }

    def parse(self, response, **kwargs):
        li_list = response.xpath("//*[@id='form']/div[3]/div[4]/div")
        print(len(li_list))
        for li in li_list:
            item = ExhibitionItem()
            item["museumID"] = 81
            item["museumName"] = "南京市博物总馆"
            item["exhibitionName"] = StrFilter.filter(
                li.xpath("./div/span").xpath('string(.)').extract_first())

            url = StrFilter.getDoamin(response) + str(
                li.xpath("./a/@href").extract_first())
            yield scrapy.Request(
                url,
                callback=self.parseAnotherPage,
                meta={"item": item}
            )

    def parseAnotherPage(self, response):
        item = response.meta["item"]
        item["exhibitionImageLink"] = StrFilter.getDoamin(response) + str(
            response.xpath("//*[@id='form']/div[3]/div[2]/div/div[1]/img/@src").extract_first())
        item['exhibitionIntroduction'] = StrFilter.filter(
            response.xpath("//*[@id='form']/div[3]/div[3]").xpath('string(.)').extract_first())
        item["exhibitionTime"] = StrFilter.filter(
            response.xpath("//*[@id='form']/div[3]/div[2]/div/div[2]/dl/dt[1]/b").xpath('string(.)').extract_first())
        print(item)
        yield item