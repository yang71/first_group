#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/11 20:11
# @Author  : 10711
# @File    : Exhibition172.py
# @Software: PyCharm


from ..items import *
from ..str_filter import *
from ..auxiliary_files import Exhibition172_supporting

class Exhibition172(scrapy.Spider):
    name = "Exhibition172"
    allowed_domains = ['zunyihy.cn']
    start_urls = Exhibition172_supporting.Exhibition172Supporting.startUrl

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.ExhibitionPipeLine': 302,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.DefaultMiddleware': 0,
        },
    }

    def parse(self, response, **kwargs):
        li_list = response.xpath("/html/body/div[4]/div/div[3]/div")
        print(len(li_list))
        for li in li_list:
            item = ExhibitionItem()
            item["museumID"] = 172
            item["museumName"] = "遵义会议纪念馆"
            item["exhibitionImageLink"] = StrFilter.getDoamin(response) + str(
                li.xpath("./div[1]/@style").extract_first()).replace("background:url(","").replace(") no-repeat center; background-size:cover;","")
            item["exhibitionName"] = StrFilter.filter(
                li.xpath("./a/span").xpath('string(.)').extract_first())
            item["exhibitionTime"] = "常设展览"
            item['exhibitionIntroduction'] = StrFilter.filter(
                li.xpath("./div[2]/div[2]/div/div/div[1]/div[2]/div").xpath('string(.)').extract_first())
            print(item)
            yield item