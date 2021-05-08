#
from ..items import *
from ..str_filter import *

class Collection107(scrapy.Spider):
    name = "Collection107"
    allowed_domains = ['sdmuseum.com']
    start_urls = ['http://www.sdmuseum.com/channels/ch00079/']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        }
    }

    def parse(self, response, **kwargs):
        li_list = response.xpath("/html/body/div[3]/div[2]/table//tr/td/table//tr[4]/td/table//tr/td")
        print(len(li_list))
        for li in li_list:
            item = CollectionItem()
            item["museumID"] = 107
            item["museumName"] = "山东省博物馆"
            item['collectionName'] = li.xpath("./div/div[2]/a").xpath('string(.)').extract_first()
            item['collectionImageLink'] = 'http://www.sdmuseum.com'+str(li.xpath(
                "./div/div[1]/a/img/@src").extract_first())
            item['collectionIntroduction'] = StrFilter.filter(
                li.xpath("./div/div[2]/a").xpath('string(.)').extract_first())
            print(item)
            yield(item)
