import scrapy as scrapy

from ..items import *

class Museum35(scrapy.Spider):
    name = "Museum35"
    allowed_domains = ['baidu.com']
    start_urls = ['https://baike.baidu.com/item/%E2%80%9C%E4%B9%9D%C2%B7%E4%B8%80%E5%85%AB%E2%80%9D%E5%8E%86%E5%8F%B2%E5%8D%9A%E7%89%A9%E9%A6%86/3149475?fr=aladdin']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.MuseumPipeLine': 300,
        }
    }
    # 需要重写的部分
    def parse(self, response, **kwargs):
        item = MuseumBasicInformationItem()
        item["museumID"] = 35
        item["museumName"] = response.xpath('normalize-space(/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[1]/dd[1])').extract_first()
        item["address"] = response.xpath('normalize-space(/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[1]/dd[3])').extract_first()
        item["address"] = "".join(item["address"].split())
        item["openingTime"] = response.xpath('normalize-space(/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[1]/dd[5])').extract_first()
        item["openingTime"] = "".join(item["openingTime"].split())
        item["consultationTelephone"] = "024-88338981"
        item["introduction"] = response.xpath('normalize-space(/html/body/div[3]/div[2]/div/div[1]/div[4])').extract_first()
        item["introduction"] = "" .join(item["introduction"]. split())
        item["publicityVideoLink"] = None
        item["longitude"] = "123.4741"
        item["latitude"] = "41.8429"
        print(item)
        yield item
