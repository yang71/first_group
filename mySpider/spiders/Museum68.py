#lay
from ..items import *


class Museum68(scrapy.Spider):
    name = "Museum68"
    allowed_domains = ['zj-museum.com.cn']
    start_urls = ['http://www.zj-museum.com.cn/zjbwg/zjbwg//introduction.html']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.MuseumPipeLine': 300,
        }
    }

    def parse(self, response, **kwargs):
        item = MuseumBasicInformationItem()
        item["museumID"] = 68
        item["museumName"] = "镇江博物馆"
        item["address"] = "镇江市伯先路85号"
        # str(response.xpath(
        # "/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[1]/dd[3]/text()").extract_first()).replace("\n", "")
        item["openingTime"] = "周二至周日 9:00-17:00(16:00停止进馆)"
        # str(response.xpath(
        # "/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[2]/dd[3]/text()").extract_first()).replace("\n", "")
        item["consultationTelephone"] = "0511—85285032"
        item["publicityVideoLink"] = None
        item["longitude"] = "119.438261"
        item["latitude"] = "32.21968"
        item["introduction"] = response.xpath(
            '/html/body/div[3]/div[2]/div/p[1]/text()').extract()
        # str(response.xpath("/html/body/div[3]/div[2]/div/div[1]/div[4]/div[2]").xpath(
        # "string(.)").extract_first()).split("\n")[0]
        print(item)
        yield item
