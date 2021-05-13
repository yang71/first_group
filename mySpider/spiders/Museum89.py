#lay
from ..items import *


class Museum89(scrapy.Spider):
    name = "Museum89"
    allowed_domains = ['gthyjng.com']
    start_urls = ['http://www.gthyjng.com/gthyjs/201911/t20191127_543850.htm']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.MuseumPipeLine': 300,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.DefaultMiddleware': 0,
        },
    }

    def parse(self, response, **kwargs):
        item = MuseumBasicInformationItem()
        item["museumID"] = 89
        item["museumName"] = "福建博物院"
        item["address"] = "福建省龙岩市上杭县古田镇古田路85号"
        # str(response.xpath(
        # "/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[1]/dd[3]/text()").extract_first()).replace("\n", "")
        item["openingTime"] = "8:00－18:00（夏令时）、8:00－17:30（冬令时），全年对外开放，中午不休。"
        # str(response.xpath(
        # "/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[2]/dd[3]/text()").extract_first()).replace("\n", "")
        item["consultationTelephone"] = "0597-3641143"
        item["publicityVideoLink"] = None
        item["longitude"] = "116.829662"
        item["latitude"] = "25.227348"
        item["introduction"] = response.xpath(
            '//*[@id="fontzoom"]/div/div/p[1]/text()').extract()
        print(item)
        yield item
