#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/5/7 19:38 
# @Author  : ana
# @File    : Exhibition19.py
# @Software: PyCharm


from ..items import *
from ..str_filter import *


class Exhibition19(scrapy.Spider):
    name = "Exhibition19"
    allowed_domains = ['tjnhm.com']
    start_urls = ['https://www.tjnhm.com/index.php?p=zlxx&c_id=5&lanmu=2',
                  'https://www.tjnhm.com/index.php?p=zlxx&c_id=5&lanmu=2&page=2',
                  'https://www.tjnhm.com/index.php?p=zlxx&c_id=5&lanmu=2&page=2',
                  'https://www.tjnhm.com/index.php?p=zlxx&c_id=5&lanmu=2&page=2', ]

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.ExhibitionPipeLine': 302,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.DefaultMiddleware': 0,
        },
    }

    def parse(self, response, **kwargs):
        li_list = response.xpath("//*[@id='news_content']/div[@class='pro']")
        print(len(li_list))
        for li in li_list:
            item = ExhibitionItem()
            item["museumID"] = 19
            item["museumName"] = "天津自然博物馆"
            item["exhibitionImageLink"] = StrFilter.getDoamin(response) + '/' + str(li.xpath(
                "./a[1]/img/@src").extract_first())
            item["exhibitionName"] = StrFilter.filter_2(li.xpath("./a[2]/text()").extract_first())
            item["exhibitionTime"] = '常设展览'
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
            response.xpath("//*[@id='aboutus_text']").xpath('string(.)').extract_first())
        print(item)
        yield item
