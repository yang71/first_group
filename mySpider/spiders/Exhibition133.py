#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/11 14:11
# @Author  : 10711
# @File    : Exhibition133.py
# @Software: PyCharm


from ..items import *
from ..str_filter import *
from ..auxiliary_files import Exhibition133_supporting

class Exhibition133(scrapy.Spider):
    name = "Exhibition133"
    allowed_domains = ['wlt.hubei.gov.cn']
    start_urls = Exhibition133_supporting.Exhibition133Supporting.startUrl

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.ExhibitionPipeLine': 302,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.DefaultMiddleware': 0,
        },
    }

    def parse(self, response, **kwargs):
        li_list = response.xpath("/html/body/div/div[3]/div[1]/ul/li")
       # print(len(li_list))
        for li in li_list:
            item = ExhibitionItem()
            item["museumID"] = 133
            item["museumName"] = "辛亥革命武昌起义纪念馆"
            item["exhibitionName"] = StrFilter.filter(
                li.xpath("./h4/a").xpath('string(.)').extract_first())

            url = StrFilter.getDoamin(response) + str(
                li.xpath("./h4/a/@href").extract_first())
            print(url)
            yield scrapy.Request(
                url,
                callback=self.parseAnotherPage,
                meta={"item": item}
            )

    def parseAnotherPage(self, response):
        item = response.meta["item"]
        item["exhibitionImageLink"] = StrFilter.getDoamin(response) + str(
            response.xpath("/html/body/div[9]/div[3]/div/div/div[2]/div/p[1]/img/@src").extract_first())
        item['exhibitionIntroduction'] = StrFilter.filter(
            response.xpath("//*[@id='form']/div[3]/div[3]").xpath('string(.)').extract_first())
        item["exhibitionTime"] = StrFilter.filter(
            response.xpath("/html/body/div[9]/div[3]/div/div/div[1]/div/span[1]").xpath('string(.)').extract_first())
