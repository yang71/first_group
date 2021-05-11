#
from ..items import *
from ..str_filter import *

class Collection133(scrapy.Spider):
    name = "Collection133"
    allowed_domains = ['baike.baidu.com']
    start_urls = ['https://baike.baidu.com/item/%E8%BE%9B%E4%BA%A5%E9%9D%A9%E5%91%BD%E6%AD%A6%E6%98%8C%E8%B5%B7%E4%B9%89%E7%BA%AA%E5%BF%B5%E9%A6%86/1797961?fr=aladdin#4']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        }
    }

    def parse(self, response, **kwargs):
        li_list = response.xpath("/html/body/div[3]/div[2]/div/div[1]/table//tr")
        print(len(li_list))
        for li in li_list[1:]:
            item = CollectionItem()
            item["museumID"] = 133
            item["museumName"] = "辛亥革命武昌起义纪念馆"
            item['collectionName'] = li.xpath("./td[1]/div/b").xpath('string(.)').extract_first()
            item['collectionImageLink'] = 'https://baike.baidu.com'+str(li.xpath(
                "./td[2]/div/div/a/@href").extract_first())
            item['collectionIntroduction'] = StrFilter.filter(
                li.xpath("./td[1]/div").xpath('string(.)').extract_first())
            print(item)
            yield(item)
