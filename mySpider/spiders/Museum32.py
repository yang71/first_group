import scrapy as scrapy

from ..items import *

class Museum32(scrapy.Spider):
    name = "Museum32"
    allowed_domains = ['baidu.com']
    start_urls = ['https://baike.baidu.com/item/%E9%84%82%E5%B0%94%E5%A4%9A%E6%96%AF%E5%8D%9A%E7%89%A9%E9%A6%86/4468890?fr=aladdin']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.MuseumPipeLine': 300,
        }
    }
    # 需要重写的部分
    def parse(self, response, **kwargs):
        item = MuseumBasicInformationItem()
        item["museumID"] = 32
        item["museumName"] = response.xpath('normalize-space(/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[1]/dd[1])').extract_first()
        item["address"] = response.xpath('normalize-space(/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[2]/dd[1])').extract_first()
        item["address"] = "".join(item["address"].split())
        item["openingTime"] = response.xpath('normalize-space(/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[1]/dd[4])').extract_first()
        item["openingTime"] = "".join(item["openingTime"].split())
        item["consultationTelephone"] = None
        item["introduction"] = response.xpath('normalize-space(/html/body/div[3]/div[2]/div/div[1]/div[4]/div)').extract_first()
        item["introduction"] = "" .join(item["introduction"]. split())
        item["publicityVideoLink"] = None
        item["longitude"] = "109.7914"
        item["latitude"] = "39.6073"
        print(item)
        yield item
