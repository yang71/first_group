#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/11 14:11
# @Author  : 10711
# @File    : Exhibition106.py
# @Software: PyCharm


from ..items import *
from ..str_filter import *
from ..auxiliary_files import Exhibition106_supporting

class Exhibition106(scrapy.Spider):
    name = "Exhibition106"
    allowed_domains = ['qingzhoumuseum.cn']
    start_urls = Exhibition106_supporting.Exhibition106Supporting.startUrl

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.ExhibitionPipeLine': 302,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.DefaultMiddleware': 0,
        },
    }

    def parse(self, response, **kwargs):
        li_list = response.xpath("/html/body/div[2]/table/tbody/tr[4]/td/table")
        print(len(li_list))
        for li in li_list:
            item = ExhibitionItem()
            item["museumID"] = 106
            item["museumName"] = "青州博物馆"
            item["exhibitionName"] = StrFilter.filter(
                li.xpath("./tbody/tr[1]/td[2]/a/span").xpath('string(.)').extract_first())
            item["exhibitionImageLink"] = StrFilter.getDoamin(response) + str(
               li.xpath("./tbody/tr[1]/td[1]/a/img/@src").extract_first())

            t=str(
                li.xpath("./tbody/tr[1]/td[2]/a/@href").extract_first())
            t1=t.replace('./2019','/2019')
            url = StrFilter.getDoamin(response) + "/zl/jbcl"+t1
            print(url)
            yield scrapy.Request(
                url,
                callback=self.parseAnotherPage,
                meta={"item": item}
            )

    def parseAnotherPage(self, response):
        item = response.meta["item"]
        item['exhibitionIntroduction'] = StrFilter.filter(
            response.xpath("/html/body/div[2]/table/tbody/tr[4]/td/div/p[2]").xpath('string(.)').extract_first())
        item["exhibitionTime"] = "常设展览"
        print(item)
        yield item