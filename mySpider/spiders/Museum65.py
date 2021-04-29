import scrapy as scrapy
import re

from ..items import *

class Museum65(scrapy.Spider):
    name = "Museum65"
    allowed_domains = ['baidu.com']
    start_urls = ['https://baike.baidu.com/item/%E6%97%A0%E9%94%A1%E5%8D%9A%E7%89%A9%E9%99%A2/5947063?fr=aladdin']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.MuseumPipeLine': 300,
        }
    }
    # 需要重写的部分
    def parse(self, response, **kwargs):
        r = re.compile(u"\\n|\\r|\\[.*?]|\\t")
        item = MuseumBasicInformationItem()
        item["museumID"] = 65
        item["museumName"] = response.xpath('normalize-space(/html/body/div[3]/div[2]/div/div[1]/div[8]/dl[1]/dd[1])').extract_first()
        item["address"] = response.xpath('normalize-space(/html/body/div[3]/div[2]/div/div[1]/div[8]/dl[1]/dd[5])').extract_first()
        item["address"] = "".join(item["address"].split())
        item["openingTime"] = response.xpath('normalize-space(/html/body/div[3]/div[2]/div/div[1]/div[8]/dl[1]/dd[3])').extract_first()
        item["openingTime"] = "".join(item["openingTime"].split())
        item["consultationTelephone"] = "0510-85727500"
        item["introduction"] = response.xpath('normalize-space(/html/body/div[3]/div[2]/div/div[1]/div[4])').extract_first()
        item["introduction"] = "" .join(item["introduction"]. split())
        item["introduction"] = re.sub(r, '', item["introduction"])
        item["publicityVideoLink"] = None
        item["longitude"] = "120.3129"
        item["latitude"] = "31.5553"
        print(item)
        yield item
