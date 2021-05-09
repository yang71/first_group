#
from ..items import *
from ..str_filter import *

class Collection136(scrapy.Spider):
    name = "Collection136"
    allowed_domains = ['en.changjiangcp.com']
    start_urls = ['http://en.changjiangcp.com/list/17.html']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        }
    }

    def parse(self, response, **kwargs):
        li_list = response.xpath("/html/body/div[6]/div/div/div")
        print(len(li_list))
        for li in li_list:
            item = CollectionItem()
            item["museumID"] = 136
            item["museumName"] = "长江文明馆"
            item['collectionName'] = li.xpath("./a/div[2]/h2").xpath('string(.)').extract_first()
            item['collectionImageLink'] = 'http://www.whgmbwg.com'+str(li.xpath(
                "./a/img/@src").extract_first())
            item['collectionIntroduction'] = StrFilter.filter(
                li.xpath("./div[1]/a").xpath('string(.)').extract_first())
            print(item)
            yield(item)
