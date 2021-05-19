#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/11 14:11
# @Author  : 10711
# @File    : Exhibition101.py
# @Software: PyCharm


from ..items import *
from ..str_filter import *
from ..auxiliary_files import Exhibition101_supporting

class Exhibition101(scrapy.Spider):
    name = "Exhibition101"
    allowed_domains = ['gzsbwg.cn',
                       'mp.weixin.qq.com']
    start_urls = Exhibition101_supporting.Exhibition101Supporting.startUrl

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.ExhibitionPipeLine': 302,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.DefaultMiddleware': 0,
        },
    }

    def parse(self, response, **kwargs):
        li_list = response.xpath("//*[@id='contentDiv']/div")
        print(len(li_list))
        for li in li_list:
            item = ExhibitionItem()
            item["museumID"] = 101
            item["museumName"] = "赣州市博物馆"
            item["exhibitionName"] = StrFilter.filter(
                li.xpath("./div/div[1]/a").xpath('string(.)').extract_first())
            item["exhibitionTime"] = StrFilter.filter(
               li.xpath("./div/div[2]").xpath('string(.)').extract_first())
            url = StrFilter.filter(
                li.xpath("./div/div[1]/a/@href").extract_first())
            yield scrapy.Request(
                url,
                callback=self.parseAnotherPage,
                meta={"item": item}
            )

    def parseAnotherPage(self, response):
        item = response.meta["item"]
        item["exhibitionImageLink"] = StrFilter.getDoamin(response) + str(
            response.xpath("//*[@id='js_content']/section/section[5]/section[1]/section/img/@src").extract_first())
        item['exhibitionIntroduction'] = StrFilter.filter(
            response.xpath("//*[@id='js_content']/section").xpath('string(.)').extract_first())

        print(item)
        yield item