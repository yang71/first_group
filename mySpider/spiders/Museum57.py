import scrapy as scrapy
import re

from ..items import *

class Museum57(scrapy.Spider):
    name = "Museum57"
    allowed_domains = ['baidu.com']
    start_urls = ['https://baike.baidu.com/item/%E4%BE%B5%E5%8D%8E%E6%97%A5%E5%86%9B%E5%8D%97%E4%BA%AC%E5%A4%A7%E5%B1%A0%E6%9D%80%E9%81%87%E9%9A%BE%E5%90%8C%E8%83%9E%E7%BA%AA%E5%BF%B5%E9%A6%86/3508930?fr=aladdin']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.MuseumPipeLine': 300,
        }
    }
    # 需要重写的部分
    def parse(self, response, **kwargs):
        r = re.compile(u"\\n|\\r|\\[.*?]|\\t")
        item = MuseumBasicInformationItem()
        item["museumID"] = 57
        item["museumName"] = response.xpath('normalize-space(/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[1]/dd[1])').extract_first()
        item["address"] = response.xpath('normalize-space(/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[1]/dd[3])').extract_first()
        item["address"] = "".join(item["address"].split())
        item["openingTime"] = response.xpath('normalize-space(/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[1]/dd[5])').extract_first()
        item["openingTime"] = "".join(item["openingTime"].split())
        item["openingTime"] = re.sub(r, '', item["openingTime"])
        item["consultationTelephone"] = "025-86612230"
        item["introduction"] = response.xpath('normalize-space(/html/body/div[3]/div[2]/div/div[1]/div[4])').extract_first()
        item["introduction"] = "" .join(item["introduction"]. split())
        item["introduction"] = re.sub(r, '', item["introduction"])
        item["publicityVideoLink"] = None
        item["longitude"] = "118.7514"
        item["latitude"] = "32.0406"
        print(item)
        yield item
