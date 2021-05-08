#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/5/7 14:26 
# @Author  : ana
# @File    : Exhibition3.py
# @Software: PyCharm


from ..items import *
from ..str_filter import *


class Exhibition3(scrapy.Spider):
    name = "Exhibition3"
    allowed_domains = ['jb.mil.cn']
    start_urls = ['http://www.jb.mil.cn/zlcl/jbcl/']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.ExhibitionPipeLine': 302,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.DefaultMiddleware': 0,
        },
    }

    def parse(self, response, **kwargs):
        li_list = response.xpath("/html/body/div[4]/ul/li")
        print(len(li_list))
        for li in li_list:
            item = ExhibitionItem()
            item["museumID"] = 3
            item["museumName"] = "中国人民革命军事博物馆"
            item["exhibitionImageLink"] = StrFilter.getDoamin(response) + '/zlcl/jbcl' + str(li.xpath(
                "./div[@class='basicImg']/img/@src").extract_first())[1:]
            item["exhibitionName"] = StrFilter.filter_2(li.xpath(
                "./div[@class='basicDes']/h3/text()|./div[@class='basicDes leftBasicDes']/h3/text()").extract_first())
            item["exhibitionTime"] = "常设展览"
            url = StrFilter.getDoamin(response) + '/zlcl/jbcl' + str(li.xpath(
                "./div[@class='basicDes']/dl/dt/a/@href|./div[@class='basicDes leftBasicDes']/dl/dt/a/@href").extract_first())[
                                                                 1:]
            print(url)
            yield scrapy.Request(
                url,
                callback=self.parseAnotherPage,
                meta={"item": item}
            )

    def parseAnotherPage(self, response):
        item = response.meta["item"]
        item['exhibitionIntroduction'] = StrFilter.filter_2(
            response.xpath("/html/body/div[4]/div/div[1]/div[3]/div/p[1]/text()").extract_first())
        print(item)
        yield item
