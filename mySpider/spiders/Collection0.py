#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/4/30 15:38 
# @Author  : ana
# @File    : Collection0.py
# @Software: PyCharm
import logging
import time

from selenium import webdriver
from selenium.common.exceptions import JavascriptException
from selenium.webdriver.chrome.options import Options

# from ..auxiliary_files import Collection0_supporting
from ..items import *
from ..str_filter import *

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")


class Collection0(scrapy.Spider):
    name = "Collection0"
    allowed_domains = ['dpm.org.cn']
    start_urls = ['https://zm-digicol.dpm.org.cn/cultural/list?category=17',
                  'https://zm-digicol.dpm.org.cn/cultural/list?page=2&category=17',
                  'https://zm-digicol.dpm.org.cn/cultural/list?page=3&category=17',
                  'https://zm-digicol.dpm.org.cn/cultural/list?page=4&category=17',
                  'https://zm-digicol.dpm.org.cn/cultural/list?page=5&category=17',
                  'https://zm-digicol.dpm.org.cn/cultural/list?page=6&category=17',
                  'https://zm-digicol.dpm.org.cn/cultural/list?page=7&category=17',
                  'https://zm-digicol.dpm.org.cn/cultural/list?page=8&category=17',
                  'https://zm-digicol.dpm.org.cn/cultural/list?page=9&category=17',
                  'https://zm-digicol.dpm.org.cn/cultural/list?page=10&category=17',
                  'https://zm-digicol.dpm.org.cn/cultural/list?page=11&category=17',
                  'https://zm-digicol.dpm.org.cn/cultural/list?page=12&category=17',
                  'https://zm-digicol.dpm.org.cn/cultural/list?page=13&category=17',
                  'https://zm-digicol.dpm.org.cn/cultural/list?page=14&category=17',
                  'https://zm-digicol.dpm.org.cn/cultural/list?page=15&category=17',
                  'https://zm-digicol.dpm.org.cn/cultural/list?page=16&category=17',
                  'https://zm-digicol.dpm.org.cn/cultural/list?page=17&category=17',
                  'https://zm-digicol.dpm.org.cn/cultural/list?page=18&category=17',
                  'https://zm-digicol.dpm.org.cn/cultural/list?page=19&category=17',
                  'https://zm-digicol.dpm.org.cn/cultural/list?page=20&category=17',
                  'https://zm-digicol.dpm.org.cn/cultural/list?page=21&category=17',
                  'https://zm-digicol.dpm.org.cn/cultural/list?page=22&category=17',
                  'https://zm-digicol.dpm.org.cn/cultural/list?page=23&category=17',
                  'https://zm-digicol.dpm.org.cn/cultural/list?page=24&category=17',
                  'https://zm-digicol.dpm.org.cn/cultural/list?page=25&category=17',
                  'https://zm-digicol.dpm.org.cn/cultural/list?page=26&category=17',
                  'https://zm-digicol.dpm.org.cn/cultural/list?page=27&category=17',
                  'https://zm-digicol.dpm.org.cn/cultural/list?page=28&category=17',
                  'https://zm-digicol.dpm.org.cn/cultural/list?page=29&category=17',
                  'https://zm-digicol.dpm.org.cn/cultural/list?page=30&category=17',
                  'https://zm-digicol.dpm.org.cn/cultural/list?page=31&category=17',
                  'https://zm-digicol.dpm.org.cn/cultural/list?page=32&category=17',
                  'https://zm-digicol.dpm.org.cn/cultural/list?page=33&category=17',
                  'https://zm-digicol.dpm.org.cn/cultural/list?page=34&category=17',
                  'https://zm-digicol.dpm.org.cn/cultural/list?page=35&category=17',
                  'https://zm-digicol.dpm.org.cn/cultural/list?page=36&category=17',
                  'https://zm-digicol.dpm.org.cn/cultural/list?page=37&category=17',
                  'https://zm-digicol.dpm.org.cn/cultural/list?page=38&category=17',
                  'https://zm-digicol.dpm.org.cn/cultural/list?page=39&category=17',
                  'https://zm-digicol.dpm.org.cn/cultural/list?page=40&category=17',
                  ]

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.Collection0Middleware': 9527,
        }
    }

    def __init__(self):
        self.browser = webdriver.Chrome(chrome_options=chrome_options)
        super().__init__()

    def close(self, spider, reason):
        self.browser.quit()

    def parse(self, response, **kwargs):
        li_list = response.xpath("/html/body/div[2]/div[4]/div[@class='table']")
        print(len(li_list))
        for li in li_list:
            item = CollectionItem()
            item["museumID"] = 0
            item["museumName"] = "故宫博物院"
            url = str(li.xpath("./div[2]/a/@href").extract_first())
            yield scrapy.Request(
                url,
                callback=self.parseAnotherPage,
                meta={"item": item}
            )

    def parseAnotherPage(self, response):
        item = response.meta["item"]
        item['collectionName'] = response.xpath(
            "/html/body/div[1]/div/div[2]/div/div[1]/div[2]/div/h2/text()").extract_first()
        item['collectionImageLink'] = None
        iframe_id = response.xpath('//*[@id="image_iframe_id"]/@id').extract_first()

        try:
            item['collectionImageLink'] = self.browser.execute_script(
                'var images = document.getElementById("' + iframe_id
                + '").contentWindow.document.getElementsByTagName("img");'
                  'var imgURLs=new Array(images.length);'
                  'for(var i = 0;i<images.length;i++){ imgURLs[i] = images[i].src;}'
                  'return imgURLs;')[0]

        except JavascriptException as e:
            time.sleep(1)

        item['collectionIntroduction'] = StrFilter.filter(
            response.xpath("/html/body/div[1]/div").xpath(
                'string(.)').extract_first()).replace('[', '').replace(']', '').split('文字信息')[-1].split('相关信息')[
            0].replace("返回上页','故宫博物院版权所有，查看详情。", '').replace("'收','藏','相关推荐','分享'", '').replace("'相关推荐','分享'",
                                                                                                '').replace(
            "微信扫一扫：分享微信里点“发现”，扫一下二维码便可将本文分享至朋友圈。", "").replace("收藏", "")
        print(item)
        yield item
