#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/11 14:11
# @Author  : 10711
# @File    : Exhibition95.py
# @Software: PyCharm


from ..items import *
from ..str_filter import *
from ..auxiliary_files import Exhibition95_supporting

class Exhibition95(scrapy.Spider):
    name = "Exhibition95"
    allowed_domains = ['rjjng.com.cn']
    start_urls = Exhibition95_supporting.Exhibition95Supporting.startUrl

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.ExhibitionPipeLine': 302,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.DefaultMiddleware': 0,
        },
    }

    def parse(self, response, **kwargs):
        li_list = response.xpath("/html/body/div/div[3]/div/div[3]/ul/li")
        print(len(li_list))
        for li in li_list:
            item = ExhibitionItem()
            item["museumID"] = 95
            item["museumName"] = "瑞金中央革命根据地纪念馆"
            item["exhibitionName"] = StrFilter.filter(
                li.xpath("./div/h2/a").xpath('string(.)').extract_first())
            item["exhibitionImageLink"] = StrFilter.getDoamin(response) + str(
                li.xpath("./img/@src").extract_first())
            item["exhibitionTime"] = StrFilter.filter(
                li.xpath("./div/p").xpath('string(.)').extract_first())
            url = StrFilter.filter(
                li.xpath("./div/h2/a/@href").extract_first())
            print(url)
            yield scrapy.Request(
                url,
                callback=self.parseAnotherPage,
                meta={"item": item}
            )

    def parseAnotherPage(self, response):
        item = response.meta["item"]
        item['exhibitionIntroduction'] = StrFilter.filter(
            response.xpath("/html/body/div/div[3]/div/div[2]/div[1]").xpath('string(.)').extract_first())
        print(item)
        yield item