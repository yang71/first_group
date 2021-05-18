import scrapy as scrapy
import re

from ..items import *

class Museum51(scrapy.Spider):
    name = "Museum51"
    allowed_domains = ['baidu.com']
    start_urls = ['https://baike.baidu.com/item/%E4%B8%AD%E5%9B%BD%E5%85%B1%E4%BA%A7%E5%85%9A%E7%AC%AC%E4%B8%80%E6%AC%A1%E5%85%A8%E5%9B%BD%E4%BB%A3%E8%A1%A8%E5%A4%A7%E4%BC%9A%E4%BC%9A%E5%9D%80/1164711?fr=aladdin']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.MuseumPipeLine': 300,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.DefaultMiddleware': 0,
        },
    }
    # 需要重写的部分
    def parse(self, response, **kwargs):
        r = re.compile(u"\\n|\\r|\\[.*?]|\\t")
        item = MuseumBasicInformationItem()
        item["museumID"] = 51
        item["museumName"] = response.xpath('normalize-space(/html/body/div[3]/div[2]/div/div[1]/div[8]/dl[1]/dd[1])').extract_first()
        item["address"] = response.xpath('normalize-space(/html/body/div[3]/div[2]/div/div[1]/div[8]/dl[1]/dd[3])').extract_first()
        item["address"] = "".join(item["address"].split())
        item["openingTime"] = "9:00—17:00(16:00停止进场)周一闭馆"
        item["consultationTelephone"] = "021-53832171"
        item["introduction"] = response.xpath('normalize-space(/html/body/div[3]/div[2]/div/div[1]/div[4])').extract_first()
        item["introduction"] = "" .join(item["introduction"]. split())
        item["introduction"] = re.sub(r, '', item["introduction"])
        item["publicityVideoLink"] = None
        item["longitude"] = "121.4820"
        item["latitude"] = "31.2261"
        print(item)
        yield item
