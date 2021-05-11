#
from ..items import *
from ..str_filter import *

class Collection117(scrapy.Spider):
    name = "Collection117"
    allowed_domains = ['qiheritagemuseum.com']
    start_urls = ['http://www.qiheritagemuseum.com/product/5/']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        }
    }

    def parse(self, response, **kwargs):
        li_list = response.xpath("//*[@id='c_product_list-15953191985489561']/div/div[1]/div")
        print(len(li_list))
        for li in li_list[1:]:
            item = CollectionItem()
            item["museumID"] = 117
            item["museumName"] = "淄博市陶瓷博物馆"
            item['collectionName'] = li.xpath("./a[2]").xpath('string(.)').extract_first().replace('\t', '').replace('\n', '').replace(' ', '')
            item['collectionImageLink'] = str(li.xpath(
                "./div[1]/img/@src").extract_first())
            item['collectionIntroduction'] = StrFilter.filter(
                li.xpath("./div[2]/div[2]").xpath('string(.)').extract_first())
            print(item)
            yield(item)
