#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/5/7 18:25 
# @Author  : ana
# @File    : Exhibition14.py
# @Software: PyCharm


from ..items import *
from ..str_filter import *


class Exhibition14(scrapy.Spider):
    name = "Exhibition14"
    allowed_domains = ['printingmuseum.cn']
    start_urls = ['http://www.printingmuseum.cn/Exhibitions/PExhibitionsList/BasicExhibition#comehere']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.ExhibitionPipeLine': 302,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.DefaultMiddleware': 0,
        },
    }

    def parse(self, response, **kwargs):
        li_list = response.xpath("//*[@id='ulBaseExhibitList']/li")
        print(len(li_list))
        for li in li_list:
            item = ExhibitionItem()
            item["museumID"] = 14
            item["museumName"] = "中国印刷博物馆"
            item["exhibitionImageLink"] = li.xpath("./div[1]/img/@src").extract_first()
            item["exhibitionName"] = StrFilter.filter_2(li.xpath("./div[1]/span/h3/text()").extract_first())
            item["exhibitionTime"] = "常设展览"
            item['exhibitionIntroduction'] = StrFilter.filter_2(
                li.xpath("./div[1]/span/p/text()").extract_first())
            print(item)
            yield item
