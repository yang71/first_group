#
from ..items import *
from ..str_filter import *

class Collection135(scrapy.Spider):
    name = "Collection135"
    allowed_domains = ['whgmbwg.com']
    start_urls = ['http://www.whgmbwg.com/gzjx/wwjc/index.shtml']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        }
    }

    def parse(self, response, **kwargs):
        li_list = response.xpath("/html/body/div[3]/div[5]/div[1]/ul/li")
        print(len(li_list))
        for li in li_list[0:]:
            item = CollectionItem()
            item["museumID"] = 135
            item["museumName"] = "武汉革命博物馆"
            item['collectionName'] = li.xpath("./div[1]/a").xpath('string(.)').extract_first()
            item['collectionImageLink'] = 'http://www.whgmbwg.com'+str(li.xpath(
                "./a/img/@src").extract_first())
            item['collectionIntroduction'] = StrFilter.filter(
                li.xpath("./div[1]/a").xpath('string(.)').extract_first())
            print(item)
            yield(item)
