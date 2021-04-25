#lay
from ..items import *


class Museum95(scrapy.Spider):
    name = "Museum95"
    allowed_domains = ['rjjng.com.cn']
    start_urls = ['http://www.rjjng.com.cn/gaikuang.thtml?id=10928']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.MuseumPipeLine': 300,
        }
    }

    def parse(self, response, **kwargs):
        item = MuseumBasicInformationItem()
        item["museumID"] = 95
        item["museumName"] = "瑞金中央革命根据地纪念馆"
        item["address"] = "江西省瑞金市城西龙珠路1号"
        # str(response.xpath(
        # "/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[1]/dd[3]/text()").extract_first()).replace("\n", "")
        item["openingTime"] = "8:30-17:30（夏季）,8:30-17:00（冬季）"
        # str(response.xpath(
        # "/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[2]/dd[3]/text()").extract_first()).replace("\n", "")
        item["consultationTelephone"] = "0797-2522063"
        item["publicityVideoLink"] = None
        item["longitude"] = "116.022311"
        item["latitude"] = "25.874865"
        item["introduction"] = response.xpath(
            '/html/body/div[1]/div[3]/div/div[2]/div[2]/p[1]/text()').extract()

        print(item)
        yield item
