#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/11 14:11
# @Author  : 10711
# @File    : Exhibition116.py
# @Software: PyCharm


from ..items import *
from ..str_filter import *
from ..auxiliary_files import Exhibition116_supporting

class Exhibition116(scrapy.Spider):
    name = "Exhibition116"
    allowed_domains = ['zbstcbwg.cn']
    start_urls = Exhibition116_supporting.Exhibition116Supporting.startUrl

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.ExhibitionPipeLine': 302,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.DefaultMiddleware': 0,
        },
    }

    def parse(self, response, **kwargs):
        li_list = response.xpath("//*[@id='datalist']/div/div")
        print(len(li_list))
        for li in li_list:
            item = ExhibitionItem()
            item["museumID"] = 116
            item["museumName"] = "淄博市陶瓷博物馆"

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
            response.xpath("/html/body/div[4]/div[1]/div/div[2]/div[3]/img/@src").extract_first())
        item["exhibitionName"] = StrFilter.filter(
            response.xpath("/html/body/div[4]/div[1]/div/div[2]/div[1]/div").xpath('string(.)').extract_first())
        item['exhibitionIntroduction'] = StrFilter.filter(
            response.xpath("/html/body/div[4]/div[1]").xpath('string(.)').extract_first())
        item["exhibitionTime"] = "临时展览"
        print(item)
        yield item