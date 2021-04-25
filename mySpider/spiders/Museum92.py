#lay
from ..items import *


class Museum92(scrapy.Spider):
    name = "Museum92"
    allowed_domains = ['baike.baidu.com']
    start_urls = ['https://baike.baidu.com/item/%E4%B8%AD%E5%A4%AE%E8%8B%8F%E5%8C%BA%EF%BC%88%E9%97%BD%E8%A5%BF%EF%BC%89%E5%8E%86%E5%8F%B2%E5%8D%9A%E7%89%A9%E9%A6%86/22107463?fr=aladdin']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.MuseumPipeLine': 300,
        }
    }

    def parse(self, response, **kwargs):
        item = MuseumBasicInformationItem()
        item["museumID"] = 92
        item["museumName"] = "中央苏区（闽西）历史博物馆"
        item["address"] = "龙岩市新罗区北环西路51号"
        # str(response.xpath(
        # "/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[1]/dd[3]/text()").extract_first()).replace("\n", "")
        item["openingTime"] = "星期二到星期日上午8：15到11：45，下午2：15到5：15，夏季：上午不变，下午3：00到5：45，实行免费开放,闭馆时间：每星期一"
        # str(response.xpath(
        # "/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[2]/dd[3]/text()").extract_first()).replace("\n", "")
        item["consultationTelephone"] = "0597－2291479"
        item["publicityVideoLink"] = None
        item["longitude"] = "117.030617"
        item["latitude"] = "25.108544"
        item["introduction"] = response.xpath(
            '/html/body/div[3]/div[2]/div/div[1]/div[4]/div[2]/text()[1]').extract()
        print(item)
        yield item
