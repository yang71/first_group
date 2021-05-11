#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/5/7 18:10 
# @Author  : ana
# @File    : Exhibition13.py
# @Software: PyCharm


from ..items import *
from ..str_filter import *


class Exhibition13(scrapy.Spider):
    name = "Exhibition13"
    allowed_domains = ['pgm.org.cn']
    start_urls = ['http://www.pgm.org.cn/pgm/zzzc/zzzc_list.shtml']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.ExhibitionPipeLine': 302,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.DefaultMiddleware': 0,
        },
    }

    def parse(self, response, **kwargs):
        li_list = response.xpath("/html/body/div/div[3]/div[2]/ul/li")
        print(len(li_list))
        for li in li_list:
            item = ExhibitionItem()
            item["museumID"] = 13
            item["museumName"] = "恭王府博物馆"
            item["exhibitionName"] = StrFilter.filter_2(li.xpath("./a/text()").extract_first())
            url = StrFilter.getDoamin(response) + str(li.xpath("./a/@href").extract_first())[5:]
            print(url)
            yield scrapy.Request(
                url,
                callback=self.parseAnotherPage,
                meta={"item": item}
            )

    def parseAnotherPage(self, response):
        item = response.meta["item"]
        item["exhibitionImageLink"] = StrFilter.getDoamin(response) + "/pgm/xyhthks/202104/" + str(response.xpath(
            "//*[@id='content']//img/@src").extract_first())
        if str(item["exhibitionImageLink"])[-4:] == 'None':
            item["exhibitionImageLink"] = None
        item["exhibitionTime"] = "见详细介绍"
        item['exhibitionIntroduction'] = StrFilter.filter_2(
            response.xpath("//*[@id='content']").xpath('string(.)').extract_first())
        print(item)
        yield item
