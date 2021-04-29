#lay
from ..items import *


class Museum96(scrapy.Spider):
    name = "Museum96"
    allowed_domains = ['81-china.com']
    start_urls = ['http://www.81-china.com/gaikuang/show-55.html']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.MuseumPipeLine': 300,
        }
    }

    def parse(self, response, **kwargs):
        item = MuseumBasicInformationItem()
        item["museumID"] = 96
        item["museumName"] = "南昌八一起义纪念馆"
        item["address"] = "南昌市西湖区中山路380号"
        # str(response.xpath(
        # "/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[1]/dd[3]/text()").extract_first()).replace("\n", "")
        item["openingTime"] = "周二至周日,09:00-17:00"
        # str(response.xpath(
        # "/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[2]/dd[3]/text()").extract_first()).replace("\n", "")
        item["consultationTelephone"] = "(0791)86613806"
        item["publicityVideoLink"] = None
        item["longitude"] = "115.969301"
        item["latitude"] = "28.561501"
        item["introduction"] = response.xpath(
            '/html/body/div[1]/div[5]/div[4]/div/p[3]/span/text()').extract()

        print(item)
        yield item
