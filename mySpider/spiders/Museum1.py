<<<<<<< HEAD
from ..items import *


class Museum0(scrapy.Spider):
    name = "Museum1"
    allowed_domains = ['baike.baidu.com']
    start_urls = ['https://baike.baidu.com/item/%E4%B8%AD%E5%9B%BD%E7%A7%91%E5%AD%A6%E6%8A%80%E6%9C%AF%E9%A6%86/1751615?fr=aladdin']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.MuseumPipeLine': 300,
        }
    }

    def parse(self, response, **kwargs):
        item = MuseumBasicInformationItem()
        item["museumID"] = 3
        item["museumName"] = response.xpath("/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[1]/dd[1]/text()").extract()
        item["address"] = response.xpath("/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[1]/dd[6]/text()").extract()
        item["openingTime"] = response.xpath("/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[2]/dd[7]/text()").extract()
        item["consultationTelephone"] = "not found"
        item["introduction"] = response.xpath("/html/body/div[3]/div[2]/div/div[1]/div[4]/div[1]/text()").extract()
        item["publicityVideoLink"] = "not found"
        item["longitude"] = "666.666666"
        item["latitude"] = "66.666666"
        yield item
=======
#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/4/18 21:52 
# @Author  : ana
# @File    : Museum1.py
# @Software: PyCharm

from ..items import *


class Museum1(scrapy.Spider):
    name = "Museum1"
    allowed_domains = ['cstm.cdstm.cn']
    start_urls = ['https://cstm.cdstm.cn/']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.MuseumPipeLine': 300,
        }
    }

    def parse(self, response, **kwargs):
        item = MuseumBasicInformationItem()
        item["museumID"] = 1
        item["museumName"] = "中国科学技术馆"
        item["address"] = "北京市朝阳区北辰东路5号"
        item["openingTime"] = response.xpath(
            "/html/body/div[6]/div[1]/div[2]/div/p[1]/span[2]/em/text()").extract_first()
        item["consultationTelephone"] = str(((response.xpath(
            "/html/body/div[8]/div/div[1]/p/text()[4]").extract_first()).replace("\xa0", '')).strip())
        item["publicityVideoLink"] = None
        item["longitude"] = "116.40504"
        item["latitude"] = "40.012384"
        url = 'https://cstm.cdstm.cn/bgs/kjghk/'
        yield scrapy.Request(url, callback=self.parseAnotherPage, meta={"item": item})

    # 切换页面
    def parseAnotherPage(self, response):
        item = response.meta["item"]
        item["introduction"] = response.xpath("/html/body/div[4]/div[3]/div/div[1]/div/p[2]/text()").extract_first()
        print(item)
        yield item
>>>>>>> 6c3f6c0374acbe0fc1fd7fc0907dac4cff9b474e
