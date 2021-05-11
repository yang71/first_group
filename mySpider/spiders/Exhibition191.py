#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/11 14:11
# @Author  : 10711
# @File    : Exhibition191.py
# @Software: PyCharm


from ..items import *
from ..str_filter import *
from ..auxiliary_files import Exhibition191_supporting

class Exhibition191(scrapy.Spider):
    name = "Exhibition191"
    allowed_domains = ['bjqtm.com']
    start_urls = Exhibition191_supporting.Exhibition191Supporting.startUrl

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.ExhibitionPipeLine': 302,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.DefaultMiddleware': 0,
        },
    }

    def parse(self, response, **kwargs):
        li_list = response.xpath("/html/body/div[4]/div/div[2]/div[2]/div[1]/ul/li")
        print(len(li_list))
        for li in li_list:
            item = ExhibitionItem()
            item["museumID"] = 191
            item["museumName"] = "宝鸡青铜器博物院"
            item["exhibitionName"] = StrFilter.filter(
                li.xpath("./h2").xpath('string(.)').extract_first())
            item["exhibitionTime"] = "常设展览"
            item["exhibitionImageLink"] = StrFilter.getDoamin(response) + str(
                li.xpath("./div/@style").extract_first()).replace("background:url('","").replace("') no-repeat center center/cover","")
            url = StrFilter.getDoamin(response) + str(
                li.xpath("./a/@href").extract_first())
            yield scrapy.Request(
                url,
                callback=self.parseAnotherPage,
                meta={"item": item}
            )

    def parseAnotherPage(self, response):
        item = response.meta["item"]
        item['exhibitionIntroduction'] = StrFilter.filter(
            response.xpath("/html/body/div[4]/div/div[2]/div[2]/div[1]").xpath('string(.)').extract_first())
        print(item)
        yield item