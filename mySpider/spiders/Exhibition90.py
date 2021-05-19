#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/11 14:11
# @Author  : 10711
# @File    : Exhibition90.py
# @Software: PyCharm


from ..items import *
from ..str_filter import *
from ..auxiliary_files import Exhibition90_supporting

class Exhibition90(scrapy.Spider):
    name = "Exhibition90"
    allowed_domains = ['qzhjg.cn']
    start_urls = Exhibition90_supporting.Exhibition90Supporting.startUrl

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.ExhibitionPipeLine': 302,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.DefaultMiddleware': 0,
        },
    }

    def parse(self, response, **kwargs):
        li_list = response.xpath("/html/body/div[1]/div[2]/div/div[3]/div/div/ul/li")
        print(len(li_list))
        for li in li_list:
            item = ExhibitionItem()
            item["museumID"] = 90
            item["museumName"] = "泉州海外交通史博物馆"
            item["exhibitionImageLink"] = StrFilter.getDoamin(response) + str(
                response.xpath("//*[@id='banner_list_2']/img/@src").extract_first())
            url = StrFilter.getDoamin(response) + str(
                li.xpath("./div[2]/a/@href").extract_first())
            yield scrapy.Request(
                url,
                callback=self.parseAnotherPage,
                meta={"item": item}
            )

    def parseAnotherPage(self, response):
        item = response.meta["item"]
        item["exhibitionName"] = StrFilter.filter(
            response.xpath("/html/body/div[1]/div[2]/div/div/div/div[2]/div[1]").xpath('string(.)').extract_first())
        item['exhibitionIntroduction'] = StrFilter.filter(
            response.xpath("/html/body/div[1]/div[2]/div/div/div/div[2]/div[2]").xpath('string(.)').extract_first())
        item["exhibitionTime"] = StrFilter.filter(
            response.xpath("/html/body/div[1]/div[2]/div/div/div/div[2]/p/span[2]").xpath('string(.)').extract_first())
        print(item)
        yield item