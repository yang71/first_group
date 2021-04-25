#lay
from ..items import *


class Museum88(scrapy.Spider):
    name = "Museum88"
    allowed_domains = ['fjbwy.com']
    start_urls = ['http://www.fjbwy.com/articles/2015-04-01/content_5806.html']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.MuseumPipeLine': 300,
        }
    }

    def parse(self, response, **kwargs):
        item = MuseumBasicInformationItem()
        item["museumID"] = 88
        item["museumName"] = "福建博物院"
        item["address"] = "福州市鼓楼区湖头街96号"
        # str(response.xpath(
        # "/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[1]/dd[3]/text()").extract_first()).replace("\n", "")
        item["openingTime"] = "9:00～17:00，16：00停止进场，周一闭馆"
        # str(response.xpath(
        # "/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[2]/dd[3]/text()").extract_first()).replace("\n", "")
        item["consultationTelephone"] = "0591-83757670"
        item["publicityVideoLink"] = None
        item["longitude"] = "119.293236"
        item["latitude"] = "26.100197"
        item["introduction"] = response.xpath(
            '/html/body/div[3]/div/div[4]/p[1]/span/text()').extract()
        print(item)
        yield item
