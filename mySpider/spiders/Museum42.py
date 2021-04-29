import scrapy as scrapy

from ..items import *

class Museum42(scrapy.Spider):
    name = "Museum42"
    allowed_domains = ['baidu.com']
    start_urls = ['https://baike.baidu.com/item/%E4%BC%AA%E6%BB%A1%E7%9A%87%E5%AE%AB%E5%8D%9A%E7%89%A9%E9%99%A2/2151196?fr=aladdin']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.MuseumPipeLine': 300,
        }
    }
    # 需要重写的部分
    def parse(self, response, **kwargs):
        item = MuseumBasicInformationItem()
        item["museumID"] = 42
        item["museumName"] = response.xpath('normalize-space(/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[1]/dd[1])').extract_first()
        item["address"] = response.xpath('normalize-space(/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[1]/dd[3])').extract_first()
        item["address"] = "".join(item["address"].split())
        item["openingTime"] = response.xpath('normalize-space(/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[2]/dd[3])').extract_first()
        item["openingTime"] = "".join(item["openingTime"].split())
        item["consultationTelephone"] = "0431-82866611"
        item["introduction"] = response.xpath('normalize-space(/html/body/div[3]/div[2]/div/div[1]/div[4])').extract_first()
        item["introduction"] = "" .join(item["introduction"]. split())
        item["publicityVideoLink"] = None
        item["longitude"] = "125.3553"
        item["latitude"] = "43.9107"
        print(item)
        yield item
