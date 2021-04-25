import scrapy as scrapy
import re

from ..items import *

class Museum53(scrapy.Spider):
    name = "Museum53"
    allowed_domains = ['baidu.com']
    start_urls = ['https://baike.baidu.com/item/%E9%99%88%E4%BA%91%E7%BA%AA%E5%BF%B5%E9%A6%86/14689064?fr=aladdin']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.MuseumPipeLine': 300,
        }
    }
    # 需要重写的部分
    def parse(self, response, **kwargs):
        r = re.compile(u"\\n|\\r|\\[.*?]|\\t")
        item = MuseumBasicInformationItem()
        item["museumID"] = 53
        item["museumName"] = response.xpath('normalize-space(/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[1]/dd[1])').extract_first()
        item["address"] = "上海市青浦区练塘镇朱枫公路3516号"
        item["openingTime"] = "周二至周日9：00-16：30（16：00停止领票进馆）"
        item["consultationTelephone"] = "021-59257178"
        item["introduction"] = response.xpath('normalize-space(/html/body/div[3]/div[2]/div/div[1]/div[4])').extract_first()
        item["introduction"] = "" .join(item["introduction"]. split())
        item["introduction"] = re.sub(r, '', item["introduction"])
        item["publicityVideoLink"] = None
        item["longitude"] = "121.0510"
        item["latitude"] = "31.0136"
        print(item)
        yield item
