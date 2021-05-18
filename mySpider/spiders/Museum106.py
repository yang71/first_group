#lay
from ..items import *


class Museum106(scrapy.Spider):
    name = "Museum106"
    allowed_domains = ['qingzhoumuseum.cn']
    start_urls = ['http://www.qingzhoumuseum.cn/zx/']

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
        item["museumID"] = 106
        item["museumName"] = "青州博物馆"
        item["address"] = "潍坊市青州市范公亭西路1号"
        # str(response.xpath(
        # "/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[1]/dd[3]/text()").extract_first()).replace("\n", "")
        item["openingTime"] = "周二至周日,09:00-16:30"

        # str(response.xpath(
        # "/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[2]/dd[3]/text()").extract_first()).replace("\n", "")
        item["consultationTelephone"] = "(0536)3266200"
        item["publicityVideoLink"] = None
        item["longitude"] = "118.469183"
        item["latitude"] = "36.690088"
        item["introduction"] = response.xpath(
            '/html/body/div[2]/table/tbody/tr[4]/td/div/p[1]/text()').extract()
        print(item)
        yield item
