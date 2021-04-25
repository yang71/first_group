import scrapy as scrapy

from ..items import *

class Museum25(scrapy.Spider):
    name = "Museum25"
    allowed_domains = ['baidu.com']
    start_urls = ['https://baike.baidu.com/item/%E5%B1%B1%E8%A5%BF%E5%8D%9A%E7%89%A9%E9%99%A2/3165697?fr=aladdin']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.MuseumPipeLine': 300,
        }
    }
    # 需要重写的部分
    def parse(self, response, **kwargs):
        item = MuseumBasicInformationItem()
        item["museumID"] = 25
        item["museumName"] = response.xpath('normalize-space(/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[1]/dd[1])').extract_first()
        item["address"] = response.xpath('normalize-space(/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[1]/dd[3])').extract_first()
        item["openingTime"] = response.xpath("normalize-space(/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[1]/dd[5])").extract_first()
        item["consultationTelephone"] = "03518789188"
        item["introduction"] = response.xpath('normalize-space(/html/body/div[3]/div[2]/div/div[1]/div[4]/div[1])').extract_first()
        item["publicityVideoLink"] = None
        item["longitude"] = "112.5400"
        item["latitude"] = "37.8964"
        print(item)
        yield item
