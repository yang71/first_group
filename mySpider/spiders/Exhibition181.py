#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/11 15:44
# @Author  : 10711
# @File    : Exhibition181.py
# @Software: PyCharm


from ..items import *
from ..str_filter import *
from ..auxiliary_files import Exhibition181_supporting

class Exhibition181(scrapy.Spider):
    name = "Exhibition181"
    allowed_domains = ['cqsxymjng.cn']
    start_urls = Exhibition181_supporting.Exhibition181Supporting.startUrl

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.ExhibitionPipeLine': 302,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.DefaultMiddleware': 0,
        },
    }

    def parse(self, response, **kwargs):
        li_list = response.xpath("/html/body/div[3]/div[1]/ul")
        print(len(li_list))
        for li in li_list:
            item = ExhibitionItem()
            item["museumID"] = 181
            item["museumName"] = "重庆三峡移民纪念馆"
            item["exhibitionImageLink"] = str(
                li.xpath("./li/span[1]/a/img/@src").extract_first())
            item["exhibitionName"] = StrFilter.filter(
                li.xpath("./li/span[2]/h2/a").xpath('string(.)').extract_first())
            item["exhibitionTime"] = "常设展览"
            url = str(
                li.xpath("./li/span[2]/h2/a/@href").extract_first())
            yield scrapy.Request(
                url,
                callback=self.parseAnotherPage,
                meta={"item": item}
            )

    def parseAnotherPage(self, response):
        item = response.meta["item"]
        item['exhibitionIntroduction'] = StrFilter.filter(
            response.xpath("//*[@id='zoom']").xpath('string(.)').extract_first())
        print(item)
        yield item