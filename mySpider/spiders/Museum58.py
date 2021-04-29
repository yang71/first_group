import scrapy as scrapy
import re

from ..items import *

class Museum58(scrapy.Spider):
    name = "Museum58"
    allowed_domains = ['baidu.com']
    start_urls = ['https://baike.baidu.com/item/%E5%8D%97%E9%80%9A%E5%8D%9A%E7%89%A9%E8%8B%91/1629642?fr=aladdin']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.MuseumPipeLine': 300,
        }
    }
    # 需要重写的部分
    def parse(self, response, **kwargs):
        r = re.compile(u"\\n|\\r|\\[.*?]|\\t")
        item = MuseumBasicInformationItem()
        item["museumID"] = 58
        item["museumName"] = response.xpath('normalize-space(/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[1]/dd[1])').extract_first()
        item["address"] = response.xpath('normalize-space(/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[1]/dd[3])').extract_first()
        item["address"] = "".join(item["address"].split())
        item["address"] = re.sub(r, '', item["address"])
        item["openingTime"] = response.xpath('normalize-space(/html/body/div[3]/div[2]/div/div[1]/div[84])').extract_first()
        item["openingTime"] = "".join(item["openingTime"].split())
        item["consultationTelephone"] = "0513-85062528"
        item["introduction"] = response.xpath('normalize-space(/html/body/div[3]/div[2]/div/div[1]/div[4])').extract_first()
        item["introduction"] = "" .join(item["introduction"]. split())
        item["introduction"] = re.sub(r, '', item["introduction"])
        item["publicityVideoLink"] = None
        item["longitude"] = "120.8752"
        item["latitude"] = "32.0185"
        print(item)
        yield item
