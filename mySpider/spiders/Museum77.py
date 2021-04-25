#lay
from ..items import *


class Museum77(scrapy.Spider):
    name = "Museum77"
    allowed_domains = ['baike.baidu.com']
    start_urls = ['https://baike.baidu.com/item/%E6%9D%AD%E5%B7%9E%E5%B7%A5%E8%89%BA%E7%BE%8E%E6%9C%AF%E5%8D%9A%E7%89%A9%E9%A6%86/3726158?fr=aladdin']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.MuseumPipeLine': 300,
        }
    }

    def parse(self, response, **kwargs):
        item = MuseumBasicInformationItem()
        item["museumID"] = 77
        item["museumName"] = "杭州工艺美术博物馆"
        item["address"] = "杭州市拱墅区小河路334号"
        # str(response.xpath(
        # "/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[1]/dd[3]/text()").extract_first()).replace("\n", "")
        item["openingTime"] = "16:00停止进馆参观，周一全天闭馆（节假日除外）"
        # str(response.xpath(
        # "/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[2]/dd[3]/text()").extract_first()).replace("\n", "")
        item["consultationTelephone"] = "0571-88197511"
        item["publicityVideoLink"] = None
        item["longitude"] = "120.143317"
        item["latitude"] = "30.321879"
        item["introduction"] = response.xpath(
            '/html/body/div[3]/div[2]/div/div[1]/div[4]/div[1]/text()').extract()
        # str(response.xpath("/html/body/div[3]/div[2]/div/div[1]/div[4]/div[2]").xpath(
        # "string(.)").extract_first()).split("\n")[0]
        print(item)
        yield item
