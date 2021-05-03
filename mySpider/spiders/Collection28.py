#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/5/2 15:20 
# @Author  : ana
# @File    : Collection28.py
# @Software: PyCharm

from ..items import *
from ..str_filter import *


class Collection28(scrapy.Spider):
    name = "Collection28"
    allowed_domains = ['baike.baidu.com']
    start_urls = [
        'https://baike.baidu.com/item/%E5%A4%A7%E5%90%8C%E5%B8%82%E5%8D%9A%E7%89%A9%E9%A6%86/1777948?fr=aladdin']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        }
    }

    def parse(self, response, **kwargs):
        # t_list = response.xpath(
        #     "/html/body/div[3]/div[2]/div/div[1]/table[5]|html/body/div[3]/div[2]/div/div[1]/table[6]|html/body/div[3]/div[2]/div/div[1]/table[7]")
        t_list = [response.xpath("/html/body/div[3]/div[2]/div/div[1]/table[5]"),
                  response.xpath("/html/body/div[3]/div[2]/div/div[1]/table[6]"),
                  response.xpath("/html/body/div[3]/div[2]/div/div[1]/table[7]")]
        print(len(t_list))
        for t in t_list:
            li_list = t.xpath(".//tr")
            print(len(li_list))
            for li in li_list:
                item = CollectionItem()
                item["museumID"] = 28
                item["museumName"] = "大同博物馆"
                item['collectionName'] = StrFilter.filter(
                    li.xpath(".//td[1]/div[1]/b/text()").extract_first()).replace('[', '').replace(']', '')
                item['collectionIntroduction'] = StrFilter.filter(
                    li.xpath(".//td[1]/div[2]/text()").extract_first()).replace('[',
                                                                                '').replace(
                    ']', '')
                item['collectionImageLink'] = 'https://baike.baidu.com' + str(li.xpath(
                    ".//td[2]/div[1]/div[1]/a/@href").extract_first())
                print(item)
                yield item
