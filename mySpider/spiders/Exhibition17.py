#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/5/7 19:15 
# @Author  : ana
# @File    : Exhibition17.py
# @Software: PyCharm


from ..items import *
from ..str_filter import *


class Exhibition17(scrapy.Spider):
    name = "Exhibition17"
    allowed_domains = ['artmuseum.tsinghua.edu.cn']
    start_urls = ['https://www.artmuseum.tsinghua.edu.cn/cpsj/zlxx/zzzl/lszl/']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.ExhibitionPipeLine': 302,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.DefaultMiddleware': 0,
        },
    }

    def parse(self, response, **kwargs):
        li_list = response.xpath("/html/body/div[4]/div[3]/div/ul/li")
        print(len(li_list))
        for li in li_list:
            item = ExhibitionItem()
            item["museumID"] = 17
            item["museumName"] = "清华大学艺术博物馆"
            item["exhibitionImageLink"] = li.xpath("./a/img/@src").extract_first()
            item["exhibitionName"] = StrFilter.filter_2(li.xpath("./div[1]/h4/a/text()").extract_first())
            item["exhibitionTime"] = StrFilter.filter_2(li.xpath("./div[1]/p/text()").extract_first())
            url = StrFilter.getDoamin(response) + '/cpsj/zlxx/zzzl/lszl/' + str(
                li.xpath("./a/@href").extract_first())[2:]
            print(url)
            yield scrapy.Request(
                url,
                callback=self.parseAnotherPage,
                meta={"item": item}
            )

    def parseAnotherPage(self, response):
        item = response.meta["item"]
        item['exhibitionIntroduction'] = StrFilter.filter_2(
            response.xpath("//dl[@class='dhy_ysj_jj']/dd").xpath('string(.)').extract_first())
        print(item)
        yield item
