#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/5/7 16:26 
# @Author  : ana
# @File    : Exhibition11.py
# @Software: PyCharm

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from ..items import *
from ..str_filter import *

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument('log-level=0')


class Exhibition11(scrapy.Spider):
    name = "Exhibition11"
    allowed_domains = ['ciae.com.cn']
    start_urls = ['https://www.ciae.com.cn/plan/zh/exhibition.html']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.ExhibitionPipeLine': 302,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.Exhibition11Middleware': 65537,
        },
    }

    def __init__(self):
        self.browser = webdriver.Chrome(chrome_options=chrome_options)
        super().__init__()

    def close(self, spider, reason):
        self.browser.quit()

    def parse(self, response, **kwargs):
        # li_list = response.xpath("//div[@class='wrap']/div[@class='list']/div[@class='item']")
        li_list = response.xpath("//*[@id='ajax-list']/div[1]/div[1]")
        print(len(li_list))
        for li in li_list:
            item = ExhibitionItem()
            item["museumID"] = 11
            item["museumName"] = "中国农业博物馆"
            item["exhibitionImageLink"] = None
            item["exhibitionName"] = StrFilter.filter_2(li.xpath("./div[1]/a/text()").extract_first())
            item["exhibitionTime"] = StrFilter.filter_2(li.xpath("./div[2]/span[1]/text()").extract_first())
            item['exhibitionIntroduction'] = StrFilter.filter_2(li.xpath("./div[2]/span[2]/text()").extract_first())
            print(item)
            yield item
