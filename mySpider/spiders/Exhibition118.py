#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/11 14:11
# @Author  : 10711
# @File    : Exhibition118.py
# @Software: PyCharm


from ..items import *
from ..str_filter import *
from ..auxiliary_files import Exhibition118_supporting

class Exhibition118(scrapy.Spider):
    name = "Exhibition118"
    allowed_domains = ['tengzhoumuseum.com']
    start_urls = Exhibition118_supporting.Exhibition118Supporting.startUrl

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.ExhibitionPipeLine': 302,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.DefaultMiddleware': 0,
        },
    }

    def parse(self, response, **kwargs):
        li_list = response.xpath("/html/body/table[4]/tbody/tr/td[3]/table/tbody/tr[1]/td/table[2]/tbody/tr[1]/td/table")
        print(len(li_list))
        for li in li_list:
            item = ExhibitionItem()
            item["museumID"] = 118
            item["museumName"] = "山东省滕州市博物馆"
            url = StrFilter.getDoamin(response) + str(
                li.xpath("./tbody/tr[1]/td/a/@href").extract_first())
            yield scrapy.Request(
                url,
                callback=self.parseAnotherPage,
                meta={"item": item}
            )

    def parseAnotherPage(self, response):
        item = response.meta["item"]
        item["exhibitionName"] = StrFilter.filter(
            response.xpath("/html/body/table[4]/tbody/tr/td[2]/table/tbody/tr[1]/td/table[2]/tbody/tr[1]/td").xpath('string(.)').extract_first())
        item["exhibitionImageLink"] = StrFilter.getDoamin(response) + str(
            response.xpath("/html/body/table[4]/tbody/tr/td[2]/table/tbody/tr[1]/td/table[2]/tbody/tr[3]/td/p[11]/span/img/@src").extract_first())
        item['exhibitionIntroduction'] = StrFilter.filter(
            response.xpath("/html/body/table[4]/tbody/tr/td[2]/table/tbody/tr[1]/td/table[2]/tbody/tr[3]").xpath('string(.)').extract_first())
        item["exhibitionTime"] = StrFilter.filter(
            response.xpath("/html/body/table[4]/tbody/tr/td[2]/table/tbody/tr[1]/td/table[2]/tbody/tr[3]/td/p[3]").xpath('string(.)').extract_first())
        print(item)
        yield item