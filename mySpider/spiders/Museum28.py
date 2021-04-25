import scrapy as scrapy

from ..items import *

class Museum28(scrapy.Spider):
    name = "Museum28"
    allowed_domains = ['baidu.com']
    start_urls = ['https://baike.baidu.com/item/%E5%A4%A7%E5%90%8C%E5%B8%82%E5%8D%9A%E7%89%A9%E9%A6%86/1777948?fr=aladdin']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.MuseumPipeLine': 300,
        }
    }
    # 需要重写的部分
    def parse(self, response, **kwargs):
        item = MuseumBasicInformationItem()
        item["museumID"] = 28
        item["museumName"] = response.xpath('normalize-space(/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[1]/dd[1])').extract_first()
        item["address"] = response.xpath('normalize-space(/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[2]/dd[1])').extract_first()
        item["openingTime"] = response.xpath('normalize-space(/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[1]/dd[5])').extract_first()
        item["consultationTelephone"] = "0352-2303518"
        item["introduction"] = response.xpath('normalize-space(/html/body/div[3]/div[2]/div/div[1]/div[4])').extract_first()
        item["introduction"] = "" .join(item["introduction"]. split())
        item["publicityVideoLink"] = None
        item["longitude"] = "113.4138"
        item["latitude"] = "40.0718"
        print(item)
        yield item
