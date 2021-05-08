#
from ..items import *
from ..str_filter import *

class Collection131(scrapy.Spider):
    name = "Collection131"
    allowed_domains = ['baike.baidu.com']
    start_urls = ['https://baike.baidu.com/item/%E6%B9%96%E5%8C%97%E7%9C%81%E5%8D%9A%E7%89%A9%E9%A6%86/938188?fr=aladdin#3_1']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        }
    }

    def parse(self, response, **kwargs):
        li_list = response.xpath("/html/body/div[3]/div[2]/div/div[1]/table[1]//tr")
        print(len(li_list))
        for li in li_list[1:]:
            item = CollectionItem()
            item["museumID"] = 131
            item["museumName"] = "湖北省博物馆"
            item['collectionName'] = li.xpath("./td[2]/div/b").xpath('string(.)').extract_first().replace('：','')
            item['collectionImageLink'] = 'https://baike.baidu.com'+str(li.xpath(
                "./td[1]/div/div/a/@href").extract_first())
            item['collectionIntroduction'] = StrFilter.filter(
                li.xpath(".Collection131.py/td[2]/div").xpath('string(.)').extract_first())
            print(item)
            yield(item)
