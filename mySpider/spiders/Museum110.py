#lay
from ..items import *


class Museum110(scrapy.Spider):
    name = "Museum110"
    allowed_domains = ['kzbwg.cn']
    start_urls = ['http://www.kzbwg.cn/about/jianjie/']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.MuseumPipeLine': 300,
        }
    }

    def parse(self, response, **kwargs):
        item = MuseumBasicInformationItem()
        item["museumID"] = 110
        item["museumName"] = "孔子博物馆"
        item["address"] = "济宁市曲阜市孔子大道100号"
        # str(response.xpath(
        # "/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[1]/dd[3]/text()").extract_first()).replace("\n", "")
        item["openingTime"] = "周二至周日,09:00-16:00"

        # str(response.xpath(
        # "/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[2]/dd[3]/text()").extract_first()).replace("\n", "")
        item["consultationTelephone"] = "(0537)4459088"
        item["publicityVideoLink"] = None
        item["longitude"] = "120.658087"
        item["latitude"] = "31.160561"
        item["introduction"] = response.xpath(
            '/html/body/div[6]/div/div/div[2]/p[1]/text()').extract()
        print(item)
        yield item
