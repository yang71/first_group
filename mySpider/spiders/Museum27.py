import scrapy as scrapy

from ..items import *

class Museum27(scrapy.Spider):
    name = "Museum27"
    allowed_domains = ['baidu.com']
    start_urls = ['https://baike.baidu.com/item/%E5%85%AB%E8%B7%AF%E5%86%9B%E5%A4%AA%E8%A1%8C%E7%BA%AA%E5%BF%B5%E9%A6%86/1793514?fr=aladdin']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.MuseumPipeLine': 300,
        }
    }
    # 需要重写的部分
    def parse(self, response, **kwargs):
        item = MuseumBasicInformationItem()
        item["museumID"] = 27
        item["museumName"] = response.xpath('normalize-space(//html/body/div[3]/div[2]/div/div[1]/div[7]/dl[1]/dd[1])').extract_first()
        item["address"] = response.xpath('normalize-space(/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[1]/dd[2])').extract_first()
        item["openingTime"] = response.xpath('normalize-space(/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[1]/dd[3])').extract_first()
        item["consultationTelephone"] = "0355-5543661"
        item["introduction"] = response.xpath('normalize-space(/html/body/div[3]/div[2]/div/div[1]/div[4]/div[1])').extract_first()
        item["introduction"] = "" .join(item["introduction"]. split())
        item["publicityVideoLink"] = None
        item["longitude"] = "112.8625"
        item["latitude"] = "36.8388"
        print(item)
        yield item
