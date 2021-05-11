#
from ..items import *
from ..str_filter import *

class Collection108(scrapy.Spider):
    name = "Collection108"
    allowed_domains = ['ytmuseum.com']
    start_urls = ['http://www.ytmuseum.com/collection/zg']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        }
    }

    def parse(self, response, **kwargs):
        li_list = response.xpath("/html/body/div[2]/div[3]/div[2]/div[2]/ul/li")
        print(len(li_list))
        for li in li_list:
            item = CollectionItem()
            item["museumID"] = 108
            item["museumName"] = "烟台市博物馆"
            item['collectionName'] = li.xpath("./div[1]").xpath('string(.)').extract_first()
            item['collectionImageLink'] = 'http:' + str(li.xpath(
                "./div[2]/div[1]/a/img/@src").extract_first())
            item['collectionIntroduction'] = StrFilter.filter(
                li.xpath("./div[2]/div[2]").xpath('string(.)').extract_first())
            print(item)
            yield(item)
