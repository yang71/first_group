#
from ..items import *
from ..str_filter import *

class Collection128(scrapy.Spider):
    name = "Collection128"
    allowed_domains = ['baike.baidu.com']
    start_urls = ['https://baike.baidu.com/item/%E4%B8%AD%E5%9B%BD%E6%96%87%E5%AD%97%E5%8D%9A%E7%89%A9%E9%A6%86/11056750?fr=aladdin#3']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        }
    }

    def parse(self, response, **kwargs):
        li_list = response.xpath("/html/body/div[3]/div[2]/div/div[1]/table[2]//tr")
        print(len(li_list))
        for li in li_list[2:]:
            item = CollectionItem()
            item["museumID"] = 128
            item["museumName"] = "中国文字博物馆"
            item['collectionName'] = li.xpath("./td[1]/div/a").xpath('string(.)').extract_first()
            item['collectionImageLink'] = 'https://baike.baidu.com'+str(li.xpath(
                "./td[3]/div/div/a/@href").extract_first())
            item['collectionIntroduction'] = StrFilter.filter(
                li.xpath("./td[2]").xpath('string(.)').extract_first())
            print(item)
            yield(item)
