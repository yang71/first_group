import scrapy as scrapy
import re

from ..items import *

class Museum54(scrapy.Spider):
    name = "Museum54"
    allowed_domains = ['baidu.com']
    start_urls = ['https://baike.baidu.com/item/%E4%B8%AD%E5%9B%BD%E8%88%AA%E6%B5%B7%E5%8D%9A%E7%89%A9%E9%A6%86/3946850?fr=aladdin']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.MuseumPipeLine': 300,
        }
    }
    # 需要重写的部分
    def parse(self, response, **kwargs):
        r = re.compile(u"\\n|\\r|\\[.*?]|\\t")
        item = MuseumBasicInformationItem()
        item["museumID"] = 54
        item["museumName"] = response.xpath('normalize-space(/html/body/div[3]/div[2]/div/div[1]/div[8]/dl[1]/dd[1])').extract_first()
        item["address"] = response.xpath('normalize-space(/html/body/div[3]/div[2]/div/div[1]/div[8]/dl[1]/dd[4])').extract_first()
        item["address"] = "".join(item["address"].split())
        item["openingTime"] = response.xpath('normalize-space(/html/body/div[3]/div[2]/div/div[1]/div[8]/dl[1]/dd[6])').extract_first()
        item["openingTime"] = "".join(item["openingTime"].split())
        item["consultationTelephone"] = "021-68283691"
        item["introduction"] = response.xpath('normalize-space(/html/body/div[3]/div[2]/div/div[1]/div[4])').extract_first()
        item["introduction"] = "" .join(item["introduction"]. split())
        item["introduction"] = re.sub(r, '', item["introduction"])
        item["publicityVideoLink"] = None
        item["longitude"] = "121.9259"
        item["latitude"] = "30.9033"
        print(item)
        yield item
