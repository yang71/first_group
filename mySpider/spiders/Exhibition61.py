#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/11 13:47
# @Author  : 10711
# @File    : Exhibition61.py
# @Software: PyCharm

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from ..items import *
from ..str_filter import *
from ..auxiliary_files import Exhibition61_supporting

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument('log-level=0')

class Exhibition61(scrapy.Spider):
    name = "Exhibition61"
    allowed_domains = ['czmuseum.com']
    start_urls = Exhibition61_supporting.Exhibition61Supporting.startUrl

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.ExhibitionPipeLine': 302,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.Exhibition11Middleware': 65540,
        },
    }

    def __init__(self):
        self.browser = webdriver.Chrome(chrome_options=chrome_options)
        super().__init__()

    def close(self, spider, reason):
        self.browser.quit()

    def parse(self, response, **kwargs):
            item = ExhibitionItem()
            item["museumID"] = 61
            item["museumName"] = "常州博物馆"
            item["exhibitionImageLink"] = StrFilter.getDoamin(response) + str(
                response.xpath("//*[@id='app']/div/div[2]/div[2]/div[2]/div[2]/div[6]/div/div[2]/div[4]/p[4]/a[2]/img/@src").extract_first())
            item["exhibitionName"] = StrFilter.filter(
                response.xpath("//*[@id='app']/div/div[2]/div[2]/div[2]/div[2]/div[6]/div/div[2]/div[1]").xpath('string(.)').extract_first())
            item["exhibitionIntroduction"] = StrFilter.filter(
                response.xpath("//*[@id='app']/div/div[2]/div[2]/div[2]/div[2]/div[6]/div/div[2]/div[4]").xpath('string(.)').extract_first())
            item['exhibitionTime'] = "常设展览"
            print(item)
            yield item