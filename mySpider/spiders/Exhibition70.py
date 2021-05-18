#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/11 14:11
# @Author  : 10711
# @File    : Exhibition70.py
# @Software: PyCharm

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from ..items import *
from ..str_filter import *
from ..auxiliary_files import Exhibition70_supporting

class Exhibition70(scrapy.Spider):
    name = "Exhibition70"
    allowed_domains = ['zmnh.com']
    start_urls = Exhibition70_supporting.Exhibition70Supporting.startUrl

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.ExhibitionPipeLine': 302,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.Exhibition11Middleware': 65542,
        },
    }


    def parse(self, response, **kwargs):
        li_list = response.xpath("//*[@id='app']/div/div[2]/div[2]/div[3]/div/div/div[1]/div")
     #   print(len(li_list))
        for li in li_list:
            item = ExhibitionItem()
            item["museumID"] = 70
            item["museumName"] = "浙江自然博物院"
            item["exhibitionName"] = StrFilter.filter(
                li.xpath("./div[1]").xpath('string(.)').extract_first())
            item["exhibitionImageLink"] = StrFilter.getDoamin(response) + str(
                li.xpath("./a/img/@src").extract_first())
            item['exhibitionIntroduction'] = StrFilter.filter(
                li.xpath("./div[2]/p").xpath('string(.)').extract_first())
            item["exhibitionTime"] = "常设展览"
