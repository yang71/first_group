#lay
from ..items import *


class Museum104(scrapy.Spider):
    name = "Museum104"
    allowed_domains = ['pxmuseum.com']
    start_urls = ['http://www.pxmuseum.com/nd.jsp?id=116#_jcp=1']

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
        item["museumID"] = 104
        item["museumName"] = "青岛市博物馆"
        item["address"] = "青岛市崂山区梅岭东路51号"
        # str(response.xpath(
        # "/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[1]/dd[3]/text()").extract_first()).replace("\n", "")
        item["openingTime"] = "5月至11月 周二至周日 09:00-17:00;11月至5月 周二至周日 09:00-16:30"
        # str(response.xpath(
        # "/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[2]/dd[3]/text()").extract_first()).replace("\n", "")
        item["consultationTelephone"] = "(0532)88896286"
        item["publicityVideoLink"] = None
        item["longitude"] = "120.389455"
        item["latitude"] = "36.072227"
        item["introduction"] = response.xpath(
            '/html/body/div[2]/table/tbody/tr/td[1]/dl/dd/ol/table[2]/tbody/tr[3]/td/text()[1]').extract()
        print(item)
        yield item
