#
from ..items import *
from ..str_filter import *

class Collection129(scrapy.Spider):
    name = "Collection129"
    allowed_domains = ['pdsm.org.cn']
    start_urls = ['http://www.pdsm.org.cn/front/collection/browsecollection.html']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        }
    }

    def parse(self, response, **kwargs):
        li_list = response.xpath("/html/body/div[3]/div[4]/ul/li")
        print(len(li_list))
        for li in li_list[2:]:
            item = CollectionItem()
            item["museumID"] = 129
            item["museumName"] = "平顶山博物馆"
            item['collectionName'] = li.xpath("./div/p/a").xpath('string(.)').extract_first()
            item['collectionImageLink'] = 'http://www.pdsm.org.cn'+str(li.xpath(
                "./div/span/a/@href").extract_first())
            item['collectionIntroduction'] = StrFilter.filter(
                li.xpath("./div/p/a").xpath('string(.)').extract_first())
            print(item)
            yield(item)
