#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/4 23:30
# @Author  : 10711
# @File    : Collection161.py
# @Software: PyCharm


from ..items import *
from ..str_filter import *
from ..auxiliary_files import Collection161_supporting


class Collection161(scrapy.Spider):
    name = "Collection161"
    allowed_domains = ['sxd.cn']
    start_urls = Collection161_supporting.Collection161Supporting.startUrl

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        }
    }
    def parse(self, response, **kwargs):
        tr_list = response.xpath("/html/body/div[1]/div[2]/div[2]/table[2]/tr/td[2]/table/tr[2]/td/table/tr/td/table[1]/tr")
        print(len(tr_list))
        for tr in tr_list:
            li_list = tr.xpath("./td")
            for li in li_list:
                item = CollectionItem()
                item["museumID"] = 161
                item["museumName"] = "三星堆博物馆"
                item['collectionName'] = StrFilter.filter(
                    li.xpath("./div[2]").xpath('string(.)').extract_first())
                item['collectionImageLink'] = StrFilter.getDoamin(response) + '/' + str(
                    li.xpath("./div[1]/div/a/img/@src").extract_first())
                url = StrFilter.getDoamin(response) + '/showinfojp.asp?id=' + str(re.findall(r"\d+\.?\d*",li.xpath("./div[1]/div/a/@href").extract_first())).replace("['", '').replace("']", '')
                print(url)
                yield scrapy.Request(
                    url,
                    callback=self.parseAnotherPage,
                    meta={"item": item}
                )

    def parseAnotherPage(self, response):
        item = response.meta["item"]
        item['collectionIntroduction'] = StrFilter.filter(
            response.xpath("//table/tr/td/table/tr[2]/td").xpath('string(.)').extract_first())
        print(item)
        yield(item)