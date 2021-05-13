#lay
from ..items import *


class Museum79(scrapy.Spider):
    name = "Museum79"
    allowed_domains = ['portmuseum.cn']
    start_urls = ['http://www.portmuseum.cn/doc/gk/jj/index.shtml']

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
        item["museumID"] = 79
        item["museumName"] = "宁波中国港口博物馆"
        item["address"] = "浙江省宁波市北仑区春晓港博路6号"
        # str(response.xpath(
        # "/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[1]/dd[3]/text()").extract_first()).replace("\n", "")
        item["openingTime"] = "9:00-17:00（16:00停止入馆）,周二至周日，周一闭馆"
        # str(response.xpath(
        # "/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[2]/dd[3]/text()").extract_first()).replace("\n", "")
        item["consultationTelephone"] = "0574-26915555"
        item["publicityVideoLink"] = None
        item["longitude"] = "121.915854"
        item["latitude"] = "29.762441"
        item["introduction"] = response.xpath(
            '/html/body/div[3]/div[2]/div[1]/div[2]/p[1]/text()').extract()
        # str(response.xpath("/html/body/div[3]/div[2]/div/div[1]/div[4]/div[2]").xpath(
        # "string(.)").extract_first()).split("\n")[0]
        print(item)
        yield item
