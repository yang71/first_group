#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/5 1:55
# @Author  : 10711
# @File    : Collection150.py
# @Software: PyCharm

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from ..items import *
from ..str_filter import *
from ..auxiliary_files import Collection150_supporting

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")

class Collection150(scrapy.Spider):
    name = "Collection150"
    allowed_domains = ['gzchenjiaci.com']
    start_urls = Collection150_supporting.Collection150Supporting.startUrl

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.Collection150Middleware': 9650,
        }
    }

    def __init__(self):
        self.browser = webdriver.Chrome(chrome_options=chrome_options)
        super().__init__()

    def close(self, spider, reason):
        self.browser.quit()

    def parse(self, response, **kwargs):
        li_list = response.xpath("/html/body/div[2]/div[2]/div/div/ul/li")
        print(len(li_list))
        for li in li_list:
            item = CollectionItem()
            item["museumID"] = 150
            item["museumName"] = "广东民间工艺博物馆"
            item['collectionImageLink'] = StrFilter.getDoamin(response) + str(
                li.xpath("./a/div[1]/img/@src").extract_first())
            url = StrFilter.getDoamin(response) + str(
                li.xpath("./a/@href").extract_first())
            yield scrapy.Request(
                url,
                callback=self.parseAnotherPage,
                meta={"item": item}
            )

    def parseAnotherPage(self, response):
        item = response.meta["item"]
        item['collectionName'] = StrFilter.filter(
            response.xpath("/html/body/div[2]/div[2]/div/div/div[1]/p[2]").xpath('string(.)').extract_first())
        item['collectionIntroduction'] = StrFilter.filter(
            response.xpath("/html/body/div[2]/div[2]/div/div/div[1]/p[5]").xpath('string(.)').extract_first()) + StrFilter.filter(
            response.xpath("/html/body/div[2]/div[2]/div/div/div[1]/p[4]").xpath('string(.)').extract_first()) + StrFilter.filter(
            response.xpath("/html/body/div[2]/div[2]/div/div/div[1]/p[3]").xpath('string(.)').extract_first()) + StrFilter.filter(
            response.xpath("/html/body/div[2]/div[2]/div/div/div[1]/p[6]").xpath('string(.)').extract_first())
        print(item)
        yield(item)