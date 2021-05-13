import scrapy as scrapy

from ..items import *

class Museum22(scrapy.Spider):
    name = "Museum22"
    allowed_domains = ['hebeimuseum.org.cn']
    start_urls = ['http://www.hebeimuseum.org.cn/']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.MuseumPipeLine': 300,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.DefaultMiddleware': 0,
        },
    }
    # 需要重写的部分
    def parse(self, response, **kwargs):
        item = MuseumBasicInformationItem()
        item["museumID"] = 22
        item["museumName"] = "河北博物馆"
        item["address"] = "河北省石家庄市东大街4号"
        item["openingTime"] = response.xpath('//*[@id="content"]/div[1]/div[2]/div[2]/div[2]/p[1]/text()').extract_first()
        item["consultationTelephone"] = "(0311)966518"
        item["introduction"] = None
        item["publicityVideoLink"] = None
        item["longitude"] = "117.1531"
        item["latitude"] = "39.1747"
        print(item)
        yield item
