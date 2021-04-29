import scrapy as scrapy
import re

from ..items import *

class Museum50(scrapy.Spider):
    name = "Museum50"
    allowed_domains = ['baidu.com']
    start_urls = ['https://baike.baidu.com/item/%E4%B8%8A%E6%B5%B7%E9%B2%81%E8%BF%85%E7%BA%AA%E5%BF%B5%E9%A6%86/3862098?fr=aladdin']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.MuseumPipeLine': 300,
        }
    }
    # 需要重写的部分
    def parse(self, response, **kwargs):
        r = re.compile(u"\\n|\\r|\\[.*?]|\\t")
        item = MuseumBasicInformationItem()
        item["museumID"] = 50
        item["museumName"] = response.xpath('normalize-space(/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[1]/dd[1])').extract_first()
        item["address"] = response.xpath('normalize-space(/html/body/div[3]/div[2]/div/div[1]/div[67])').extract_first()
        item["address"] = "".join(item["address"].split())
        item["openingTime"] = response.xpath('normalize-space(/html/body/div[3]/div[2]/div/div[1]/div[70])').extract_first()
        item["openingTime"] = "".join(item["openingTime"].split())
        item["consultationTelephone"] = "86-21-65402288"
        item["introduction"] = response.xpath('normalize-space(/html/body/div[3]/div[2]/div/div[1]/div[4])').extract_first()
        item["introduction"] = "" .join(item["introduction"]. split())
        item["introduction"] = re.sub(r, '', item["introduction"])
        item["publicityVideoLink"] = None
        item["longitude"] = "121.4908"
        item["latitude"] = "31.2751"
        print(item)
        yield item
