#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/11 14:11
# @Author  : 10711
# @File    : Exhibition132.py
# @Software: PyCharm


from ..items import *
from ..str_filter import *
from ..auxiliary_files import Exhibition132_supporting

class Exhibition132(scrapy.Spider):
    name = "Exhibition132"
    allowed_domains = ['jzmsm.org']
    start_urls = Exhibition132_supporting.Exhibition132Supporting.startUrl

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.ExhibitionPipeLine': 302,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.DefaultMiddleware': 0,
        },
    }

    def parse(self, response, **kwargs):
        li_list = response.xpath("/html/body/div[3]/div[1]/ul/div/ul/li")
        print(len(li_list))
        for li in li_list:
            item = ExhibitionItem()
            item["museumID"] = 132
            item["museumName"] = "荆州博物馆"
            item["exhibitionName"] = StrFilter.filter(
                li.xpath("./a").xpath('string(.)').extract_first())

            url = StrFilter.getDoamin(response) + str(
                li.xpath("./a/@href").extract_first())
            yield scrapy.Request(
                url,
                callback=self.parseAnotherPage,
                meta={"item": item}
            )

    def parseAnotherPage(self, response):
        item = response.meta["item"]
        item["exhibitionImageLink"] = StrFilter.getDoamin(response) + str(
            response.xpath("/html/body/div[6]/div/div[3]/p[1]/span/img/@src").extract_first())
        item['exhibitionIntroduction'] = StrFilter.filter(
            response.xpath("/html/body/div[6]/div/div[3]").xpath('string(.)').extract_first())
        t=StrFilter.filter(
            response.xpath("/html/body/div[6]/div/div[2]/center/span[1]").xpath('string(.)').extract_first())
        t1=t.replace('发布时间：','')
        item["exhibitionTime"] = t1
        print(item)
        yield item