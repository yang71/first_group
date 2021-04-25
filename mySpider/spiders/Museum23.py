import scrapy as scrapy

from ..items import *

class Museum23(scrapy.Spider):
    name = "Museum23"
    allowed_domains = ['baidu.com']
    start_urls = ['https://baike.baidu.com/item/%E8%A5%BF%E6%9F%8F%E5%9D%A1%E7%BA%AA%E5%BF%B5%E9%A6%86/2504558?fr=aladdin']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.MuseumPipeLine': 300,
        }
    }
    # 需要重写的部分
    def parse(self, response, **kwargs):
        item = MuseumBasicInformationItem()
        item["museumID"] = 23
        item["museumName"] = response.xpath('/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[1]/dd[1]').xpath("string(.)").extract_first()
        item["address"] = response.xpath('/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[1]/dd[3]').xpath("string(.)").extract_first()
        item["openingTime"] = "每周二至周日上午9:30-17：00（16：30停止入馆），周一闭馆。"
        item["consultationTelephone"] = "0311-82851355"
        item["introduction"] = response.xpath("/html/body/div[3]/div[2]/div/div[1]/div[4]/div[1]").xpath("string(.)").extract_first()
        item["publicityVideoLink"] = None
        item["longitude"] = "113.9514"
        item["latitude"] = "38.3455"
        print(item)
        yield item
