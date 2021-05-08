#
from ..items import *
from ..str_filter import *

class Collection122(scrapy.Spider):
    name = "Collection122"
    allowed_domains = ['baike.baidu.com']
    start_urls = ['https://baike.baidu.com/item/%E6%B2%B3%E5%8D%97%E5%8D%9A%E7%89%A9%E9%99%A2/529742?fr=aladdin']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        }
    }

    def parse(self, response, **kwargs):
        li_list = response.xpath("/html/body/div[3]/div[2]/div/div[1]/div")
        print(len(li_list))
        for li in li_list[41:]:
            item = CollectionItem()
            item["museumID"] = 122
            item["museumName"] = "河南博物院"
            item['collectionName'] = li.xpath("./h3/text()").extract_first()
            item['collectionImageLink'] = str(li.xpath(
                "./div/a/img/@src").extract_first())
            item['collectionIntroduction'] = StrFilter.filter(
                li.xpath("./text()").extract_first())
            print(item)
            yield(item)
