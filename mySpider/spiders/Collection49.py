#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/5/1 19:06 
# @Author  : ana
# @File    : Collection49.py
# @Software: PyCharm
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from ..items import *
from ..str_filter import *

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")

# 要多次才能成功
class Collection49(scrapy.Spider):
    name = "Collection49"
    allowed_domains = ['shanghaimuseum.net']
    start_urls = [
        'https://www.shanghaimuseum.net/mu/frontend/pg/collection/antique?antiqueType1Code=CP_HIGH_CLASS_TYPE_1']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.Collection49Middleware': 9534,
        }
    }

    def __init__(self):
        self.browser = webdriver.Chrome(chrome_options=chrome_options)
        super().__init__()

    def close(self, spider, reason):
        self.browser.quit()

    def parse(self, response, **kwargs):
        li_list = response.xpath("//*[@id='list1']/li")
        print(len(li_list))
        for li in li_list:
            item = CollectionItem()
            item["museumID"] = 49
            item["museumName"] = "上海博物馆"
            item['collectionImageLink'] = 'https://www.shanghaimuseum.net/mu' + str(li.xpath(
                ".//img/@src").extract_first())
            item['collectionName'] = StrFilter.filter(
                li.xpath("./div[1]/div[2]/text()").extract_first()).replace('[', '').replace(']', '')
            url = "https://www.shanghaimuseum.net/mu" + str(li.xpath("./div[1]/div[1]/a/@href").extract_first())
            print(url)
            yield scrapy.Request(
                url,
                callback=self.parseAnotherPage,
                meta={"item": item}
            )

    # 爬不到介绍,虽然链接正确但是spider进不去,图片也显示不了
    def parseAnotherPage(self, response):
        item = response.meta["item"]
        item['collectionIntroduction'] = StrFilter.filter(
            response.xpath("//*[@id='main-content']").xpath('string(.)').extract_first()).replace('[',
                                                                                                  '').replace(
            ']', '')

        item['collectionIntroduction'] = item['collectionName']
        print(item)
        yield item
