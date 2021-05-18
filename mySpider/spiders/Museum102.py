#lay
from ..items import *


class Museum102(scrapy.Spider):
    name = "Museum102"
    allowed_domains = ['zgtcbwg.com']
    start_urls = ['http://www.zgtcbwg.com/index.php?s=/home/article/page/id/39.html']

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
        item["museumID"] = 102
        item["museumName"] = "景德镇中国陶瓷博物馆"
        item["address"] = "江西省景德镇市昌江区紫晶路1号"
        # str(response.xpath(
        # "/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[1]/dd[3]/text()").extract_first()).replace("\n", "")
        item["openingTime"] = "周二至周日:09:00-16:30"

        # str(response.xpath(
        # "/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[2]/dd[3]/text()").extract_first()).replace("\n", "")
        item["consultationTelephone"] = "(0798)8253701"
        item["publicityVideoLink"] = None
        item["longitude"] = "119.837128"
        item["latitude"] = "31.265104"
        item["introduction"] = response.xpath(
            '/html/body/div[1]/div[1]/div[2]/div[2]/p[3]/span/text()').extract()
        print(item)
        yield item
