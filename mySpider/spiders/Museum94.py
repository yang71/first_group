#lay
from ..items import *


class Museum94(scrapy.Spider):
    name = "Museum94"
    allowed_domains = ['jxmuseum.cn']
    start_urls = ['http://www.jxmuseum.cn/survey/introduction']

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
        item["museumID"] = 94
        item["museumName"] = "江西省博物馆"
        item["address"] = "江西省南昌市红谷滩区赣江北大道698号"
        # str(response.xpath(
        # "/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[1]/dd[3]/text()").extract_first()).replace("\n", "")
        item["openingTime"] = "周二至周日9：00—17：00；周一闭馆（法定节假日除外）"
        # str(response.xpath(
        # "/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[2]/dd[3]/text()").extract_first()).replace("\n", "")
        item["consultationTelephone"] = "0791-88233369"
        item["publicityVideoLink"] = None
        item["longitude"] = "115.888431"
        item["latitude"] = "28.711549"
        item["introduction"] = "江西省博物馆筹建于1953年，是全省最大的综合性博物馆，首批国家一级博物馆，全省爱国主义教育基地。60 多年来，江西省博物馆历经八一广场老馆到新洲路馆到赣江北大道新馆。新馆为江西省文化中心三大馆之一，以方盒为建筑原型，寓意为宝盒，共6层，建筑面积8.6万平方米，展陈面积2.8万平方米。"
        print(item)
        yield item
