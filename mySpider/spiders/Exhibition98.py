#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/11 14:11
# @Author  : 10711
# @File    : Exhibition98.py
# @Software: PyCharm

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


from ..items import *
from ..str_filter import *
from ..auxiliary_files import Exhibition98_supporting

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument('log-level=0')


class Exhibition98(scrapy.Spider):
    name = "Exhibition98"
    allowed_domains = ['bdsrjng.cn']
    start_urls = Exhibition98_supporting.Exhibition98Supporting.startUrl

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.ExhibitionPipeLine': 302,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.Exhibition11Middleware': 65545,
        },
    }

    def __init__(self):
        self.browser = webdriver.Chrome(chrome_options=chrome_options)
        super().__init__()

    def close(self, spider, reason):
        self.browser.quit()

    def parse(self, response, **kwargs):
            item = ExhibitionItem()
            item["museumID"] = 98
            item["museumName"] = "八大山人纪念馆"
            item["exhibitionName"] = StrFilter.filter(
                response.xpath("//*[@id='mm-0']/div[4]/div[2]/div[3]/div[2]/section[2]").xpath('string(.)').extract_first())
            item["exhibitionImageLink"] = StrFilter.getDoamin(response) + str(
                response.xpath("//*[@id='mm-0']/div[4]/div[2]/div[3]/p[3]/span/img/@src").extract_first())
            item['exhibitionIntroduction'] = StrFilter.filter(
                response.xpath("//*[@id='mm-0']/div[4]/div[2]/div[3]").xpath('string(.)').extract_first())
            item["exhibitionTime"] = "常设展览"
            print(item)
            yield item