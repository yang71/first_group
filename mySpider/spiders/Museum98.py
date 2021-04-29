#lay
from ..items import *


class Museum98(scrapy.Spider):
    name = "Museum98"
    allowed_domains = ['baike.baidu.com']
    start_urls = ['https://baike.baidu.com/item/%E5%85%AB%E5%A4%A7%E5%B1%B1%E4%BA%BA%E7%BA%AA%E5%BF%B5%E9%A6%86/647149?fr=aladdin']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.MuseumPipeLine': 300,
        }
    }

    def parse(self, response, **kwargs):
        item = MuseumBasicInformationItem()
        item["museumID"] = 98
        item["museumName"] = "八大山人纪念馆"
        item["address"] = "江西省南昌市青云谱区青云路259号"
        # str(response.xpath(
        # "/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[1]/dd[3]/text()").extract_first()).replace("\n", "")
        item["openingTime"] = "周二至周日,09:00-16:30"
        # str(response.xpath(
        # "/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[2]/dd[3]/text()").extract_first()).replace("\n", "")
        item["consultationTelephone"] = "(0791)85273565"
        item["publicityVideoLink"] = None
        item["longitude"] = "115.923393"
        item["latitude"] = "28.610596"
        item["introduction"] = response.xpath(
            '/html/body/div[3]/div[2]/div/div[1]/div[4]/div[1]/text()').extract()

        print(item)
        yield item
