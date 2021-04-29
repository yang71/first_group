import scrapy as scrapy

from ..items import *

class Museum36(scrapy.Spider):
    name = "Museum36"
    allowed_domains = ['baidu.com']
    start_urls = ['https://baike.baidu.com/item/%E6%97%85%E9%A1%BA%E5%8D%9A%E7%89%A9%E9%A6%86/1630157?fr=aladdin']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.MuseumPipeLine': 300,
        }
    }
    # 需要重写的部分
    def parse(self, response, **kwargs):
        item = MuseumBasicInformationItem()
        item["museumID"] = 36
        item["museumName"] = response.xpath('normalize-space(/html/body/div[3]/div[2]/div/div[1]/div[8]/dl[1]/dd[1])').extract_first()
        item["address"] = response.xpath('normalize-space(/html/body/div[3]/div[2]/div/div[1]/div[8]/dl[1]/dd[6])').extract_first()
        item["address"] = "".join(item["address"].split())
        item["openingTime"] = response.xpath('normalize-space(/html/body/div[3]/div[2]/div/div[1]/div[72])').extract_first()
        item["openingTime"] = "".join(item["openingTime"].split())
        item["consultationTelephone"] = "0411-86383334"
        item["introduction"] = response.xpath('normalize-space(/html/body/div[3]/div[2]/div/div[1]/div[4])').extract_first()
        item["introduction"] = "" .join(item["introduction"]. split())
        item["publicityVideoLink"] = None
        item["longitude"] = "121.2403"
        item["latitude"] = "38.8147"
        print(item)
        yield item
