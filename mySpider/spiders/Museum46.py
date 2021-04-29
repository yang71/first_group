import scrapy as scrapy
import re

from ..items import *

class Museum46(scrapy.Spider):
    name = "Museum46"
    allowed_domains = ['baidu.com']
    start_urls = ['https://baike.baidu.com/item/%E9%BB%91%E9%BE%99%E6%B1%9F%E7%9C%81%E5%8D%9A%E7%89%A9%E9%A6%86/1629873?fr=aladdin']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.MuseumPipeLine': 300,
        }
    }
    # 需要重写的部分
    def parse(self, response, **kwargs):
        r = re.compile(u"\\n|\\r|\\[.*?]|\\t")
        item = MuseumBasicInformationItem()
        item["museumID"] = 46
        item["museumName"] = response.xpath('normalize-space(/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[1]/dd[1])').extract_first()
        item["address"] = response.xpath('normalize-space(/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[2]/dd[1])').extract_first()
        item["address"] = "".join(item["address"].split())
        item["openingTime"] = response.xpath('normalize-space(/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[1]/dd[4])').extract_first()
        item["openingTime"] = "".join(item["openingTime"].split())
        item["consultationTelephone"] = "0451-53644151"
        item["introduction"] = response.xpath('normalize-space(/html/body/div[3]/div[2]/div/div[1]/div[4])').extract_first()
        item["introduction"] = "" .join(item["introduction"]. split())
        item["introduction"] = re.sub(r, '', item["introduction"])
        item["publicityVideoLink"] = None
        item["longitude"] = "126.6412"
        item["latitude"] = "45.7575"
        print(item)
        yield item
