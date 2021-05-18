#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/11 14:11
# @Author  : 10711
# @File    : Exhibition89.py
# @Software: PyCharm


from ..items import *
from ..str_filter import *
from ..auxiliary_files import Exhibition89_supporting

class Exhibition89(scrapy.Spider):
    name = "Exhibition89"
    allowed_domains = ['gthyjng.com','mp.weixin.qq.com']
    start_urls = Exhibition89_supporting.Exhibition89Supporting.startUrl

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.ExhibitionPipeLine': 302,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.DefaultMiddleware': 0,
        },
    }

    def parse(self, response, **kwargs):
        li_list = response.xpath("/html/body/div[4]/div/div[2]/div[2]/ul/li")
        print(len(li_list))
        for li in li_list:
            item = ExhibitionItem()
            item["museumID"] = 89
            item["museumName"] = "古田会议纪念馆"
            item["exhibitionName"] = StrFilter.filter(
                li.xpath("./h1").xpath('string(.)').extract_first())

            url = StrFilter.filter(
                li.xpath("./p/a/@href").extract_first())
            print(url)
            yield scrapy.Request(
                url,
                callback=self.parseAnotherPage,
                meta={"item": item}
            )

    def parseAnotherPage(self, response):
        item = response.meta["item"]
        item["exhibitionImageLink"] = StrFilter.getDoamin(response) + str(
            response.xpath("//*[@id='js_content']/section/section[3]/section/img/@src").extract_first())
        item['exhibitionIntroduction'] = StrFilter.filter(
            response.xpath("//*[@id='js_content']").xpath('string(.)').extract_first())
        item["exhibitionTime"] ="线上展览"
        print(item)
        yield item