#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/11 20:11
# @Author  : 10711
# @File    : Exhibition171.py
# @Software: PyCharm


from ..items import *
from ..str_filter import *
from ..auxiliary_files import Exhibition171_supporting

class Exhibition171(scrapy.Spider):
    name = "Exhibition171"
    allowed_domains = ['zhudeguli.com']
    start_urls = Exhibition171_supporting.Exhibition171Supporting.startUrl

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.ExhibitionPipeLine': 302,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.DefaultMiddleware': 0,
        },
    }

    def parse(self, response, **kwargs):
        li_list = response.xpath("/html/body/div[2]/div/div[2]/div[2]/ul/li")
        print(len(li_list))
        for li in li_list:
            item = ExhibitionItem()
            item["museumID"] = 171
            item["museumName"] = "朱德同志故居纪念馆"
            item["exhibitionImageLink"] = str(
                li.xpath("./a/img/@src").extract_first())
            item["exhibitionName"] = StrFilter.filter(
                li.xpath("./a/span").xpath('string(.)').extract_first())
            item["exhibitionTime"] = "常设展览"
            url = str(
                li.xpath("./a/@href").extract_first())
            yield scrapy.Request(
                url,
                callback=self.parseAnotherPage,
                meta={"item": item}
            )

    def parseAnotherPage(self, response):
        item = response.meta["item"]
        item['exhibitionIntroduction'] = StrFilter.filter(
            response.xpath("//*[@id='content']").xpath('string(.)').extract_first()).replace('\u200d', '')
        print(item)
        yield item