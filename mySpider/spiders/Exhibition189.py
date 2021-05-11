#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/11 15:43
# @Author  : 10711
# @File    : Exhibition189.py
# @Software: PyCharm


from ..items import *
from ..str_filter import *
from ..auxiliary_files import Exhibition189_supporting

class Exhibition189(scrapy.Spider):
    name = "Exhibition189"
    allowed_domains = ['bpmuseum.com']
    start_urls = Exhibition189_supporting.Exhibition189Supporting.startUrl

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.ExhibitionPipeLine': 302,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.DefaultMiddleware': 0,
        },
    }

    def parse(self, response, **kwargs):
        li_list = response.xpath("//*[@id='brand-waterfall']/div")
        print(len(li_list))
        for li in li_list:
            item = ExhibitionItem()
            item["museumID"] = 189
            item["museumName"] = "西安半坡博物馆"
            item["exhibitionImageLink"] = StrFilter.getDoamin(response) + str(
                li.xpath("./div/a/img/@src").extract_first())
            item["exhibitionName"] = StrFilter.filter(
                li.xpath("./div/div/h3/a").xpath('string(.)').extract_first())
            item["exhibitionTime"] = "常设展览"
            url = str(
                li.xpath("./div/div/h3/a/@href").extract_first())
            yield scrapy.Request(
                url,
                callback=self.parseAnotherPage,
                meta={"item": item}
            )

    def parseAnotherPage(self, response):
        item = response.meta["item"]
        item['exhibitionIntroduction'] = StrFilter.filter(
            response.xpath("//*[@class='ti']").xpath('string(.)').extract_first())
        print(item)
        yield item