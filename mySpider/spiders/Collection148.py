#
from ..items import *
from ..str_filter import *

class Collection148(scrapy.Spider):
    name = "Collection148"
    allowed_domains = ['baike.baidu.com']
    start_urls = ['https://baike.baidu.com/item/%E6%B7%B1%E5%9C%B3%E5%8D%9A%E7%89%A9%E9%A6%86/8703873?fr=aladdin#4']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        }
    }

    def parse(self, response, **kwargs):
        li_list = response.xpath("/html/body/div[3]/div[2]/div/div[1]/table//tr")
        print(len(li_list))
        for li in li_list[2:]:
            item = CollectionItem()
            item["museumID"] = 148
            item["museumName"] = "深圳博物馆"
            item['collectionName'] = li.xpath("./td[1]/div[1]/b[1]").xpath('string(.)').extract_first().replace('\n','')
            item['collectionImageLink'] = 'https://baike.baidu.com'+str(li.xpath(
                "./td[2]/div/div/a/@href").extract_first())
            item['collectionIntroduction'] = StrFilter.filter(
                li.xpath("./td[1]").xpath('string(.)').extract_first())
            print(item)
            yield(item)
