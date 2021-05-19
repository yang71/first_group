#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/11 14:11
# @Author  : 10711
# @File    : Exhibition67.py
# @Software: PyCharm

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from ..items import *
from ..str_filter import *
from ..auxiliary_files import Exhibition67_supporting

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument('log-level=0')

class Exhibition67(scrapy.Spider):
    name = "Exhibition67"
    allowed_domains = ['csmuseum.cn']
    start_urls = Exhibition67_supporting.Exhibition67Supporting.startUrl

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.ExhibitionPipeLine': 302,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.Exhibition67Middleware': 4541,
        },
    }
    def __init__(self):
        self.browser = webdriver.Chrome(chrome_options=chrome_options)
        super().__init__()

    def close(self, spider, reason):
        self.browser.quit()

    def parse(self, response, **kwargs):
            item = ExhibitionItem()
            item["museumID"] = 67
            item["museumName"] = "常熟博物馆"
            item["exhibitionImageLink"] = StrFilter.getDoamin(response) + str(
                response.xpath("//*[@id='app']/div[2]/div[2]/img/@src").extract_first())
            item["exhibitionName"] = StrFilter.filter(
                response.xpath("//*[@id='app']/div[2]/div[2]/p[1]").xpath('string(.)').extract_first())
            item["exhibitionTime"] = StrFilter.filter(
                response.xpath("//*[@id='app']/div[2]/div[2]/p[2]").xpath('string(.)').extract_first())
            item['exhibitionIntroduction'] = StrFilter.filter(
                response.xpath("//*[@id='app']/div[2]/div[2]").xpath('string(.)').extract_first())
            print(item)
            yield item