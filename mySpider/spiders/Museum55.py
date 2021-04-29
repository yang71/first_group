import scrapy as scrapy
import re

from ..items import *

class Museum55(scrapy.Spider):
    name = "Museum55"
    allowed_domains = ['baidu.com']
    start_urls = ['https://baike.baidu.com/item/%E9%BE%99%E5%8D%8E%E7%83%88%E5%A3%AB%E7%BA%AA%E5%BF%B5%E9%A6%86/4441488?fr=aladdin']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.MuseumPipeLine': 300,
        }
    }
    # 需要重写的部分
    def parse(self, response, **kwargs):
        r = re.compile(u"\\n|\\r|\\[.*?]|\\t")
        item = MuseumBasicInformationItem()
        item["museumID"] = 55
        item["museumName"] = response.xpath('normalize-space(/html/body/div[3]/div[2]/div/div[1]/div[8]/dl[1]/dd[1])').extract_first()
        item["address"] = response.xpath('normalize-space(/html/body/div[3]/div[2]/div/div[1]/div[8]/dl[2]/dd[1])').extract_first()
        item["address"] = "".join(item["address"].split())
        item["openingTime"] = response.xpath('normalize-space(/html/body/div[3]/div[2]/div/div[1]/div[34])').extract_first()
        item["openingTime"] = "".join(item["openingTime"].split())
        item["consultationTelephone"] = "021-64685995"
        item["introduction"] = response.xpath('normalize-space(/html/body/div[3]/div[2]/div/div[1]/div[4])').extract_first()
        item["introduction"] = "" .join(item["introduction"]. split())
        item["introduction"] = re.sub(r, '', item["introduction"])
        item["publicityVideoLink"] = None
        item["longitude"] = "110.3355"
        item["latitude"] = "20.0363"
        print(item)
        yield item
