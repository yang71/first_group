#lay
from ..items import *


class Museum84(scrapy.Spider):
    name = "Museum84"
    allowed_domains = ['ahgm.org.cn']
    start_urls = ['http://www.ahgm.org.cn/ahgm/ahgm/dbjj/gzzc/index.html']

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
        item["museumID"] = 84
        item["museumName"] = "安徽省地质博物馆"
        item["address"] = "安徽省合肥市政务区仙龙湖路999号"
        # str(response.xpath(
        # "/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[1]/dd[3]/text()").extract_first()).replace("\n", "")
        item["openingTime"] = "周二至周日9:00-17:00（16:00停止入场）"
        # str(response.xpath(
        # "/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[2]/dd[3]/text()").extract_first()).replace("\n", "")
        item["consultationTelephone"] = "0551-63548008"
        item["publicityVideoLink"] = None
        item["longitude"] = "117.228637"
        item["latitude"] = "31.809576"
        item["introduction"] = response.xpath(
            '/html/body/div[6]/div/div[4]/div/div/div[2]/span/span/span/text()').extract()
        print(item)
        yield item
