#
from ..items import *
from ..str_filter import *

class Collection105(scrapy.Spider):
    name = "Collection105"
    allowed_domains = ['baike.baidu.com']
    start_urls = ['https://baike.baidu.com/item/%E4%B8%AD%E5%9B%BD%E7%94%B2%E5%8D%88%E6%88%98%E4%BA%89%E5%8D%9A%E7%89%A9%E9%A6%86/3575085?fr=aladdin#3']

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
            item["museumID"] = 105
            item["museumName"] = "中国甲午战争博物馆"
            item['collectionName'] = li.xpath("./td[1]").xpath('string(.)').extract_first()
            item['collectionImageLink'] = 'https://baike.baidu.com'+str(li.xpath(
                "./td[2]/div/div/a/@href").extract_first())
            item['collectionIntroduction'] = StrFilter.filter(
                li.xpath("./td[1]").xpath('string(.)').extract_first())
            print(item)
            yield(item)


