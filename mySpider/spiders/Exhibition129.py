#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/11 14:11
# @Author  : 10711
# @File    : Exhibition129.py
# @Software: PyCharm


from ..items import *
from ..str_filter import *
from ..auxiliary_files import Exhibition129_supporting

class Exhibition129(scrapy.Spider):
    name = "Exhibition129"
    allowed_domains = ['pdsm.org.cn']
    start_urls = Exhibition129_supporting.Exhibition129Supporting.startUrl

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.ExhibitionPipeLine': 302,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.DefaultMiddleware': 0,
        },
    }

    def parse(self, response, **kwargs):
        li_list = response.xpath("/html/body/div[3]/div[3]/ul/li")
        print(len(li_list))
        for li in li_list:
            item = ExhibitionItem()
            item["museumID"] = 129
            item["museumName"] = "平顶山博物馆"
            item["exhibitionName"] = StrFilter.filter(
                li.xpath("./p/a").xpath('string(.)').extract_first())
            item["exhibitionImageLink"] = StrFilter.getDoamin(response) + str(
                li.xpath("./a/img/@src").extract_first())
            url = StrFilter.getDoamin(response) + str(
                li.xpath("./p/a/@href").extract_first())
            yield scrapy.Request(
                url,
                callback=self.parseAnotherPage,
                meta={"item": item}
            )

    def parseAnotherPage(self, response):
        item = response.meta["item"]

        item['exhibitionIntroduction'] = StrFilter.filter(
            response.xpath("/html/body/div[3]/div[4]").xpath('string(.)').extract_first())
        item["exhibitionTime"] = "常设展览"
        print(item)
        yield item