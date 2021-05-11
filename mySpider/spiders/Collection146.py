#
from ..items import *
from ..str_filter import *

class Collection146(scrapy.Spider):
    name = "Collection146"
    allowed_domains = ['baike.baidu.com']
    start_urls = ['https://baike.baidu.com/item/%E8%A5%BF%E6%B1%89%E5%8D%97%E8%B6%8A%E7%8E%8B%E5%8D%9A%E7%89%A9%E9%A6%86/1786642?fr=aladdin#4']

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
            item["museumID"] = 146
            item["museumName"] = "西汉南越王博物馆"
            item['collectionName'] = li.xpath("./td[1]/div/a").xpath('string(.)').extract_first()
                #.replace('：','')
            item['collectionImageLink'] = 'https://baike.baidu.com'+str(li.xpath(
                "./td[3]/div/div/a/@href").extract_first())
            item['collectionIntroduction'] = StrFilter.filter(
                li.xpath("./td[2]/div/text()").extract_first())
            print(item)
            yield(item)
