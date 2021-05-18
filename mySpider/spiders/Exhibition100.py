#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/11 14:11
# @Author  : 10711
# @File    : Exhibition100.py
# @Software: PyCharm


from ..items import *
from ..str_filter import *
from ..auxiliary_files import Exhibition100_supporting

class Exhibition100(scrapy.Spider):
    name = "Exhibition100"
    allowed_domains = ['lushanmuseum.com']
    start_urls = Exhibition100_supporting.Exhibition100Supporting.startUrl

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.ExhibitionPipeLine': 302,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.DefaultMiddleware': 0,
        },
    }

    def parse(self, response, **kwargs):
            item = ExhibitionItem()
            item["museumID"] = 100
            item["museumName"] = "江西省庐山博物馆"
            item["exhibitionName"] = StrFilter.filter(
                response.xpath("/html/body/table[4]/tbody/tr/td[3]/table/tbody/tr[2]/td/text()").xpath('string(.)').extract_first())
            item["exhibitionImageLink"] = StrFilter.getDoamin(response) + str(
                response.xpath("/html/body/table[4]/tbody/tr/td[3]/table/tbody/tr[4]/td/p[2]/img/@src").extract_first())
            item['exhibitionIntroduction'] = StrFilter.filter(
                response.xpath("/html/body/table[4]/tbody/tr/td[3]/table/tbody/tr[4]/td").xpath('string(.)').extract_first())
            item["exhibitionTime"] = "常设展览"
            print(item)
            yield item