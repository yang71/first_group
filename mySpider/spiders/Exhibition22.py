#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/5/7 20:19 
# @Author  : ana
# @File    : Exhibition22.py
# @Software: PyCharm

from ..items import *
from ..str_filter import *


class Exhibition22(scrapy.Spider):
    name = "Exhibition22"
    allowed_domains = ['hebeimuseum.org.cn']
    start_urls = ['http://www.hebeimuseum.org.cn/channels/12.html']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.ExhibitionPipeLine': 302,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.DefaultMiddleware': 0,
        },
    }

    def parse(self, response, **kwargs):
        li_list = response.xpath("//*[@id='content']/div[2]/div[2]/div/ul/li")
        print(len(li_list))
        for li in li_list:
            item = ExhibitionItem()
            item["museumID"] = 22
            item["museumName"] = "河北博物院"
            item["exhibitionImageLink"] = StrFilter.getDoamin(response) + str(li.xpath(
                "./dl/dt/a/img/@src").extract_first())
            item["exhibitionName"] = StrFilter.filter_2(li.xpath("./dl/dd/a/text()").extract_first())
            item["exhibitionTime"] = '常设展览'
            url = StrFilter.getDoamin(response) + str(li.xpath("./dl/dt/a/@href").extract_first())
            print(url)
            yield scrapy.Request(
                url,
                callback=self.parseAnotherPage,
                meta={"item": item}
            )

    def parseAnotherPage(self, response):
        item = response.meta["item"]
        item['exhibitionIntroduction'] = StrFilter.filter_2(
            response.xpath("//*[@id='content']/div[2]/div[3]/div[2]/div[@class='text']").xpath(
                'string(.)').extract_first())
        print(item)
        yield item
