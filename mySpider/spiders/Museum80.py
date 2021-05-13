#lay
from ..items import *


class Museum80(scrapy.Spider):
    name = "Museum80"
    allowed_domains = ['bytravel.cn']
    start_urls = ['http://www.bytravel.cn/Landscape/57/nanhugemingjinian.html']

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
        item["museumID"] = 80
        item["museumName"] = "南湖革命纪念馆"
        item["address"] = "浙江嘉兴市南湖区烟雨路七一广场"
        # str(response.xpath(
        # "/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[1]/dd[3]/text()").extract_first()).replace("\n", "")
        item["openingTime"] = "8：30—16：30"
        # str(response.xpath(
        # "/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[2]/dd[3]/text()").extract_first()).replace("\n", "")
        item["consultationTelephone"] = "0574-26915555"
        item["publicityVideoLink"] = None
        item["longitude"] = "120.767807"
        item["latitude"] = "30.753078"
        item["introduction"] = response.xpath(
            '//*[@id="page_left"]/div[7]/p[1]/text()').extract()
        # str(response.xpath("/html/body/div[3]/div[2]/div/div[1]/div[4]/div[2]").xpath(
        # "string(.)").extract_first()).split("\n")[0]
        print(item)
        yield item
