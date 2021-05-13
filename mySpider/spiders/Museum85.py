#lay
from ..items import *


class Museum85(scrapy.Spider):
    name = "Museum85"
    allowed_domains = ['douban.com']
    start_urls = ['https://www.douban.com/note/706802767/']

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
        item["museumID"] = 85
        item["museumName"] = "淮北市博物馆"
        item["address"] = "安徽省淮北市相山区博物馆路1号"
        # str(response.xpath(
        # "/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[1]/dd[3]/text()").extract_first()).replace("\n", "")
        item["openingTime"] = "周二-周日，周一闭馆。夏季：8:30-11:00，15:00-17:30；冬季：8:30-11:00，14:30-17:00"
        # str(response.xpath(
        # "/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[2]/dd[3]/text()").extract_first()).replace("\n", "")
        item["consultationTelephone"] = "0561-3115614"
        item["publicityVideoLink"] = None
        item["longitude"] = "116.804537"
        item["latitude"] = "33.961656"
        item["introduction"] = response.xpath(
            '//*[@id="link-report"]/div[1]/p[7]/text()').extract()
        print(item)
        yield item
