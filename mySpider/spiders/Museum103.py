#lay
from ..items import *


class Museum103(scrapy.Spider):
    name = "Museum103"
    allowed_domains = ['pxmuseum.com']
    start_urls = ['http://www.pxmuseum.com/nd.jsp?id=116#_jcp=1']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.MuseumPipeLine': 300,
        }
    }

    def parse(self, response, **kwargs):
        item = MuseumBasicInformationItem()
        item["museumID"] = 103
        item["museumName"] = "萍乡博物馆"
        item["address"] = "萍乡市滨河东路376号"
        # str(response.xpath(
        # "/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[1]/dd[3]/text()").extract_first()).replace("\n", "")
        item["openingTime"] = "周二至周日:09:00-16:30"

        # str(response.xpath(
        # "/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[2]/dd[3]/text()").extract_first()).replace("\n", "")
        item["consultationTelephone"] = "(0799)7115595"
        item["publicityVideoLink"] = None
        item["longitude"] = "113.866329"
        item["latitude"] = "27.646295"
        item["introduction"] = response.xpath(
            '//*[@id="module12"]/div/div/div/div/div[3]/div/p[4]/span/span/text()').extract()
        print(item)
        yield item
