#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/11 12:49
# @Author  : 10711
# @File    : Exhibition200.py
# @Software: PyCharm

from ..items import *
from ..str_filter import *

class Exhibiton0(scrapy.Spider):
    name = "Exhibition0"
    allowed_domains = ['dpm.org.cn']
    start_urls = ['https://www.dpm.org.cn/shows.html']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.ExhibitionPipeLine': 302,
        }
    }

    def parse(self, response, **kwargs):
        # li_list = response.xpath("//div[@id='temporary_5']/div[@class='temporary5']")
        # for li in li_list:
        item = ExhibitionItem()
        item["museumID"] = 0
        item["museumName"] = "故宫博物院"
        item["exhibitionName"] = "test"
        item["exhibitionImageLink"] = "test"
        item["exhibitionTime"] = 123
        item["exhibitionIntroduction"] = 456
        print(item)
        yield item