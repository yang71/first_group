import scrapy as scrapy
import re

from ..items import *

class Museum64(scrapy.Spider):
    name = "Museum64"
    allowed_domains = ['baidu.com']
    start_urls = ['https://baike.baidu.com/item/%E9%9B%A8%E8%8A%B1%E5%8F%B0%E7%83%88%E5%A3%AB%E7%BA%AA%E5%BF%B5%E9%A6%86/4544039?fr=aladdin']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.MuseumPipeLine': 300,
        }
    }
    # 需要重写的部分
    def parse(self, response, **kwargs):
        r = re.compile(u"\\n|\\r|\\[.*?]|\\t")
        item = MuseumBasicInformationItem()
        item["museumID"] = 64
        item["museumName"] = response.xpath('normalize-space(/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[1]/dd[1])').extract_first()
        item["address"] = "南京市雨花台区雨花路215号雨花台风景名胜区烈士陵园区内"
        item["openingTime"] = response.xpath('normalize-space(/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[1]/dd[3])').extract_first()
        item["openingTime"] = "".join(item["openingTime"].split())
        item["consultationTelephone"] = "025-68783067"
        item["introduction"] = response.xpath('normalize-space(/html/body/div[3]/div[2]/div/div[1]/div[4])').extract_first()
        item["introduction"] = "" .join(item["introduction"]. split())
        item["introduction"] = re.sub(r, '', item["introduction"])
        item["publicityVideoLink"] = None
        item["longitude"] = "118.7860"
        item["latitude"] = "32.0083"
        print(item)
        yield item
