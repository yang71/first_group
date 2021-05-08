#
from ..items import *
from ..str_filter import *

class Collection118(scrapy.Spider):
    name = "Collection118"
    allowed_domains = ['tengzhoumuseum.com']
    start_urls = ['http://www.tengzhoumuseum.com/productlist/list-10-1.html']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        }
    }

    def parse(self, response, **kwargs):
        li_list = response.xpath("/html/body/table[4]//tr/td[3]/table//tr[1]/td/table[2]//tr[1]/td/table")
        print(len(li_list))
        for li in li_list[1:]:
            item = CollectionItem()
            item["museumID"] = 118
            item["museumName"] = "滕州市博物馆"
            item['collectionName'] = li.xpath(".//tr[2]/td/a").xpath('string(.)').extract_first()
            item['collectionImageLink'] = 'http://www.zbstcbwg.cn' + str(li.xpath(
                ".//tr[1]/td/a/img/@src").extract_first())
            item['collectionIntroduction'] = StrFilter.filter(
                li.xpath(".//tr[2]/td/a").xpath('string(.)').extract_first())
            print(item)
            yield(item)
