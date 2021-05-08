#
from ..items import *
from ..str_filter import *

class Collection134(scrapy.Spider):
    name = "Collection134"
    allowed_domains = ['baike.baidu.com']
    start_urls = ['https://baike.baidu.com/item/%E6%AD%A6%E6%B1%89%E5%B8%82%E4%B8%AD%E5%B1%B1%E8%88%B0%E5%8D%9A%E7%89%A9%E9%A6%86/49861362?fr=aladdin#4']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        }
    }

    def parse(self, response, **kwargs):
        li_list = response.xpath("/html/body/div[3]/div[2]/div/div[1]/table")
        print(len(li_list))
        for li in li_list[2:4]:
            li_list1 = li.xpath("./tr")
            print(len(li_list))
            for li in li_list1:
                item = CollectionItem()
                item["museumID"] = 134
                item["museumName"] = "武汉市中山舰博物馆"
                item['collectionName'] = li.xpath("./td[2]/div/div/span").xpath('string(.)').extract_first().replace('\n','')
                item['collectionImageLink'] = 'https://baike.baidu.com'+str(li.xpath(
                "./td[2]/div/div/a/@href").extract_first())
                item['collectionIntroduction'] = StrFilter.filter(
                li.xpath("./td[1]/div").xpath('string(.)').extract_first())
                print(item)
                yield(item)
