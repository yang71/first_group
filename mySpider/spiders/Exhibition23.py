#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/5/7 20:27 
# @Author  : ana
# @File    : Exhibition23.py
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


class Exhibition23(scrapy.Spider):
    name = "Exhibition23"
    allowed_domains = ['xbpjng.cn']
    start_urls = ['http://www.xbpjng.cn/PlatNews/platform.aspx?c=3f80c295-81c8-49f9-838f-b3cfce9bc5c9&z=795']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.ExhibitionPipeLine': 302,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.Exhibition23Middleware': 65538,
        },
    }

    def __init__(self):
        self.browser = webdriver.Chrome(chrome_options=chrome_options)
        super().__init__()

    def close(self, spider, reason):
        self.browser.quit()

    def parse(self, response, **kwargs):
        li_list = response.xpath("//*[@id='ctl00']/div[3]/div/div[2]//a")
        print(len(li_list))
        for li in li_list:
            item = ExhibitionItem()
            item["museumID"] = 23
            item["museumName"] = "西柏坡纪念馆"
            item["exhibitionName"] = StrFilter.filter_2(li.xpath("./text()").extract_first())
            item["exhibitionTime"] = "常设展览"
            url = str(li.xpath("./a/@href").extract_first())
            print(url)
            yield scrapy.Request(
                url,
                callback=self.parseAnotherPage,
                meta={"item": item}
            )

    def parseAnotherPage(self, response):
        item = response.meta["item"]
        item['exhibitionIntroduction'] = StrFilter.filter_2(
            response.xpath("//*[@id='lb_Content']/p[2]").xpath('string(.)').extract_first())
        item["exhibitionImageLink"] = response.xpath("//*[@id='form1']//img/@src").extract_first()
        print(item)
        yield item
