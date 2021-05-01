#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/5/1 15:22 
# @Author  : ana
# @File    : Collection21.py
# @Software: PyCharm

from ..items import *
from ..str_filter import *


class Collection21(scrapy.Spider):
    name = "Collection21"
    allowed_domains = ['pjcmm.com']
    start_urls = ['http://www.pjcmm.com/listPro.aspx?cateid=82&page=1',
                  'http://www.pjcmm.com/listPro.aspx?cateid=82&page=2',
                  'http://www.pjcmm.com/listPro.aspx?cateid=82&page=3',
                  ]

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        }
    }

    def parse(self, response, **kwargs):
        li_list = response.xpath("/html/body/div[4]/div[2]/ul/li")
        print(len(li_list))
        for li in li_list:
            item = CollectionItem()
            item["museumID"] = 21
            item["museumName"] = "平津战役纪念馆"
            item['collectionImageLink'] = "http://www.pjcmm.com/" + str(li.xpath("./a/img/@src").extract_first())
            url = "http://www.pjcmm.com/" + str(li.xpath("./a/@href").extract_first())
            item['collectionName'] = li.xpath("./a/p/text()").extract_first()
            yield scrapy.Request(
                url,
                callback=self.parseAnotherPage,
                meta={"item": item}
            )

    def parseAnotherPage(self, response):
        item = response.meta["item"]
        item['collectionIntroduction'] = StrFilter.filter(
            response.xpath("/html/body/div[4]/div[2]").xpath('string(.)').extract_first()).replace('[', '').replace(
            ']', '').split("true});\',\'")[1].split("\\")[0]
        print(item)
        yield item
