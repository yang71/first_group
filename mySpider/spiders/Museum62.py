import scrapy as scrapy
import re

from ..items import *

class Museum62(scrapy.Spider):
    name = "Museum62"
    allowed_domains = ['baidu.com']
    start_urls = ['https://baike.baidu.com/item/%E5%8D%97%E4%BA%AC%E5%B8%82%E5%8D%9A%E7%89%A9%E6%80%BB%E9%A6%86/19324216?fr=aladdin']

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
        item["museumID"] = 62
        item["museumName"] = response.xpath('normalize-space(/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[1]/dd[1])').extract_first()
        item["address"] = "南京市秦淮区王府大街朝天宫4号"
        item["openingTime"] = "开放时间：9:00—18:00（周一闭馆）"
        item["consultationTelephone"] = "025-84466460"
        item["introduction"] = response.xpath('normalize-space(/html/body/div[3]/div[2]/div/div[1]/div[4])').extract_first()
        item["introduction"] = "" .join(item["introduction"]. split())
        item["introduction"] = re.sub(r, '', item["introduction"])
        item["publicityVideoLink"] = None
        item["longitude"] = "118.7813"
        item["latitude"] = "32.0393"
        print(item)
        yield item
