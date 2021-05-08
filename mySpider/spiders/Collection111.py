#
from ..items import *
from ..str_filter import *

class Collection111(scrapy.Spider):
    name = "Collection111"
    allowed_domains = ['baike.baidu.com']
    start_urls = ['https://baike.baidu.com/item/%E6%B5%8E%E5%8D%97%E5%B8%82%E5%8D%9A%E7%89%A9%E9%A6%86/118264?fr=aladdin#3']

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
            item["museumID"] = 111
            item["museumName"] = "济南市博物馆"
            item['collectionName'] = li.xpath("./td[1]/div/b").xpath('string(.)').extract_first()
            item['collectionImageLink'] = 'https://baike.baidu.com' + str(li.xpath(
                "./td[3]/div/div/a/@href").extract_first())
            item['collectionIntroduction'] = StrFilter.filter(
                li.xpath("./td[2]").xpath('string(.)').extract_first())
            print(item)
            yield(item)
