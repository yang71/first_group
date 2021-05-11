#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/5/7 18:51 
# @Author  : ana
# @File    : Exhibition15.py
# @Software: PyCharm


from ..items import *
from ..str_filter import *


class Exhibition15(scrapy.Spider):
    name = "Exhibition15"
    allowed_domains = ['cnfm.org.cn']
    start_urls = ['http://www.cnfm.org.cn/ybzl/ztzl.shtml']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.ExhibitionPipeLine': 302,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.DefaultMiddleware': 0,
        },
    }

    def parse(self, response, **kwargs):
        li_list = response.xpath(
            "/html/body/table[1]//tr/td/table[2]//tr/td/table//tr[3]/td[2]/table//tr/td/table//tr[1]/td")
        print(len(li_list))
        for li in li_list:
            item = ExhibitionItem()
            item["museumID"] = 15
            item["museumName"] = "北京电影博物馆"
            item["exhibitionImageLink"] = StrFilter.getDoamin(response) + li.xpath(
                ".//img/@src").extract_first()
            item["exhibitionName"] = StrFilter.filter_2(li.xpath(".//p/a/text()").extract_first())
            item["exhibitionTime"] = None
            item['exhibitionIntroduction'] = None
            print(item)
            yield item
