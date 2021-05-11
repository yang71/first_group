from ..items import *
from ..str_filter import *

from ..items import *
from ..str_filter import *


class Collection102(scrapy.Spider):
    name = "Collection102"
    allowed_domains = ['baike.baidu.com']
    start_urls = ['https://baike.baidu.com/item/%E6%99%AF%E5%BE%B7%E9%95%87%E9%99%B6%E7%93%B7%E9%A6%86/8981379?fr=aladdin']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        }
    }

    def parse(self, response, **kwargs):
        li_list = response.xpath("/html/body/div[3]/div[2]/div/div[1]/table//tr")
        print(len(li_list))
        for li in li_list:
            item = CollectionItem()
            item["museumID"] = 102
            item["museumName"] = "景德镇中国陶瓷博物馆"
            item['collectionName'] = li.xpath("./td/div/b").xpath('string(.)').extract_first()
            item['collectionImageLink'] = 'https://baike.baidu.com' + str(li.xpath(
                "./td/div/div/a/@href").extract_first())
            item['collectionIntroduction'] = StrFilter.filter(
                li.xpath("./td[1]/div[2]").xpath('string(.)').extract_first())

            print(item)
            yield(item)

