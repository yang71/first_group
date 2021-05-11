#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/5/7 20:11 
# @Author  : ana
# @File    : Exhibition21.py
# @Software: PyCharm


from ..items import *
from ..str_filter import *


class Exhibition21(scrapy.Spider):
    name = "Exhibition21"
    allowed_domains = ['pjcmm.com']
    start_urls = ['http://www.pjcmm.com/listPro.aspx?cateid=79']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.ExhibitionPipeLine': 302,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.DefaultMiddleware': 0,
        },
    }

    def parse(self, response, **kwargs):
        li_list = response.xpath("/html/body/div[4]/div[2]/ul/li")
        print(len(li_list))
        for li in li_list:
            item = ExhibitionItem()
            item["museumID"] = 21
            item["museumName"] = "平津战役纪念馆"
            item["exhibitionImageLink"] = StrFilter.getDoamin(response) + str(li.xpath(
                "./a/img/@src").extract_first())
            item["exhibitionName"] = StrFilter.filter_2(li.xpath("./a/p/text()").extract_first())
            item["exhibitionTime"] = '常设展览'
            url = StrFilter.getDoamin(response) + '/' + str(li.xpath("./a/@href").extract_first())
            print(url)
            yield scrapy.Request(
                url,
                callback=self.parseAnotherPage,
                meta={"item": item}
            )

    def parseAnotherPage(self, response):
        item = response.meta["item"]
        item['exhibitionIntroduction'] = StrFilter.filter_2(
            response.xpath("/html/body/div[4]/div[2]/p/span").xpath('string(.)').extract_first())
        print(item)
        yield item
