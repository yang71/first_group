#
from ..items import *
from ..str_filter import *

class Collection125(scrapy.Spider):
    name = "Collection125"
    allowed_domains = ['nyhhg.com']
    start_urls = ['http://nyhhg.com/a/xy/']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        }
    }

    def parse(self, response, **kwargs):
        li_list = response.xpath("/html/body/div[4]/div[2]/div[2]/dl/dd")
        print(len(li_list))
        for li in li_list[2:]:
            item = CollectionItem()
            item["museumID"] = 125
            item["museumName"] = "洛阳博物馆"
            item['collectionName'] = li.xpath("./div[2]/a").xpath('string(.)').extract_first()
            item['collectionImageLink'] = 'http://nyhhg.com'+str(li.xpath(
                "./div[1]/a/img/@src").extract_first())
            item['collectionIntroduction'] = StrFilter.filter(
                li.xpath("./div[2]/a").xpath('string(.)').extract_first())
            print(item)
            yield(item)
