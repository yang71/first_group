import scrapy as scrapy

from ..items import *

class Museum21(scrapy.Spider):
    name = "Museum21"
    allowed_domains = ['pjcmm.com']
    start_urls = ['http://www.pjcmm.com/home.aspx']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.MuseumPipeLine': 300,
        }
    }
    # 需要重写的部分
    def parse(self, response, **kwargs):
        item = MuseumBasicInformationItem()
        item["museumID"] = 21
        item["museumName"] = response.xpath('/html/head/title').xpath("string(.)").extract_first()
        item["address"] = "天津市红桥区平津道8号"
        item["openingTime"] = "周二至周日9:00至16:00，周一闭馆。"
        item["consultationTelephone"] = "022-26535412"
        item["introduction"] = response.xpath('/html/body/div[5]/div[2]/p[2]/a').xpath("string(.)").extract_first()
        item["publicityVideoLink"] = None
        item["longitude"] = "117.1531"
        item["latitude"] = "39.1747"
        # print(item)
        yield item
