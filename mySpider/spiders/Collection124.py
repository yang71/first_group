#
from ..items import *
from ..str_filter import *

class Collection124(scrapy.Spider):
    name = "Collection124"
    allowed_domains = ['baike.baidu.com']
    start_urls = ['https://baike.baidu.com/item/%E6%B4%9B%E9%98%B3%E5%8D%9A%E7%89%A9%E9%A6%86/1628817?fr=aladdin#5']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        }
    }

    def parse(self, response, **kwargs):
        li_list = response.xpath("/html/body/div[3]/div[2]/div/div[1]/table")
        print(len(li_list))
        for li in li_list[3:]:
            item = CollectionItem()
            item["museumID"] = 124
            item["museumName"] = "洛阳博物馆"
            item['collectionName'] = li.xpath(".//tr[1]/td[2]").xpath('string(.)').extract_first()
            item['collectionImageLink'] = 'https://baike.baidu.com'+str(li.xpath(
                ".//tr[4]/td/div[3]/div/a/@href").extract_first())
            item['collectionIntroduction'] = StrFilter.filter(
                li.xpath(".//tr[4]/td/div[2]").xpath('string(.)').extract_first())
            print(item)
            yield(item)
