#
from ..items import *
from ..str_filter import *

class Collection142(scrapy.Spider):
    name = "Collection142"
    allowed_domains = ['baike.baidu.com']
    start_urls = ['https://baike.baidu.com/item/%E9%95%BF%E6%B2%99%E7%AE%80%E7%89%8D%E5%8D%9A%E7%89%A9%E9%A6%86/5388818?fr=aladdin#3']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        }
    }

    def parse(self, response, **kwargs):
        li_list = response.xpath("/html/body/div[3]/div[2]/div/div[1]/table//tr")
        print(len(li_list))
        for li in li_list[0:]:
            item = CollectionItem()
            item["museumID"] = 142
            item["museumName"] = "长沙简牍博物馆"
            item['collectionName'] = li.xpath("./td[1]/div[1]/b").xpath('string(.)').extract_first()
            item['collectionImageLink'] = 'https://baike.baidu.com'+str(li.xpath(
                "./td[2]/div/div/a/@href").extract_first())
            item['collectionIntroduction'] = StrFilter.filter(
                li.xpath("./td[1]").xpath('string(.)').extract_first())
            print(item)
            yield(item)
