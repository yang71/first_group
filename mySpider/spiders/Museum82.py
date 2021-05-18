#lay
from ..items import *


class Museum82(scrapy.Spider):
    name = "Museum82"
    allowed_domains = ['ahm.cn']
    start_urls = ['https://www.ahm.cn/News/Survey/abjj']

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
        item["museumID"] = 82
        item["museumName"] = "安徽省博物馆"
        item["address"] = "老馆：安徽省合肥市安庆路268号,新馆：安徽省合肥市怀宁路87号"
        # str(response.xpath(
        # "/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[1]/dd[3]/text()").extract_first()).replace("\n", "")
        item["openingTime"] = "每星期二至星期日9:00-17:00（16:00停止取票、入馆）每星期一闭馆（国家法定节假日除外）"
        # str(response.xpath(
        # "/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[2]/dd[3]/text()").extract_first()).replace("\n", "")
        item["consultationTelephone"] = "0551-63736658"
        item["publicityVideoLink"] = None
        item["longitude"] = "117.063604"
        item["latitude"] = "30.530957"
        item["introduction"] = response.xpath(
            '/html/body/div[3]/div/div[3]/div[1]/div/p[1]/text()').extract()
        print(item)
        yield item
