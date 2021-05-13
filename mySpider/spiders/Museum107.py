#lay
from ..items import *


class Museum107(scrapy.Spider):
    name = "Museum107"
    allowed_domains = ['sdmuseum.com']
    start_urls = ['http://www.sdmuseum.com/articles/ch00005/201701/aa4de466-179e-4c4d-bd0a-3ca2af6f7923.shtml']

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
        item["museumID"] = 107
        item["museumName"] = "山东博物馆"
        item["address"] = "济南市历下区经十东路11899号"
        # str(response.xpath(
        # "/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[1]/dd[3]/text()").extract_first()).replace("\n", "")
        item["openingTime"] = "周二至周日,09:00-16:00"

        # str(response.xpath(
        # "/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[2]/dd[3]/text()").extract_first()).replace("\n", "")
        item["consultationTelephone"] = "(0531)85058202"
        item["publicityVideoLink"] = None
        item["longitude"] = "117.102287"
        item["latitude"] = "36.664652"
        item["introduction"] = response.xpath(
            '/html/body/div[3]/div[2]/div[2]/div/p[1]/span/text()[1]').extract()
        print(item)
        yield item
