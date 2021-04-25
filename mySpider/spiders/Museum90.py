#lay
from ..items import *


class Museum90(scrapy.Spider):
    name = "Museum90"
    allowed_domains = ['qzhjg.cn']
    start_urls = ['http://www.qzhjg.cn/bggk/index.jhtml']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.MuseumPipeLine': 300,
        }
    }

    def parse(self, response, **kwargs):
        item = MuseumBasicInformationItem()
        item["museumID"] = 90
        item["museumName"] = "泉州海外交通史博物馆"
        item["address"] = "泉州市丰泽区东湖街425号"
        # str(response.xpath(
        # "/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[1]/dd[3]/text()").extract_first()).replace("\n", "")
        item["openingTime"] = "夏令时：上午 9:00 —下午17:30(17:00停止入场),冬令时：上午 9:00 —下午17:00(16:30停止入场)"
        # str(response.xpath(
        # "/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[2]/dd[3]/text()").extract_first()).replace("\n", "")
        item["consultationTelephone"] = "0595-22100561"
        item["publicityVideoLink"] = None
        item["longitude"] = "118.617926"
        item["latitude"] = "24.915806"
        item["introduction"] = response.xpath(
            '/html/body/div[1]/div[2]/div/div[3]/div/div/div[2]/p[2]/span/text()').extract()
        print(item)
        yield item
