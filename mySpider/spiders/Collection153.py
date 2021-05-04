#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/5 0:47
# @Author  : 10711
# @File    : Collection153.py
# @Software: PyCharm

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from ..items import *
from ..str_filter import *
from ..auxiliary_files import Collection153_supporting

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")

#有点问题，无法运行，待更新
class Collection153(scrapy.Spider):
    name = "Collection153"
    allowed_domains = ['ypzz.cn']
    start_urls = Collection153_supporting.Collection153Supporting.startUrl

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.Collection153Middleware': 9653,
        }
    }

    def __init__(self):
        self.browser = webdriver.Chrome(chrome_options=chrome_options)
        super().__init__()

    def close(self, spider, reason):
        self.browser.quit()

    def parse(self, response, **kwargs):
        li_list = response.xpath("//*[@id='viewlist-target-ww']/li")
        print(len(li_list))
        for li in li_list:
            item = CollectionItem()
            item["museumID"] = 153
            item["museumName"] = "鸦片战争博物馆"
            item['collectionName'] = StrFilter.filter(
                li.xpath("./a/div[2]/h4").xpath('string(.)').extract_first())
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
            response.xpath("//*[@id='wwDetail-target']/ul/li/div[2]/p[2]").xpath('string(.)').extract_first())
        print(item)
        yield(item)