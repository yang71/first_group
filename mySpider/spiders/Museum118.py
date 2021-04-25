#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/4/25 10:12
# @Author  : zqy
# @File    : Museum000.py
# @Software: PyCharm

from ..items import *
import re


class Museum118(scrapy.Spider):
    name = 'Museum118'
    allowed_domains = ['baike.baidu.com']
    start_urls = ['https://baike.baidu.com/item/%E5%B1%B1%E4%B8%9C%E7%9C%81%E6%BB%95%E5%B7%9E%E5%B8%82%E5%8D%9A%E7%89%A9%E9%A6%86/24167836?fr=aladdin']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.MuseumPipeLine': 300,
        }
    }

    def parse(self, response, **kwargs):
        r = re.compile(u"\\n|\\r|\\[.*?]|\\t|\\xa0")
        item = MuseumBasicInformationItem()
        item["museumID"] = 118
        item["museumName"] = "山东省滕州市博物馆"
        item["address"] = response.xpath("/html/body/div[3]/div[2]/div/div[1]/div[8]/dl[2]/dd[2]").xpath('string(.)').extract_first()
        item["address"] = re.sub(r, '', item["address"])

        item["openingTime"] = response.xpath("/html/body/div[3]/div[2]/div/div[1]/div[8]/dl[1]/dd[4]").xpath('string(.)').extract_first()
        item["openingTime"] = re.sub(r, '', item["openingTime"])

        item["consultationTelephone"] = "0632-5500986"
        item["consultationTelephone"] = re.sub(r, '', item["consultationTelephone"])

        item["publicityVideoLink"] = None
        item["longitude"] = "117.182536"
        item["latitude"] = "35.093718"

        item["introduction"] = "滕州市博物馆是集历史、艺术、人文为一体的综合性、多功能、现代化地方博物馆。1956年，滕县文化馆建立文物陈列室，1958年成立滕县博物馆，设“自然之部”、“历史之部”和“社建之部”3个陈列室，并有石刻碑廊一处，收藏文物500余件。"
        print(item)
        yield item