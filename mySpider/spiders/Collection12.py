#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/5/1 10:13 
# @Author  : ana
# @File    : Collection12.py
# @Software: PyCharm

from ..items import *
from ..str_filter import *
from ..auxiliary_files import Collection12_supporting


class Collection12(scrapy.Spider):
    name = "Collection12"
    allowed_domains = ['bjp.org.cn']
    start_urls = Collection12_supporting.Collection12Supporting.startUrl

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        }
    }

    def parse(self, response, **kwargs):
        li_list = response.xpath("/html/body/div[3]/div[2]/div[3]/div[2]/div/ul/li")
        for li in li_list:
            item = CollectionItem()
            item["museumID"] = 12
            item["museumName"] = "北京天文馆"
            item['collectionName'] = li.xpath("./a/div[2]/h3/text()").extract_first()
            item['collectionIntroduction'] = StrFilter.filter(li.xpath("./a/div[2]/p/text()").extract_first()).replace(
                '[', '').replace(']', '')
            item['collectionImageLink'] = 'http://www.bjp.org.cn' + str(li.xpath(
                "./a/div[1]/div/div/img[2]/@src").extract_first())
            print(item)
            yield item
