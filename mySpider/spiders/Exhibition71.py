#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/11 14:11
# @Author  : 10711
# @File    : Exhibition71.py
# @Software: PyCharm


from ..items import *
from ..str_filter import *
from ..auxiliary_files import Exhibition71_supporting

class Exhibition71(scrapy.Spider):
    name = "Exhibition71"
    allowed_domains = ['chinasilkmuseum.com']
    start_urls = Exhibition71_supporting.Exhibition71Supporting.startUrl

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.ExhibitionPipeLine': 302,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.DefaultMiddleware': 0,
        },
    }

    def parse(self, response, **kwargs):
        li_list = response.xpath("/html/body/div[1]/div/div[2]/div/ul/li")
        print(len(li_list))
        for li in li_list:
            item = ExhibitionItem()
            item["museumID"] = 71
            item["museumName"] = "中国丝绸博物馆"
            item["exhibitionName"] = StrFilter.filter(
                li.xpath("./div/h3/a").xpath('string(.)').extract_first())
            item["exhibitionImageLink"] = StrFilter.getDoamin(response) + str(
                li.xpath("./a[1]/img/@src").extract_first())
            url = StrFilter.getDoamin(response) + str(
                li.xpath("./a[1]/@href").extract_first())
            yield scrapy.Request(
                url,
                callback=self.parseAnotherPage,
                meta={"item": item}
            )

    def parseAnotherPage(self, response):
        item = response.meta["item"]
        item["exhibitionTime"] = StrFilter.filter(
            response.xpath("/html/body/div[1]/div/div[3]/div/div[2]/p[2]").xpath('string(.)').extract_first())
        item['exhibitionIntroduction'] = StrFilter.filter(
            response.xpath("/html/body/div[1]/div/div[3]/div/div[2]").xpath('string(.)').extract_first())
        print(item)
        yield item