#lay
from ..items import *


class Museum105(scrapy.Spider):
    name = "Museum105"
    allowed_domains = ['jiawuzhanzheng.org']
    start_urls = ['http://www.jiawuzhanzheng.org/menu/about-us/fsjwar-expo-museum']

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
        item["museumID"] = 105
        item["museumName"] = "中国甲午战争博物馆"
        item["address"] = "山东省威海市刘公岛丁公路48号"
        # str(response.xpath(
        # "/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[1]/dd[3]/text()").extract_first()).replace("\n", "")
        item["openingTime"] = "07:00-18:00"

        # str(response.xpath(
        # "/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[2]/dd[3]/text()").extract_first()).replace("\n", "")
        item["consultationTelephone"] = "0631-5208001"
        item["publicityVideoLink"] = None
        item["longitude"] = "122.193741"
        item["latitude"] = "37.505408"
        item["introduction"] = response.xpath(
            '//*[@id="content_mainA"]/div/div/div/p[1]/text()').extract()
        print(item)
        yield item
