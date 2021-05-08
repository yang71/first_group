from ..items import *
from ..str_filter import *


class Collection43(scrapy.Spider):
    name = "Collection100"
    allowed_domains = ['lushanmuseum.com']
    start_urls = ['http://www.lushanmuseum.com/jingpin.asp?id=35']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        }
    }

    def parse(self, response, **kwargs):
        li_list = response.xpath("/html/body/div/div/div/div/div[2]/ul/li[1]/div")
        print(len(li_list))
        for li in li_list:
            item = CollectionItem()
            item["museumID"] = 100
            item["museumName"] = "庐山博物馆"
            item['collectionName'] = StrFilter.filter(
                li.xpath("/html/body/div/div/div/div/div[2]/ul/li/div/p/span").extract_first()).replace('[', '').replace(']', '')

            item['collectionImageLink'] = 'https://baike.baidu.com' + str(li.xpath(
                "./td[1]/div[1]/div[1]/a/@href").extract_first())

            def parseAnotherPage(self, response):
                item = response.meta["item"]
                item['collectionIntroduction'] = StrFilter.filter(
                    response.xpath("/html/body/div/div[2]/div[1]/div[2]/div[2]/div/div/div/div[3]").xpath(
                        'string(.)').extract_first())
                print(item)
                yield item
