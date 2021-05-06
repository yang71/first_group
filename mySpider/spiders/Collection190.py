#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/4 12:46
# @Author  : 10711
# @File    : Collection190.py
# @software: PyCharm

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

from ..items import *
from ..str_filter import *
from ..auxiliary_files import Collection190_supporting

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")


class Collection190(scrapy.Spider):
    name = "Collection190"
    allowed_domains = ['xabwy.com']
    start_urls = Collection190_supporting.Collection190Supporting.startUrl

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.Collection190Middleware': 9690,
        }
    }
    def __init__(self):
        self.browser = webdriver.Chrome(chrome_options=chrome_options)
        super().__init__()

    def close(self, spider, reason):
        self.browser.quit()

    def parse(self, response, **kwargs):
        li_list = response.xpath("//*[@id='newlist']/div")
        print(len(li_list))
        for li in li_list:
            item = CollectionItem()
            item["museumID"] = 190
            item["museumName"] = "西安博物院"
            item['collectionName'] = StrFilter.filter(
                li.xpath("./div/a").xpath('string(.)').extract_first())
            item['collectionImageLink'] = str(
                li.xpath("./a/img/@src").extract_first())
            item['collectionIntroduction'] = StrFilter.filter(
                li.xpath("./div/div[1]").xpath('string(.)').extract_first())
            print(item)
            yield(item)