#lay
from ..items import *


class Museum100(scrapy.Spider):
    name = "Museum100"
    allowed_domains = ['lushanmuseum.com']
    start_urls = ['http://www.lushanmuseum.com/gaikuang.asp?id=106']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.MuseumPipeLine': 300,
        }
    }

    def parse(self, response, **kwargs):
        item = MuseumBasicInformationItem()
        item["museumID"] = 100
        item["museumName"] = "江西省庐山博物馆"
        item["address"] = "江西省九江市庐山市牯岭东谷"
        # str(response.xpath(
        # "/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[1]/dd[3]/text()").extract_first()).replace("\n", "")
        item["openingTime"] = "08:30-17:00"
        # str(response.xpath(
        # "/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[2]/dd[3]/text()").extract_first()).replace("\n", "")
        item["consultationTelephone"] = "(0792)8288062"
        item["publicityVideoLink"] = None
        item["longitude"] = "115.983527"
        item["latitude"] = "29.556921"
        item["introduction"] = "庐山博物馆座落在风景秀丽的芦林湖畔，占地面积二万余平方米，馆藏极为丰富，尤以陶瓷、书画最具特色。庐山博物馆座落在风景秀丽的芦林湖畔，占地面积二万余平方米，馆藏极为丰富，尤以陶瓷、书画最具特色。"

        print(item)
        yield item
