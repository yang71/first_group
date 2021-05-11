#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/5/7 10:42 
# @Author  : ana
# @File    : Exhibition0.py
# @Software: PyCharm

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from ..items import *
from ..str_filter import *

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument('log-level=3')


class Exhibition0(scrapy.Spider):
    name = "Exhibition0"
    allowed_domains = ['dpm.org.cn']
    start_urls = ['https://www.dpm.org.cn/classify/exhibition.html']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.ExhibitionPipeLine': 302,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.Exhibition0Middleware': 65535,
        },
    }

    def __init__(self):
        self.browser = webdriver.Chrome(chrome_options=chrome_options)
        super().__init__()

    def close(self, spider, reason):
        self.browser.quit()

    def parse(self, response, **kwargs):
        li_list = response.xpath("//*[@id='lists']/div[1]/div/div")
        print(len(li_list))
        for li in li_list:
            item = ExhibitionItem()
            item["museumID"] = 0
            item["museumName"] = "故宫博物院"
            item["exhibitionImageLink"] = StrFilter.getDoamin(response) + li.xpath(
                "./div[1]/a/img/@src").extract_first()
            item["exhibitionName"] = StrFilter.filter_2(li.xpath("./div[2]/div[1]/div[1]/a/text()").extract_first())
            item["exhibitionTime"] = StrFilter.filter_2(li.xpath("./div[2]/div[1]/div[2]/p[2]/text()").extract_first())
            url = str(li.xpath("./div[1]/a/@href").extract_first())
            print(url)
            yield scrapy.Request(
                url,
                callback=self.parseAnotherPage,
                meta={"item": item}
            )

    def parseAnotherPage(self, response):
        item = response.meta["item"]
        item['exhibitionIntroduction'] = StrFilter.filter_2(
            response.xpath("/html/body/div/div[3]/div[1]/div/div[3]/div/p[3]/text()").extract_first())
        print(item)
        yield item
