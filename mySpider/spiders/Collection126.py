#
from ..items import *
from ..str_filter import *

class Collection126(scrapy.Spider):
    name = "Collection126"
    allowed_domains = ['baike.baidu.com']
    start_urls = ['https://baike.baidu.com/item/%E5%BC%80%E5%B0%81%E5%B8%82%E5%8D%9A%E7%89%A9%E9%A6%86/1628889?fr=aladdin#3']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        }
    }

    def parse(self, response, **kwargs):
        li_list = response.xpath("/html/body/div[3]/div[2]/div/div[1]/table[2]//tr")
        print(len(li_list))
        for li in li_list[1:]:
            item = CollectionItem()
            item["museumID"] = 126
            item["museumName"] = "开封市博物馆"
            item['collectionName'] = li.xpath("./td[1]/div[1]/b").xpath('string(.)').extract_first()
            item['collectionImageLink'] = 'https://baike.baidu.com'+str(li.xpath(
                "./td[2]/div/div/a/@href").extract_first())
            item['collectionIntroduction'] = StrFilter.filter(
                li.xpath("./td[1]/div[2]/text()").extract_first())
            print(item)
            yield(item)
