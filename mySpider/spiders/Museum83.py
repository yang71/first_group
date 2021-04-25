#lay
from ..items import *


class Museum83(scrapy.Spider):
    name = "Museum83"
    allowed_domains = ['hzwhbwg.com']
    start_urls = ['http://www.hzwhbwg.com/index.php/list-2.html']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.MuseumPipeLine': 300,
        }
    }

    def parse(self, response, **kwargs):
        item = MuseumBasicInformationItem()
        item["museumID"] = 83
        item["museumName"] = "安徽中国徽州文化博物馆"
        item["address"] = "安徽省黄山市机场迎宾大道50号 "
        # str(response.xpath(
        # "/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[1]/dd[3]/text()").extract_first()).replace("\n", "")
        item["openingTime"] = "开放时间09:00-17:00,16:30停止入馆，周一闭馆"
        # str(response.xpath(
        # "/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[2]/dd[3]/text()").extract_first()).replace("\n", "")
        item["consultationTelephone"] = "0559-2574222"
        item["publicityVideoLink"] = None
        item["longitude"] = "118.281156"
        item["latitude"] = "29.7234"
        item["introduction"] = response.xpath(
            '/html/body/div[6]/div[2]/p[2]/text()').extract()
        print(item)
        yield item
