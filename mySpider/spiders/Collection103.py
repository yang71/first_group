from ..items import *
from ..str_filter import *

from ..items import *
from ..str_filter import *


class Collection103(scrapy.Spider):
    name = "Collection103"
    allowed_domains = ['baike.baidu.com']
    start_urls = ['https://baike.baidu.com/item/%E8%90%8D%E4%B9%A1%E5%8D%9A%E7%89%A9%E9%A6%86/1663230?fr=aladdin']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        }
    }

    def parse(self, response, **kwargs):
        li_list = response.xpath("/html/body/div[3]/div[2]/div/div[1]/table[1]//tr/td")
        print(len(li_list))
        for li in li_list:
            item = CollectionItem()
            item["museumID"] = 103
            item["museumName"] = "萍乡博物馆"
            item['collectionName'] = li.xpath("./div[2]").xpath('string(.)').extract_first()
            item['collectionImageLink'] = 'https://baike.baidu.com'+str(li.xpath(
                "./div[1]/div/a/@href").extract_first())
            item['collectionIntroduction'] = StrFilter.filter(
                li.xpath("./div[3]").xpath('string(.)').extract_first())
            print(item)
            yield(item)


