#lay
from ..items import *


class Museum93(scrapy.Spider):
    name = "Museum93"
    allowed_domains = ['jgsgmbwg.com']
    start_urls = ['http://www.jgsgmbwg.com/about.php?cid=3']

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
        item["museumID"] = 93
        item["museumName"] = "井冈山革命博物馆"
        item["address"] = "江西省井冈山茨坪红军南路"
        # str(response.xpath(
        # "/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[1]/dd[3]/text()").extract_first()).replace("\n", "")
        item["openingTime"] = "8:00-17:00"
        # str(response.xpath(
        # "/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[2]/dd[3]/text()").extract_first()).replace("\n", "")
        item["consultationTelephone"] = "0796-6552248"
        item["publicityVideoLink"] = None
        item["longitude"] = "114.172166"
        item["latitude"] = "26.573406"
        item["introduction"] = response.xpath(
            '//*[@id="top"]/div[5]/div[2]/div/p[2]/span[1]/span[2]/text()').extract()
        print(item)
        yield item
