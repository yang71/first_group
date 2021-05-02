#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/5/1 17:06 
# @Author  : ana
# @File    : Collection33.py
# @Software: PyCharm
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from ..items import *
from ..str_filter import *

from ..auxiliary_files import Collection33_supporting

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")


class Collection33(scrapy.Spider):
    name = "Collection33"
    allowed_domains = ['cfbwg.org.cn']
    start_urls = Collection33_supporting.Collection33Supporting.startUrl
    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.Collection33Middleware': 9532,
        }
    }

    def __init__(self):
        self.browser = webdriver.Chrome(chrome_options=chrome_options)
        super().__init__()

    def close(self, spider, reason):
        self.browser.quit()

    def parse(self, response, **kwargs):
        li_list = response.xpath("/html/body/div[3]/ul/li")
        print(len(li_list))
        for li in li_list:
            item = CollectionItem()
            item["museumID"] = 33
            item["museumName"] = "赤峰博物馆"
            item['collectionName'] = StrFilter.filter(
                li.xpath("./a/div[2]/text()").extract_first()).replace('[', '').replace(']', '')
            item['collectionImageLink'] = str(li.xpath(
                "./a/div[1]/img/@src").extract_first())
            url = "http://www.cfbwg.org.cn/" + str(li.xpath("./a/@href").extract_first())
            yield scrapy.Request(
                url,
                callback=self.parseAnotherPage,
                meta={"item": item}
            )

    def parseAnotherPage(self, response):
        item = response.meta["item"]
        item['collectionIntroduction'] = StrFilter.filter(
            response.xpath("/html/body/div[2]/div/div[2]/div[2]").xpath('string(.)').extract_first()).replace('[',
                                                                                                              '').replace(
            ']', '')
        print(item)
        yield item
