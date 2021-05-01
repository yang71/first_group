#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/5/1 10:13 
# @Author  : ana
# @File    : Collection11.py
# @Software: PyCharm

from ..items import *
from ..str_filter import *


class Collection11(scrapy.Spider):
    name = "Collection11"
    allowed_domains = ['bjp.org.cn']
    start_urls = ['http://www.bjp.org.cn/kxyj/zpzs/szl/list.shtml']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        }
    }

    def parse(self, response, **kwargs):
        li_list = response.xpath("/html/body/div[3]/div[2]/div[3]/div[2]/div/ul/li")
        for li in li_list:
            item = CollectionItem()
            item["museumID"] = 11
            item["museumName"] = "北京天文馆"
            item['collectionName'] = li.xpath("./a/div[2]/h3/text()").extract_first()
            item['collectionIntroduction'] = StrFilter.filter(li.xpath("./a/div[2]/p/text()").extract_first()).replace(
                '[', '').replace(']', '')
            item['collectionImageLink'] = 'http://www.bjp.org.cn' + str(li.xpath(
                "./a/div[1]/div/div/img[2]/@src").extract_first())
            print(item)
            yield item
