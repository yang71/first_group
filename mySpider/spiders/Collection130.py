#
from ..items import *
from ..str_filter import *

class Collection130(scrapy.Spider):
    name = "Collection130"
    allowed_domains = ['aybwg.org']
    start_urls = ['http://www.aybwg.org/photo/list.php?catid=40']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        }
    }

    def parse(self, response, **kwargs):
        li_list = response.xpath("/html/body/div/div[4]/div[2]/div/ul/li")
        print(len(li_list))
        for li in li_list[1:]:
            item = CollectionItem()
            item["museumID"] = 130
            item["museumName"] = "安阳博物馆"
            item['collectionName'] = li.xpath("./a/span").xpath('string(.)').extract_first()
            item['collectionImageLink'] = str(li.xpath(
                "./a/div/img/@src").extract_first())
            item['collectionIntroduction'] = StrFilter.filter(
                li.xpath("./a/span").xpath('string(.)').extract_first())
            print(item)
            yield(item)
