#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/5/2 12:04 
# @Author  : ana
# @File    : Collection8.py
# @Software: PyCharm
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from ..items import *
from ..str_filter import *

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")


class Collection8(scrapy.Spider):
    name = "Collection8"
    allowed_domains = ['1937china.com']
    start_urls = ['http://www.1937china.com/views/kzww/kzww_jpdc.html']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.Collection8Middleware': 9528,
        }
    }

    def __init__(self):
        self.browser = webdriver.Chrome(chrome_options=chrome_options)
        super().__init__()

    def close(self, spider, reason):
        self.browser.quit()

    def parse(self, response, **kwargs):
        li_list = response.xpath("//*[@id='main']/div[2]/div")
        print(len(li_list))
        for li in li_list:
            item = CollectionItem()
            item["museumID"] = 8
            item["museumName"] = "中国人民抗日战争纪念馆"
            item['collectionName'] = StrFilter.filter(
                li.xpath("./div[2]/div[1]/text()").extract_first()).replace('[', '').replace(']', '')
            item['collectionImageLink'] = 'http://www.1937china.com/' + str(li.xpath(
                "./div[1]/img/@src").extract_first())
            item['collectionIntroduction'] = StrFilter.filter(
                li.xpath("./div[2]/div[2]").xpath('string(.)').extract_first()).replace('[',
                                                                                        '').replace(
                ']', '')
            print(item)
            yield item
