#lay
from ..items import *


class Museum86(scrapy.Spider):
    name = "Museum86"
    allowed_domains = ['sz-museum.com']
    start_urls = ['http://www.sz-museum.com/channel/18.html?wd=bgjs']

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
        item["museumID"] = 86
        item["museumName"] = "宿州市博物馆"
        item["address"] = "安徽省宿州市埇桥区博物馆路1号"
        # str(response.xpath(
        # "/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[1]/dd[3]/text()").extract_first()).replace("\n", "")
        item["openingTime"] = "周二—周日9:00-17:00，周一闭馆（国家法定节假日除外）"
        # str(response.xpath(
        # "/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[2]/dd[3]/text()").extract_first()).replace("\n", "")
        item["consultationTelephone"] = "3020006"
        item["publicityVideoLink"] = None
        item["longitude"] = "116.970544"
        item["latitude"] = "33.652095"
        item["introduction"] = response.xpath(
            '/html/body/div[1]/div[4]/div/div/div[2]/div[2]/p[1]/text()').extract()
        print(item)
        yield item
