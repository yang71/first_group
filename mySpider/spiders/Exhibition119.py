#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/11 14:11
# @Author  : 10711
# @File    : Exhibition119.py
# @Software: PyCharm


from ..items import *
from ..str_filter import *
from ..auxiliary_files import Exhibition119_supporting

class Exhibition119(scrapy.Spider):
    name = "Exhibition119"
    allowed_domains = ['tzhhxsg.com']
    start_urls = Exhibition119_supporting.Exhibition119Supporting.startUrl

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.ExhibitionPipeLine': 302,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.DefaultMiddleware': 0,
        },
    }

    def parse(self, response, **kwargs):
        li_list = response.xpath("/html/body/div[4]/div[3]/div/div[2]/div[2]/div[2]/a")
        print(len(li_list))
        for li in li_list:
            item = ExhibitionItem()
            item["museumID"] = 119
            item["museumName"] = "滕州市汉画像石馆"
            item["exhibitionName"] = StrFilter.filter(
                li.xpath("./p").xpath('string(.)').extract_first())

            url = StrFilter.getDoamin(response) + str(
                li.xpath("./@href").extract_first())
            yield scrapy.Request(
                url,
                callback=self.parseAnotherPage,
                meta={"item": item}
            )

    def parseAnotherPage(self, response):
        item = response.meta["item"]
        item["exhibitionImageLink"] = StrFilter.getDoamin(response) + str(
            response.xpath("/html/body/div[4]/div[3]/div/div[2]/div[2]/div[2]/p[17]/span/img/@src").extract_first())
        item['exhibitionIntroduction'] = StrFilter.filter(
            response.xpath("/html/body/div[4]/div[3]/div/div[2]/div[2]/div[2]").xpath('string(.)').extract_first())
        item["exhibitionTime"] = StrFilter.filter(
            response.xpath("/html/body/div[4]/div[3]/div/div[2]/div[2]/div[1]/span").xpath('string(.)').extract_first())
        print(item)
        yield item