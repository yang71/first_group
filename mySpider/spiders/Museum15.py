#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/4/20 18:52 
# @Author  : ana
# @File    : Museum15.py
# @Software: PyCharm

from ..items import *


class Museum15(scrapy.Spider):
    name = "Museum15"
    allowed_domains = ['www.cnfm.org.cn']
    start_urls = ['http://www.cnfm.org.cn/index_2019.shtml']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.MuseumPipeLine': 300,
        }
    }

    def parse(self, response, **kwargs):
        item = MuseumBasicInformationItem()
        item["museumID"] = 15
        item["museumName"] = "中国电影博物馆"
        item["address"] = "北京市朝阳区南影路九号"
        item["openingTime"] = str(response.xpath(
            "//*[@id='scroll_begin']/a//text()").extract_first()).replace(" ", "").split("\n")[1].replace("\r", "")
        item["consultationTelephone"] = "010-64319548"
        item["publicityVideoLink"] = None
        item["longitude"] = "116.422139"
        item["latitude"] = "40.063913"
        url = 'http://www.cnfm.org.cn/ybxxjs/ybjj.shtml'
        yield scrapy.Request(url, callback=self.parseAnotherPage, meta={"item": item})

    # 切换页面
    def parseAnotherPage(self, response):
        item = response.meta["item"]
        item[
            "introduction"] = "中国电影博物馆是经国务院批准，原国家广播电影电视总局和北京市人民政府共同建设的大型公共文化设施，是目前世界上最大的国家级电影专业博物馆，是纪念中国电影诞生100周年的标志性建筑，是展示中国电影发展历程、博览电影科技、传播电影文化和进行学术研究交流的艺术殿堂，是爱国主义教育基地、廉政教育基地、青少年电影文化活动基地和科普教育基地等。"

        print(item)
        yield item
