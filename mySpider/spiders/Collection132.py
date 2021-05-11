#
from ..items import *
from ..str_filter import *

class Collection132(scrapy.Spider):
    name = "Collection132"
    allowed_domains = ['jzmsm.org']
    start_urls = ['http://www.jzmsm.org/yk/cangpin/guobaoxinshang/']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        }
    }

    def parse(self, response, **kwargs):
        li_list = response.xpath("/html/body/div[3]/ul/li")
        print(len(li_list))
        for li in li_list[1:]:
            item = CollectionItem()
            item["museumID"] = 132
            item["museumName"] = "荆州博物馆"
            item['collectionName'] = li.xpath("./a[2]").xpath('string(.)').extract_first().replace('：','')
            item['collectionImageLink'] = 'http://www.jzmsm.org'+str(li.xpath(
                "./a[1]/@href").extract_first())
            item['collectionIntroduction'] = StrFilter.filter(
                li.xpath("./a[2]").xpath('string(.)').extract_first())
            print(item)
            yield(item)
