#
from ..items import *
from ..str_filter import *

class Collection127(scrapy.Spider):
    name = "Collection127"
    allowed_domains = ['eywsqsfbwg.com']
    start_urls = ['http://www.eywsqsfbwg.com/index.php?m=content&c=index&a=lists&catid=15']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        }
    }

    def parse(self, response, **kwargs):
        li_list = response.xpath("/html/body/div[4]/div[2]/div[2]/ul/li")
        print(len(li_list))
        for li in li_list[1:]:
            item = CollectionItem()
            item["museumID"] = 127
            item["museumName"] = "鄂豫皖苏区首府革命博物馆"
            item['collectionName'] = li.xpath("./a/p").xpath('string(.)').extract_first()
            item['collectionImageLink'] = str(li.xpath(
                "./a/@href").extract_first())
            item['collectionIntroduction'] = StrFilter.filter(
                li.xpath("./a/p").xpath('string(.)').extract_first())
            print(item)
            yield(item)
