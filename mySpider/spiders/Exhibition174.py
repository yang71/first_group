#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/11 20:10
# @Author  : 10711
# @File    : Exhibition174.py
# @Software: PyCharm


from ..items import *
from ..str_filter import *
from ..auxiliary_files import Exhibition174_supporting

class Exhibition174(scrapy.Spider):
    name = "Exhibition174"
    allowed_domains = ['gzsmzmuseum.cn']
    start_urls = Exhibition174_supporting.Exhibition174Supporting.startUrl

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.ExhibitionPipeLine': 302,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.DefaultMiddleware': 0,
        },
    }

    def parse(self, response, **kwargs):
        li_list = response.xpath("//*[@class='newsli']/li")
        print(len(li_list))
        for li in li_list:
            item = ExhibitionItem()
            item["museumID"] = 174
            item["museumName"] = "贵州省民族博物馆"
            item["exhibitionImageLink"] = StrFilter.getDoamin(response) + str(
                li.xpath("./div[1]/a/div/img/@src").extract_first())
            item["exhibitionName"] = StrFilter.filter(
                li.xpath("./h3/a").xpath('string(.)').extract_first())
            item["exhibitionTime"] = "常设展览"
            item['exhibitionIntroduction'] = StrFilter.filter(
                li.xpath("./p/a").xpath('string(.)').extract_first())
            print(item)
            yield item