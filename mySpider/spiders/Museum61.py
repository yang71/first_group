import scrapy as scrapy
import re

from ..items import *

class Museum61(scrapy.Spider):
    name = "Museum61"
    allowed_domains = ['baidu.com']
    start_urls = ['https://baike.baidu.com/item/%E5%B8%B8%E5%B7%9E%E5%8D%9A%E7%89%A9%E9%A6%86/1765322?fr=aladdin']

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
        item["museumID"] = 61
        item["museumName"] = response.xpath('normalize-space(/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[1]/dd[1])').extract_first()
        item["address"] = "常州市新北区龙城大道1288号"
        item["openingTime"] = "每日9:00-17:00(16:00停止入场),周一闭馆"
        item["consultationTelephone"] = "0519-85165080"
        item["introduction"] = response.xpath('normalize-space(/html/body/div[3]/div[2]/div/div[1]/div[4])').extract_first()
        item["introduction"] = "" .join(item["introduction"]. split())
        item["introduction"] = re.sub(r, '', item["introduction"])
        item["publicityVideoLink"] = None
        item["longitude"] = "119.9781"
        item["latitude"] = "31.8149"
        print(item)
        yield item
