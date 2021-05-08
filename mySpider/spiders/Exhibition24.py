#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/5/7 22:27 
# @Author  : ana
# @File    : Exhibition24.py
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


class Exhibition24(scrapy.Spider):
    name = "Exhibition24"
    allowed_domains = ['hdmuseum.org']
    start_urls = ['https://www.hdmuseum.org/Home/clzl_list?type=1']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.ExhibitionPipeLine': 302,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.Exhibition24Middleware': 65539,
        },
    }

    def __init__(self):
        self.browser = webdriver.Chrome(chrome_options=chrome_options)
        super().__init__()

    def close(self, spider, reason):
        self.browser.quit()

    def parse(self, response, **kwargs):
        li_list = response.xpath("//*[@id='list']/ul/li")
        print(len(li_list))
        for li in li_list:
            item = ExhibitionItem()
            item["museumID"] = 24
            item["museumName"] = "邯郸博物馆"
            item["exhibitionImageLink"] = StrFilter.getDoamin(response) + '/' + str(li.xpath(
                "./a/div[1]/img/@src").extract_first())
            item["exhibitionName"] = StrFilter.filter_2(li.xpath("./a/h2/text()").extract_first())
            item["exhibitionTime"] = "常设展览"
            url = StrFilter.getDoamin(response) + '/' + str(li.xpath("./a/@href").extract_first())
            print(url)
            yield scrapy.Request(
                url,
                callback=self.parseAnotherPage,
                meta={"item": item}
            )

    def parseAnotherPage(self, response):
        item = response.meta["item"]
        item['exhibitionIntroduction'] = StrFilter.filter_2(
            response.xpath("//div[@class='about-content']").xpath('string(.)').extract_first())
        print(item)
        yield item
