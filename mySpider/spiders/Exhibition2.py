#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/5/7 13:36 
# @Author  : ana
# @File    : Exhibition2.py
# @Software: PyCharm


from ..items import *
from ..str_filter import *


class Exhibition(scrapy.Spider):
    name = "Exhibition2"
    allowed_domains = ['gmc.org.cn']
    start_urls = ['http://www.gmc.org.cn/exhib_views.html']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.ExhibitionPipeLine': 302,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.DefaultMiddleware': 0,
        },
    }

    def parse(self, response, **kwargs):
        li_list = response.xpath("//*[@id='datalist']/div/div")
        print(len(li_list))
        for li in li_list:
            item = ExhibitionItem()
            item["museumID"] = 2
            item["museumName"] = "中国地质博物馆"
            item["exhibitionName"] = StrFilter.filter_2(li.xpath("./a/div[1]/text()").extract_first())
            item["exhibitionTime"] = StrFilter.filter_2(li.xpath("./a/div[2]").xpath('string(.)').extract_first())
            if len(item["exhibitionTime"]) == 0:
                item["exhibitionTime"] = "常设展览"
            url = StrFilter.getDoamin(response) + str(li.xpath("./a/@href").extract_first())
            yield scrapy.Request(
                url,
                callback=self.parseAnotherPage,
                meta={"item": item}
            )

    def parseAnotherPage(self, response):
        item = response.meta["item"]
        item["exhibitionImageLink"] = StrFilter.getDoamin(response) + response.xpath(
            "/html/body/div[4]/div/div/div[2]/p[2]/img/@src").extract_first()
        item['exhibitionIntroduction'] = None
        print(item)
        yield item
