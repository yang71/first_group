#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/5/2 13:54 
# @Author  : ana
# @File    : Collection42.py
# @Software: PyCharm
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from ..items import *
from ..str_filter import *

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")


class Collection42(scrapy.Spider):
    name = "Collection42"
    allowed_domains = ['wmhg.com.cn']
    start_urls = ['https://www.wmhg.com.cn/collection_list.html']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.Collection42Middleware': 9533,
        }
    }

    def __init__(self):
        self.browser = webdriver.Chrome(chrome_options=chrome_options)
        super().__init__()

    def close(self, spider, reason):
        self.browser.quit()

    def parse(self, response, **kwargs):
        li_list = response.xpath("//*[@id='datalist']/div[1]/div")
        print(len(li_list))
        for li in li_list:
            item = CollectionItem()
            item["museumID"] = 42
            item["museumName"] = "伪满皇宫博物院"
            item['collectionImageLink'] = 'https://www.wmhg.com.cn' + str(li.xpath(
                "./a/span[1]/img/@src").extract_first())
            item['collectionName'] = str(li.xpath("./a/span[2]/text()").extract_first())
            url = "https://www.wmhg.com.cn" + str(li.xpath("./a/@href").extract_first())
            yield scrapy.Request(
                url,
                callback=self.parseAnotherPage,
                meta={"item": item}
            )

    def parseAnotherPage(self, response):
        item = response.meta["item"]
        item['collectionIntroduction'] = StrFilter.filter(
            response.xpath("//div[@class='slick-cont']").xpath('string(.)').extract_first()).replace('[', '').replace(
            ']', '')
        print(item)
        yield item
