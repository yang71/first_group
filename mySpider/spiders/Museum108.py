#lay
from ..items import *


class Museum108(scrapy.Spider):
    name = "Museum108"
    allowed_domains = ['ytmuseum.com']
    start_urls = ['http://www.ytmuseum.com/article']

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
        item["museumID"] = 108
        item["museumName"] = "烟台市博物馆"
        item["address"] = "烟台市芝罘区南大街61号"
        # str(response.xpath(
        # "/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[1]/dd[3]/text()").extract_first()).replace("\n", "")
        item["openingTime"] = "周二至周日,09:00-16:00"

        # str(response.xpath(
        # "/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[2]/dd[3]/text()").extract_first()).replace("\n", "")
        item["consultationTelephone"] = "(0535)6232976"
        item["publicityVideoLink"] = None
        item["longitude"] = "121.454415"
        item["latitude"] = "37.470038"
        item["introduction"] = response.xpath(
            '//*[@id="MainLeft"]/div[4]/div[1]/div/div/div[1]/div/div[1]/span/p[1]/span[2]/text()').extract()
        print(item)
        yield item
