#
from ..items import *
from ..str_filter import *

class Collection116(scrapy.Spider):
    name = "Collection116"
    allowed_domains = ['zbstcbwg.cn']
    start_urls = ['http://www.zbstcbwg.cn/collections.html']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        }
    }

    def parse(self, response, **kwargs):
        li_list = response.xpath("//*[@id='datalist']/ul/li")
        print(len(li_list))
        for li in li_list[3:]:
            item = CollectionItem()
            item["museumID"] = 116
            item["museumName"] = "淄博市陶瓷博物馆"
            item['collectionName'] = li.xpath("./a/div[2]").xpath('string(.)').extract_first()
            item['collectionImageLink'] = 'http://www.zbstcbwg.cn' + str(li.xpath(
                "./a/div[1]/img/@src").extract_first())
            item['collectionIntroduction'] = StrFilter.filter(
                li.xpath("./a/div[1]/div[2]").xpath('string(.)').extract_first())
            print(item)
            yield(item)
