#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/4 23:29
# @Author  : 10711
# @File    : Collection164.py
# @Software: PyCharm

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from ..items import *
from ..str_filter import *
from ..auxiliary_files import Collection164_supporting

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument('log-level=3')

class Collection164(scrapy.Spider):
    name = "Collection164"
    allowed_domains = ['cddfct.com']
    start_urls = Collection164_supporting.Collection164Supporting.startUrl

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.Collection164Middleware': 9664,
        }
    }

    def __init__(self):
        self.browser = webdriver.Chrome(chrome_options=chrome_options)
        super().__init__()

    def close(self, spider, reason):
        self.browser.quit()

    def parse(self, response, **kwargs):
        li_list = response.xpath("/html/body/div[2]/div[2]/div[1]/div[2]/ul/li")
        print(len(li_list))
        for li in li_list:
            item = CollectionItem()
            item["museumID"] = 164
            item["museumName"] = "成都杜甫草堂博物馆"
            item['collectionImageLink'] = str(
                li.xpath("./div[1]/a/img/@src").extract_first())
            url = StrFilter.getDoamin(response) + str(
                li.xpath("./div[1]/a/@href").extract_first())
            yield scrapy.Request(
                url,
                callback=self.parseAnotherPage,
                meta={"item": item}
            )

    def parseAnotherPage(self, response):
        item = response.meta["item"]
        item['collectionName'] = StrFilter.filter(
            response.xpath("//*[@id='simTestContent']/h1").xpath('string(.)').extract_first())
        item['collectionIntroduction'] = StrFilter.filter(
            response.xpath("//*[@id='simTestContent']/div/span").xpath('string(.)').extract_first())
        print(item)
        yield(item)