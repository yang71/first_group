#
from ..items import *
from ..str_filter import *

class Collection137(scrapy.Spider):
    name = "Collection137"
    allowed_domains = ['ycbwg.com']
    start_urls = ['http://www.ycbwg.com/web/explore/collection/list.shtml']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        }
    }

    def parse(self, response, **kwargs):
        li_list = response.xpath("/html/body/div/div[1]/div[3]/div/div[2]/div[3]/div[1]/ul/li")
        print(len(li_list))
        for li in li_list:
            item = CollectionItem()
            item["museumID"] = 137
            item["museumName"] = "宜昌博物馆"
            item['collectionName'] = li.xpath("./div[2]/a/h5/span[1]").xpath('string(.)').extract_first().replace('\ue165于','')
            item['collectionImageLink'] = 'http://www.ycbwg.com'+str(li.xpath(
                "./div[1]/a/img/@src").extract_first())
            item['collectionIntroduction'] = StrFilter.filter(
                li.xpath("./div[2]/a/h5/span[1]").xpath('string(.)').extract_first()).replace('\ue165于','')
            print(item)
            yield(item)
