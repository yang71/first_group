#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/5/7 13:09 
# @Author  : ana
# @File    : Exhibition1.py
# @Software: PyCharm


from ..items import *
from ..str_filter import *


class Exhibition(scrapy.Spider):
    name = "Exhibition1"
    allowed_domains = ['cstm.cdstm.cn']
    start_urls = ['https://cstm.cdstm.cn/cszl/yzzq/']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.ExhibitionPipeLine': 302,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.DefaultMiddleware': 0,
        },
    }

    def parse(self, response, **kwargs):
        li_list = response.xpath("/html/body/div[4]/div[3]/div[1]/ul/li/div/a[position()<9]")
        print(len(li_list))
        for li in li_list:
            item = ExhibitionItem()
            item["museumID"] = 1
            item["museumName"] = "中国科学技术馆"

            item["exhibitionTime"] = "常设展览"
            url = StrFilter.getDoamin(response) + '/cszl' + str(li.xpath("./@href").extract_first())[2:]
            print(url)
            yield scrapy.Request(
                url,
                callback=self.parseAnotherPage,
                meta={"item": item, "temp": str(li.xpath("./@href").extract_first())[2:]}
            )

    def parseAnotherPage(self, response):
        temp = response.meta["temp"]
        item = response.meta["item"]
        item["exhibitionName"] = StrFilter.filter_2(
            response.xpath("/html/body/div[4]/div[3]/div[2]/h3[1]/span[2]/text()").extract_first())[0:4]
        item["exhibitionImageLink"] = StrFilter.getDoamin(response) + '/cszl' + temp + str(response.xpath(
            "/html/body/div[4]/div[3]/div[2]/ul/li[1]/a[1]/img/@src").extract_first())[1:]
        item['exhibitionIntroduction'] = StrFilter.filter_2(
            response.xpath("/html/body/div[4]/div[3]/div[2]/div/text()").extract_first())
        if str(item["exhibitionName"]) != 'None':
            print(item)
            yield item
