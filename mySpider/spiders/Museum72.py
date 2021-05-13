#lay
from ..items import *


class Museum72(scrapy.Spider):
    name = "Museum72"
    allowed_domains = ['nbmuseum.cn']
    start_urls = ['http://nbmuseum.cn/col/col41/index.html']

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
        item["museumID"] = 72
        item["museumName"] = "宁波博物院"
        item["address"] = "宁波市鄞州区首南中路1000号"
        # str(response.xpath(
        # "/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[1]/dd[3]/text()").extract_first()).replace("\n", "")
        item["openingTime"] = "参观入场时间9：00—16：00，闭馆时间17：00。周一闭馆（国家法定节假日除外）。"
        # str(response.xpath(
        # "/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[2]/dd[3]/text()").extract_first()).replace("\n", "")
        item["consultationTelephone"] = "（0574）82815588"
        item["publicityVideoLink"] = None
        item["longitude"] = "121.551803"
        item["latitude"] = "29.821188"
        item["introduction"] = response.xpath(
            '//*[@id="zoom"]/p[1]/text()').extract()
        # str(response.xpath("/html/body/div[3]/div[2]/div/div[1]/div[4]/div[2]").xpath(
        # "string(.)").extract_first()).split("\n")[0]
        yield item
