#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/11 14:11
# @Author  : 10711
# @File    : Exhibition66.py
# @Software: PyCharm


from ..items import *
from ..str_filter import *
from ..auxiliary_files import Exhibition66_supporting

class Exhibition66(scrapy.Spider):
    name = "Exhibition66"
    allowed_domains = ['xzmuseum.com']
    start_urls = Exhibition66_supporting.Exhibition66Supporting.startUrl

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.ExhibitionPipeLine': 302,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.DefaultMiddleware': 0,
        },
    }

    def parse(self, response, **kwargs):
        li_list = response.xpath("/html/body/div[4]/div/div[2]/div[2]/div[3]/div")
        print(len(li_list))
        for li in li_list:
            item = ExhibitionItem()
            item["museumID"] = 66
            item["museumName"] = "徐州博物馆"
            item["exhibitionName"] = StrFilter.filter(
                li.xpath("./h2/a").xpath('string(.)').extract_first())
            item["exhibitionImageLink"] = StrFilter.getDoamin(response) + str(
                response.xpath("./img/@src").extract_first())
            item["exhibitionTime"] = StrFilter.filter(
                li.xpath("./p").xpath('string(.)').extract_first())
            url = StrFilter.getDoamin(response) + str(
                li.xpath("./h2/a/@href").extract_first())
            yield scrapy.Request(
                url,
                callback=self.parseAnotherPage,
                meta={"item": item}
            )

    def parseAnotherPage(self, response):
        item = response.meta["item"]

        item['exhibitionIntroduction'] = StrFilter.filter(
            response.xpath("/html/body/div[4]/div/div[2]/div[2]/div[3]").xpath('string(.)').extract_first())

        print(item)
        yield item