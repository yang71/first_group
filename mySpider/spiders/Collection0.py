from ..items import *


class Collection0(scrapy.Spider):
    name = "Collection0"
    allowed_domains = ['dpm.org.cn']
    start_urls = ['https://www.dpm.org.cn/shows.html']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        }
    }

    def parse(self, response, **kwargs):
        # li_list = response.xpath("//div[@id='temporary_5']/div[@class='temporary5']")
        # for li in li_list:
        item = CollectionItem()
        item["museumID"] = 0
        item["museumName"] = "故宫博物院"
        item["collectionName"] = "test"
        item["collectionImageLink"] = "test"
        item["collectionIntroduction"] = 456
        print(item)
        yield item
