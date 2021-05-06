#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/4 16:41
# @Author  : 10711
# @File    : Collection172.py
# @Software: PyCharm

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from ..items import *
from ..str_filter import *
from ..auxiliary_files import Collection172_supporting

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")

class Collection172(scrapy.Spider):
    name = "Collection172"
    allowed_domains = ['zunyihy.cn']
    start_urls = Collection172_supporting.Collection172Supporting.startUrl

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.Collection172Middleware': 9672,
        }
    }

    def __init__(self):
        self.browser = webdriver.Chrome(chrome_options=chrome_options)
        super().__init__()

    def close(self, spider, reason):
        self.browser.quit()

    def parse(self, response, **kwargs):
        li_list = response.xpath("//*[@id='list_wenchuang']/div")
        print(len(li_list))
        for li in li_list:
            item = CollectionItem()
            item["museumID"] = 172
            item["museumName"] = "遵义会议纪念馆"
            item['collectionName'] = StrFilter.filter(
                li.xpath("./a/div[2]").xpath('string(.)').extract_first())
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
        item['collectionIntroduction'] = StrFilter.filter(
            response.xpath("//div[@class='situation_1']").xpath('string(.)').extract_first())
        print(item)
        yield(item)