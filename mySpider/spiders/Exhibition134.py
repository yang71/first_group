#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/11 14:11
# @Author  : 10711
# @File    : Exhibition134.py
# @Software: PyCharm


from ..items import *
from ..str_filter import *
from ..auxiliary_files import Exhibition134_supporting

class Exhibition134(scrapy.Spider):
    name = "Exhibition134"
    allowed_domains = ['zhongshanwarship.org.cn']
    start_urls = Exhibition134_supporting.Exhibition134Supporting.startUrl

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.ExhibitionPipeLine': 302,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.DefaultMiddleware': 0,
        },
    }

    def parse(self, response, **kwargs):
        li_list = response.xpath("//*[@id='caseListDIV']/div")
        print(len(li_list))
        for li in li_list:
            item = ExhibitionItem()
            item["museumID"] = 134
            item["museumName"] = "武汉市中山舰博物馆"
            item["exhibitionName"] = StrFilter.filter(
                li.xpath("./div/a/span").xpath('string(.)').extract_first())

            url = StrFilter.getDoamin(response) + str(
                li.xpath("./div/a/@href").extract_first())
            yield scrapy.Request(
                url,
                callback=self.parseAnotherPage,
                meta={"item": item}
            )

    def parseAnotherPage(self, response):
        item = response.meta["item"]
        item["exhibitionImageLink"] = StrFilter.getDoamin(response) + str(
            response.xpath("./div/a/img/@src").extract_first())
        item['exhibitionIntroduction'] = StrFilter.filter(
            response.xpath("/html/body/div[3]/div[1]/div[2]").xpath('string(.)').extract_first())
        item["exhibitionTime"] = StrFilter.filter(
            response.xpath("//*[@id='form']/div[3]/div[2]/div/div[2]/dl/dt[1]/b").xpath('string(.)').extract_first())
        print(item)
        yield item