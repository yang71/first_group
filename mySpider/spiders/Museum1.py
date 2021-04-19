from ..items import *


class Museum0(scrapy.Spider):
    name = "Museum1"
    allowed_domains = ['baike.baidu.com']
    start_urls = ['https://baike.baidu.com/item/%E4%B8%AD%E5%9B%BD%E7%A7%91%E5%AD%A6%E6%8A%80%E6%9C%AF%E9%A6%86/1751615?fr=aladdin']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.MuseumPipeLine': 300,
        }
    }

    def parse(self, response, **kwargs):
        item = MuseumBasicInformationItem()
        item["museumID"] = 3
        item["museumName"] = response.xpath("/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[1]/dd[1]/text()").extract()
        item["address"] = response.xpath("/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[1]/dd[6]/text()").extract()
        item["openingTime"] = response.xpath("/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[2]/dd[7]/text()").extract()
        item["consultationTelephone"] = "not found"
        item["introduction"] = response.xpath("/html/body/div[3]/div[2]/div/div[1]/div[4]/div[1]/text()").extract()
        item["publicityVideoLink"] = "not found"
        item["longitude"] = "666.666666"
        item["latitude"] = "66.666666"
        yield item
