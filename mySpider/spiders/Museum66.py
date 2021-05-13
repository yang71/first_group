#lay
from ..items import *


class Museum66(scrapy.Spider):
    name = "Museum66"
    allowed_domains = ['xzmuseum.com']
    start_urls = ['http://xzmuseum.com/about.aspx?page=about']

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
        item["museumID"] = 66
        item["museumName"] = "徐州博物馆"
        item["address"] = "江苏省徐州市和平路118号"
        # str(response.xpath(
        # "/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[1]/dd[3]/text()").extract_first()).replace("\n", "")
        item["openingTime"] = "周二至周日9：00—17：00开放（16:00停止入馆） | 每周一闭馆（遇法定节假日顺延）"
        # str(response.xpath(
        # "/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[2]/dd[3]/text()").extract_first()).replace("\n", "")
        item["consultationTelephone"] = "0516—83804412"
        item["publicityVideoLink"] = None
        item["longitude"] = "117.192977"
        item["latitude"] = "34.256457"
        item["introduction"] = response.xpath(
            '/html/body/div[4]/div/div[2]/div[2]/div[2]/p[2]/span[1]/span[2]/span/text()').extract()
        # str(response.xpath("/html/body/div[3]/div[2]/div/div[1]/div[4]/div[2]").xpath(
        # "string(.)").extract_first()).split("\n")[0]
        print(item)
        yield item
