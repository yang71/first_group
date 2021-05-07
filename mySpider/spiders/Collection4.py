#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/4/30 18:27 
# @Author  : ana
# @File    : Collection4.py
# @Software: PyCharm

from ..items import *
from ..str_filter import *


class Collection4(scrapy.Spider):
    name = "Collection4"
    allowed_domains = ['casc-spacemuseum.com']
    start_urls = ['http://www.casc-spacemuseum.com/basic-display.aspx']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.DefaultMiddleware': 0,
        },
    }

    def parse(self, response, **kwargs):
        item = CollectionItem()
        item["museumID"] = 4
        item["museumName"] = "中国航天博物馆"
        item['collectionName'] = "“长征”系列运载火箭的实物及模型"
        item['collectionImageLink'] = 'http://www.casc-spacemuseum.com/' + response.xpath(
            "//*[@id='right']/div[2]/p[2]/img/@src").extract_first()
        item[
            'collectionIntroduction'] = "卫星区中排列着“风云一号”、“东方红一号”、“东方红二号”等10颗吕类卫星。大厅西部依次排放着运载火箭发动机系列，这是运载火箭的心脏。除此之外，在这里还可以领略到自天外归来的返回式卫星回收舱实物的勃勃英姿，欣赏到著名的“长征二号”捆绑式火箭发射澳星飞行全过程模拟演示的壮观场面。"
        print(item)
        yield item
