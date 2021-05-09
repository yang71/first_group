#
from ..items import *
from ..str_filter import *

class Collection147(scrapy.Spider):
    name = "Collection147"
    allowed_domains = ['baike.baidu.com']
    start_urls = ['https://baike.baidu.com/item/%E5%AD%99%E4%B8%AD%E5%B1%B1%E6%95%85%E5%B1%85%E7%BA%AA%E5%BF%B5%E9%A6%86/2033485?fr=aladdin#4']

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
            item["museumID"] = 147
            item["museumName"] = "孙中山故居纪念馆"
            item['collectionName'] = li.xpath("./td[2]/div/div/span").xpath('string(.)').extract_first().replace('\n','')
            item['collectionImageLink'] = 'https://baike.baidu.com'+str(li.xpath(
                "./td[2]/div/div/a/@href").extract_first())
            item['collectionIntroduction'] = StrFilter.filter(
                li.xpath("./td[1]").xpath('string(.)').extract_first())
            print(item)
            yield(item)
