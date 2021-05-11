#
from ..items import *
from ..str_filter import *

class Collection104(scrapy.Spider):
    name = "Collection104"
    allowed_domains = ['qingdaomuseum.com']
    start_urls = ['http://www.qingdaomuseum.com/collection/category/16']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        }
    }

    def parse(self, response, **kwargs):
        li_list = response.xpath("/html/body/div[6]/div[2]/div/div[2]/div")
        print(len(li_list))
        for li in li_list:
            item = CollectionItem()
            item["museumID"] = 104
            item["museumName"] = "青岛市博物馆"
            item['collectionName'] = li.xpath(".//b").xpath('string(.)').extract_first()
            item['collectionImageLink'] = str(li.xpath(
                "./div/div/a/img/@src").extract_first())
            item['collectionIntroduction'] = StrFilter.filter(
                li.xpath("./div/p").xpath('string(.)').extract_first())
            print(item)
            yield(item)


