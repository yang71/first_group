#lay
from ..items import *


class Museum87(scrapy.Spider):
    name = "Museum87"
    allowed_domains = ['ahbbmuseum.com']
    start_urls = ['https://www.ahbbmuseum.com/?about_8/']

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
        item["museumID"] = 87
        item["museumName"] = "蚌埠市博物馆"
        item["address"] = "安徽省蚌埠市东海大道市民广场"
        # str(response.xpath(
        # "/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[1]/dd[3]/text()").extract_first()).replace("\n", "")
        item["openingTime"] = "9:00-17:00,周一（除国家法定节假日外）闭馆"
        # str(response.xpath(
        # "/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[2]/dd[3]/text()").extract_first()).replace("\n", "")
        item["consultationTelephone"] = "0552—2042312"
        item["publicityVideoLink"] = None
        item["longitude"] = "117.395513"
        item["latitude"] = "32.921524"
        item["introduction"] = response.xpath(
            '/html/body/div[2]/div[2]/div/div/div/div/div/div[2]/p[2]').extract()
        print(item)
        yield item
