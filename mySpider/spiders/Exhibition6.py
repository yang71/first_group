#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/5/7 15:01 
# @Author  : ana
# @File    : Exhibition6.py
# @Software: PyCharm


from ..items import *
from ..str_filter import *


class Exhibition6(scrapy.Spider):
    name = "Exhibition6"
    allowed_domains = ['capitalmuseum.org.cn']
    start_urls = ['http://www.capitalmuseum.org.cn/zlxx/ztyscl.htm']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.ExhibitionPipeLine': 302,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.DefaultMiddleware': 0,
        },
    }

    def parse(self, response, **kwargs):
        li_list = response.xpath("//*[@id='__']//tr[2]/td/table[@width='560']")
        print(len(li_list))
        for li in li_list:
            item = ExhibitionItem()
            item["museumID"] = 6
            item["museumName"] = "首都博物馆"
            item["exhibitionImageLink"] = StrFilter.getDoamin(response) + 'zlxx/' + li.xpath(
                ".//tr[2]/td[1]/img/@src").extract_first()
            item["exhibitionName"] = StrFilter.filter_2(
                li.xpath(".//tr[2]/td[3]/table[1]//tr[1]//td/text()").extract_first())
            item["exhibitionTime"] = "常设展览"
            item['exhibitionIntroduction'] = StrFilter.filter_2(
                response.xpath(".//tr[2]/td[3]/table[1]//tr[3]/td[1]").xpath('string(.)').extract_first())
            print(item)
            yield item
