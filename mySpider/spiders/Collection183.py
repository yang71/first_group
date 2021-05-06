#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/4 15:05
# @Author  : 10711
# @File    : Collection183.py
# @Software: PyCharm


from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from ..items import *
from ..str_filter import *
from ..auxiliary_files import Collection183_supporting

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")


class Collection183(scrapy.Spider):
    name = "Collection183"
    allowed_domains = ['tibetmuseum.com.cn']
    start_urls = Collection183_supporting.Collection183Supporting.startUrl

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.Collection183Middleware': 9683,
        }
    }

    def __init__(self):
        self.browser = webdriver.Chrome(chrome_options=chrome_options)
        super().__init__()

    def close(self, spider, reason):
        self.browser.quit()

    def parse(self, response, **kwargs):
        item = CollectionItem()
        item["museumID"] = 183
        item["museumName"] = "西藏博物馆"
        item['collectionName'] = StrFilter.filter(
            response.xpath("//*[@class='p_title']").xpath('string(.)').extract_first())
        item['collectionImageLink'] = str(
            response.xpath("//*[@id='app']/div/div[2]/div/div[2]/div/div/div/div/img/@src").extract_first())
        item['collectionIntroduction'] = StrFilter.filter(
            response.xpath("//*[@id='app']/div/div[2]/div/div[3]/div/p[3]/p[1]").xpath('string(.)').extract_first())
        print(item)
        yield(item)