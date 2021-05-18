#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/11 14:11
# @Author  : 10711
# @File    : Exhibition104.py
# @Software: PyCharm


from ..items import *
from ..str_filter import *
from ..auxiliary_files import Exhibition104_supporting

class Exhibition104(scrapy.Spider):
    name = "Exhibition104"
    allowed_domains = ['qingdaomuseum.com']
    start_urls = Exhibition104_supporting.Exhibition104Supporting.startUrl

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.ExhibitionPipeLine': 302,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.DefaultMiddleware': 0,
        },
    }

    def parse(self, response, **kwargs):
        li_list = response.xpath("/html/body/div[6]/div[2]/div[2]/div[1]/div")
        print(len(li_list))
        for li in li_list:
            item = ExhibitionItem()
            item["museumID"] = 104
            item["museumName"] = "青岛市博物馆"
            item["exhibitionName"] = StrFilter.filter(
                li.xpath("./div/a/div/h4").xpath('string(.)').extract_first())
            item["exhibitionImageLink"] = StrFilter.getDoamin(response) + str(
                li.xpath("./div/a/img/@src").extract_first())
            url = StrFilter.filter(
                li.xpath("./div/a/@href").extract_first())
            yield scrapy.Request(
                url,
                callback=self.parseAnotherPage,
                meta={"item": item}
            )

    def parseAnotherPage(self, response):
        item = response.meta["item"]

        item['exhibitionIntroduction'] = StrFilter.filter(
            response.xpath("/html/body/div[6]/div[2]/div/div[4]").xpath('string(.)').extract_first())
        item["exhibitionTime"] = "常设展览"
        print(item)
        yield item