#
from ..items import *
from ..str_filter import *

class Collection109(scrapy.Spider):
    name = "Collection109"
    allowed_domains = ['wfsbwg.com']
    start_urls = ['http://www.wfsbwg.com/list/?5_1.html']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        }
    }

    def parse(self, response, **kwargs):
        li_list = response.xpath("/html/body/div[7]/div[2]/div[2]/div[1]/ul/li")
        print(len(li_list))
        for li in li_list:
            item = CollectionItem()
            item["museumID"] = 109
            item["museumName"] = "潍坊市博物馆"
            item['collectionName'] = li.xpath("./div/a/@title").extract_first()
            item['collectionImageLink'] = 'http://www.wfsbwg.com' + str(li.xpath(
                "./div/a/img/@src").extract_first())
            item['collectionIntroduction'] = StrFilter.filter(
                li.xpath("./div/a/@title").extract_first())
            print(item)
            yield(item)
