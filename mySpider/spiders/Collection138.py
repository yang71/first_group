#
from ..items import *
from ..str_filter import *

class Collection138(scrapy.Spider):
    name = "Collection138"
    allowed_domains = ['szbwg.net']
    start_urls = ['https://www.szbwg.net/list-10-1.html']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        }
    }

    def parse(self, response, **kwargs):
        li_list = response.xpath("/html/body/div[3]/div/div[2]/div/ul/li")
        print(len(li_list))
        for li in li_list:
            item = CollectionItem()
            item["museumID"] = 138
            item["museumName"] = "随州市博物馆"
            item['collectionName'] = li.xpath("./div/a/h2").xpath('string(.)').extract_first()
            item['collectionImageLink'] = str(li.xpath(
                "./a/i/img/@src").extract_first())
            item['collectionIntroduction'] = StrFilter.filter(
                li.xpath("./div/a/h2").xpath('string(.)').extract_first())
            print(item)
            yield(item)
