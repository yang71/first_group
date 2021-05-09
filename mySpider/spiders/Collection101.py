from ..items import *
from ..str_filter import *

from ..items import *
from ..str_filter import *


class Collection101(scrapy.Spider):
    name = "Collection101"
    allowed_domains = ['gzsbwg.cn']
    start_urls = ['http://www.gzsbwg.cn/html/infolist-32.html']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        }
    }

    def parse(self, response, **kwargs):
        li_list = response.xpath("/html/body/div[5]/div/div/a")
        print(len(li_list))
        for li in li_list:
            item = CollectionItem()
            item["museumID"] = 101
            item["museumName"] = "赣州市博物馆"
            item['collectionName'] = li.xpath("./span").xpath('string(.)').extract_first()
            item['collectionImageLink'] = 'http://www.gzsbwg.cn' + str(li.xpath(
                "./img/@src").extract_first())
            item['collectionIntroduction'] = StrFilter.filter(
                li.xpath("./span").xpath('string(.)').extract_first())
            print(item)
            yield(item)

