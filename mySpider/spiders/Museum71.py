#lay
from ..items import *


class Museum71(scrapy.Spider):
    name = "Museum71"
    allowed_domains = ['chinasilkmuseum.com']
    start_urls = ['https://www.chinasilkmuseum.com/bwggk/index_3.aspx']

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
        item["museumID"] = 71
        item["museumName"] = "中国丝绸博物馆"
        item["address"] = "浙江省杭州市西湖区玉皇山路73-1号"
        # str(response.xpath(
        # "/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[1]/dd[3]/text()").extract_first()).replace("\n", "")
        item["openingTime"] = "9:00—17:00（16:30停止入馆），每周一：9:00—12:00闭馆（法定节假日除外）"
        # str(response.xpath(
        # "/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[2]/dd[3]/text()").extract_first()).replace("\n", "")
        item["consultationTelephone"] = "0516—83804412"
        item["publicityVideoLink"] = None
        item["longitude"] = "120.157949"
        item["latitude"] = "30.228906"
        item["introduction"] = response.xpath(
            '/html/body/div[1]/div/div[3]/div/p[2]/text()').extract()
        # str(response.xpath("/html/body/div[3]/div[2]/div/div[1]/div[4]/div[2]").xpath(
        # "string(.)").extract_first()).split("\n")[0]
        print(item)
        yield item
