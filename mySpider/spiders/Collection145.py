#
from ..items import *
from ..str_filter import *

class Collection145(scrapy.Spider):
    name = "Collection145"
    allowed_domains = ['baike.baidu.com']
    start_urls = ['https://baike.baidu.com/item/%E5%B9%BF%E4%B8%9C%E7%9C%81%E5%8D%9A%E7%89%A9%E9%A6%86/1628626?fr=aladdin#4']

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
            item["museumID"] = 145
            item["museumName"] = "广东省博物馆"
            item['collectionName'] = li.xpath("./td[1]/div/b").xpath('string(.)').extract_first().replace('：','')
            item['collectionImageLink'] = 'https://baike.baidu.com'+str(li.xpath(
                "./td[2]/div/div/a/@href").extract_first())
            item['collectionIntroduction'] = StrFilter.filter(
                li.xpath("./td[1]/div/text()").extract_first())
            print(item)
            yield(item)
