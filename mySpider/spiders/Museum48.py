import scrapy as scrapy
import re

from ..items import *

class Museum48(scrapy.Spider):
    name = "Museum48"
    allowed_domains = ['baidu.com']
    start_urls = ['https://baike.baidu.com/item/%E9%BB%91%E9%BE%99%E6%B1%9F%E7%9C%81%E6%B0%91%E6%97%8F%E5%8D%9A%E7%89%A9%E9%A6%86/2887345?fr=aladdin']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.MuseumPipeLine': 300,
        }
    }
    # 需要重写的部分
    def parse(self, response, **kwargs):
        r = re.compile(u"\\n|\\r|\\[.*?]|\\t")
        item = MuseumBasicInformationItem()
        item["museumID"] = 48
        item["museumName"] = response.xpath('normalize-space(/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[1]/dd[1])').extract_first()
        item["address"] = response.xpath('normalize-space(/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[1]/dd[3])').extract_first()
        item["address"] = "".join(item["address"].split())
        item["openingTime"] = "8:30-16:30(每周一闭馆)"
        item["consultationTelephone"] = "0451—82540093"
        item["introduction"] = response.xpath('normalize-space(/html/body/div[3]/div[2]/div/div[1]/div[4])').extract_first()
        item["introduction"] = "" .join(item["introduction"]. split())
        item["introduction"] = re.sub(r, '', item["introduction"])
        item["publicityVideoLink"] = None
        item["longitude"] = "126.6820"
        item["latitude"] = "45.7804"
        print(item)
        yield item
