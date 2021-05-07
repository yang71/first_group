#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/4/30 14:05 
# @Author  : ana
# @File    : Collection3.py
# @Software: PyCharm

from ..items import *
from ..str_filter import *


class Collection2(scrapy.Spider):
    name = "Collection3"
    allowed_domains = ['jb.mil.cn']
    start_urls = ['http://www.jb.mil.cn/was/web/search?token=14.1499419140318.94&channelid=237727',
                  'http://www.jb.mil.cn/was/web/search?page=2&channelid=237727&token=14.1499419140318.94&perpage=12&outlinepage=10',
                  'http://www.jb.mil.cn/was/web/search?page=3&channelid=237727&token=14.1499419140318.94&perpage=12&outlinepage=10',
                  'http://www.jb.mil.cn/was/web/search?page=4&channelid=237727&token=14.1499419140318.94&perpage=12&outlinepage=10',
                  'http://www.jb.mil.cn/was/web/search?page=5&channelid=237727&token=14.1499419140318.94&perpage=12&outlinepage=10',
                  'http://www.jb.mil.cn/was/web/search?page=6&channelid=237727&token=14.1499419140318.94&perpage=12&outlinepage=10']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.DefaultMiddleware': 0,
        },
    }

    def parse(self, response, **kwargs):
        li_list = response.xpath("/html/body/div/div[1]/ul/li")
        for li in li_list:
            item = CollectionItem()
            item["museumID"] = 3
            item["museumName"] = "中国人民革命军事博物馆"
            url = str(li.xpath("./a/@href").extract_first())
            yield scrapy.Request(
                url,
                callback=self.parseAnotherPage,
                meta={"item": item}
            )

    def parseAnotherPage(self, response):
        item = response.meta["item"]
        item['collectionName'] = response.xpath("/html/body/div[4]/div/div[1]/h2/text()").extract_first()
        item['collectionImageLink'] = 'http://www.jb.mil.cn/gcww/wwjs_new/shzysq/201707/' + response.xpath(
            "/html/body/div[4]/div/div[1]/div/p[1]/img/@oldsrc").extract_first()
        item['collectionIntroduction'] = ''.join(re.sub(StrFilter.r1, "", str(
            response.xpath("/html/body/div[4]/div/div[1]/div/p[3]/text()").extract_first())).split())
        print(item)
        yield item
