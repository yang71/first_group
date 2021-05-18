#lay
from ..items import *


class Museum99(scrapy.Spider):
    name = "Museum99"
    allowed_domains = ['baike.baidu.com']
    start_urls = ['https://baike.baidu.com/item/%E5%85%AB%E5%A4%A7%E5%B1%B1%E4%BA%BA%E7%BA%AA%E5%BF%B5%E9%A6%86/647149?fr=aladdin']

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
        item["museumID"] = 99
        item["museumName"] = "九江市博物馆"
        item["address"] = "江西省九江市八里湖新区文博园内(胜利碑下)"
        # str(response.xpath(
        # "/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[1]/dd[3]/text()").extract_first()).replace("\n", "")
        item["openingTime"] = "周二至周日,09:00-17:00"

        # str(response.xpath(
        # "/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[2]/dd[3]/text()").extract_first()).replace("\n", "")
        item["consultationTelephone"] = "(0792)8135002"
        item["publicityVideoLink"] = None
        item["longitude"] = "115.960661"
        item["latitude"] = "29.666661"
        item["introduction"] = "九江市博物馆位于江西省九江市八里湖新区文博园内（胜利碑下）。九江市博物馆具有文物展览、学术交流、文物技术保护、公共服务等功能，是江西省建筑面积最大、功能最齐全的大型综合性博物馆，国家一级博物馆。该馆建于1978年6月，占地面积112亩，建筑面积1.8万平方米，展区面积9800平方米。截至到2012年底，九江市博物馆共免费接待观众近30万人次。"

        print(item)
        yield item
