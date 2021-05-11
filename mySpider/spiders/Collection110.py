#
from ..items import *
from ..str_filter import *

class Collection110(scrapy.Spider):
    name = "Collection110"
    allowed_domains = ['ytmuseum.com']
    start_urls = ['http://www.kzbwg.cn/diancang/zhenpin/sh/']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        }
    }

    def parse(self, response, **kwargs):
        li_list = response.xpath("/html/body/div[6]/div/div/div[2]/div")
        print(len(li_list))
        for li in li_list[2:]:
            item = CollectionItem()
            item["museumID"] = 110
            item["museumName"] = "孔子博物馆"
            item['collectionName'] = li.xpath("./div/h3/a").xpath('string(.)').extract_first()
            item['collectionImageLink'] = 'http://www.kzbwg.cn' + str(li.xpath(
                "./a/img/@src").extract_first())
            item['collectionIntroduction'] = StrFilter.filter(
                li.xpath("./div/p").xpath('string(.)').extract_first())
            print(item)
            yield(item)
