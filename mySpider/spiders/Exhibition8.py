#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/5/7 15:36 
# @Author  : ana
# @File    : Exhibition8.py
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


class Exhibition8(scrapy.Spider):
    name = "Exhibition8"
    allowed_domains = ['1937china.com']
    start_urls = ['http://www.1937china.com/views/kzzl/zlzs_ztzl.html']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.ExhibitionPipeLine': 302,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.Exhibition8Middleware': 65536,
        },
    }

    def __init__(self):
        self.browser = webdriver.Chrome(chrome_options=chrome_options)
        super().__init__()

    def close(self, spider, reason):
        self.browser.quit()

    def parse(self, response, **kwargs):
        li_list = response.xpath("//*[@id='kzzl_ztzl']/div/div[1]")
        print(len(li_list))
        for li in li_list:
            item = ExhibitionItem()
            item["museumID"] = 8
            item["museumName"] = "中国人民抗日战争纪念馆"
            item["exhibitionImageLink"] = StrFilter.getDoamin(response) + str(li.xpath(
                "./div[1]//li/article/div[1]/div[2]/a//img/@src").extract_first())
            item["exhibitionName"] = StrFilter.filter_2(
                li.xpath("./div[1]//li/article/div[1]/div[1]/h2/a/span/text()").extract_first())
            item["exhibitionTime"] = "常设展览"
            item['exhibitionIntroduction'] = StrFilter.filter_2(
                response.xpath("./div[1]//li/article/div[1]/div[1]/div[3]").xpath('string(.)').extract_first())
            print(item)
            yield item
