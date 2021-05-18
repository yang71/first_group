import scrapy as scrapy

from ..items import *

class Museum29(scrapy.Spider):
    name = "Museum29"
    allowed_domains = ['baidu.com']
    start_urls = ['https://baike.baidu.com/item/%E5%B1%B1%E8%A5%BF%E5%9C%B0%E8%B4%A8%E5%8D%9A%E7%89%A9%E9%A6%86/13877240?fr=aladdin']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.MuseumPipeLine': 300,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.DefaultMiddleware': 0,
        },
    }
    # 需要重写的部分
    def parse(self, response, **kwargs):
        item = MuseumBasicInformationItem()
        item["museumID"] = 29
        item["museumName"] = response.xpath('normalize-space(/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[1]/dd[1])').extract_first()
        item["address"] = response.xpath('normalize-space(/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[1]/dd[3])').extract_first()
        item["openingTime"] = response.xpath('normalize-space(/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[2]/dd[1])').extract_first()
        item["consultationTelephone"] = "0351-4069643"
        item["introduction"] = response.xpath('normalize-space(/html/body/div[3]/div[2]/div/div[1]/div[4])').extract_first()
        item["introduction"] = "" .join(item["introduction"]. split())
        item["publicityVideoLink"] = response.xpath('/html/body/div[3]/div[1]/div/div[2]/div[2]/div/div[1]')
        item["longitude"] = "112.5400"
        item["latitude"] = "37.8964"
        print(item)
        yield item
