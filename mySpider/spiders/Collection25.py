#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/5/1 16:04 
# @Author  : ana
# @File    : Collection25.py
# @Software: PyCharm

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from ..items import *
from ..str_filter import *

from ..auxiliary_files import Collection25_supporting

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")


class Collection25(scrapy.Spider):
    name = "Collection25"
    allowed_domains = ['shanximuseum.com']
    start_urls = Collection25_supporting.Collection25Supporting.startUrl

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.Collection25Middleware': 9531,
        }
    }

    def __init__(self):
        self.browser = webdriver.Chrome(chrome_options=chrome_options)
        super().__init__()

    def close(self, spider, reason):
        self.browser.quit()

    def parse(self, response, **kwargs):
        li_list = response.xpath("//*[@id='datalist']/div/div[@class='wf-item show_hide']")
        print(len(li_list))
        for li in li_list:
            item = CollectionItem()
            item["museumID"] = 25
            item["museumName"] = "山西博物院"
            item['collectionName'] = StrFilter.filter(
                li.xpath("./a/div[2]/div/text()").extract_first()).replace('[', '').replace(']', '')
            item['collectionImageLink'] = 'http://www.shanximuseum.com' + str(li.xpath(
                "./a/div[1]/img/@src").extract_first())
            url = "http://www.shanximuseum.com/" + str(li.xpath("./a/@href").extract_first())
            yield scrapy.Request(
                url,
                callback=self.parseAnotherPage,
                meta={"item": item}
            )

    def parseAnotherPage(self, response):
        item = response.meta["item"]
        item['collectionIntroduction'] = StrFilter.filter(
            response.xpath("//div[@class='collection_xx2']").xpath('string(.)').extract_first()).replace('[',
                                                                                                         '').replace(
            ']', '').replace("'分享至：'", '')
        print(item)
        yield item
