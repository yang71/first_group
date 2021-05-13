#lay
from ..items import *


class Museum101(scrapy.Spider):
    name = "Museum101"
    allowed_domains = ['gzsbwg.cn']
    start_urls = ['http://www.gzsbwg.cn/html/infolist-1.html']

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
        item["museumID"] = 101
        item["museumName"] = "赣州市博物馆"
        item["address"] = "江西省赣康路与长宁路交叉口南150米"
        # str(response.xpath(
        # "/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[1]/dd[3]/text()").extract_first()).replace("\n", "")
        item["openingTime"] = "周二至周日,09:00-17:00"

        # str(response.xpath(
        # "/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[2]/dd[3]/text()").extract_first()).replace("\n", "")
        item["consultationTelephone"] = "(0797)8302212"
        item["publicityVideoLink"] = None
        item["longitude"] = "114.940503"
        item["latitude"] = "25.835176"
        item["introduction"] = response.xpath(
            '//*[@id="contentDiv"]/div[1]/div/div/div/text()[1]').extract()
        print(item)
        yield item
