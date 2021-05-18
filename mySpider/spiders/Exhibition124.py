#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/11 14:11
# @Author  : 10711
# @File    : Exhibition124.py
# @Software: PyCharm


from ..items import *
from ..str_filter import *
from ..auxiliary_files import Exhibition124_supporting

class Exhibition124(scrapy.Spider):
    name = "Exhibition124"
    allowed_domains = ['lymuseum.com']
    start_urls = Exhibition124_supporting.Exhibition124Supporting.startUrl

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.ExhibitionPipeLine': 302,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.DefaultMiddleware': 0,
        },
    }

    def parse(self, response, **kwargs):
        li_list = response.xpath("//*[@id='list_article']/tbody/tr[1]/td/table/tbody/tr/td/div")
        print(len(li_list))
        for li in li_list:
            item = ExhibitionItem()
            item["museumID"] = 124
            item["museumName"] = "洛阳博物馆"
            item["exhibitionName"] = StrFilter.filter(
                li.xpath("./p[2]").xpath('string(.)').extract_first())
            item["exhibitionImageLink"] = StrFilter.getDoamin(response) + str(
                li.xpath("./p[1]/a/img/@src").extract_first())
            url = StrFilter.getDoamin(response) + str(
                li.xpath("./p[2]/a/@href").extract_first())
            yield scrapy.Request(
                url,
                callback=self.parseAnotherPage,
                meta={"item": item}
            )

    def parseAnotherPage(self, response):
        item = response.meta["item"]

        item['exhibitionIntroduction'] = StrFilter.filter(
            response.xpath("//*[@id='viewphoto']/tbody/tr[1]/td/table[2]/tbody/tr[2]").xpath('string(.)').extract_first())
        item["exhibitionTime"] = StrFilter.filter(
            response.xpath("//*[@id='form']/div[3]/div[2]/div/div[2]/dl/dt[1]/b").xpath('string(.)').extract_first())
        print(item)
        yield item