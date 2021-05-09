#
from ..items import *
from ..str_filter import *

class Collection141(scrapy.Spider):
    name = "Collection141"
    allowed_domains = ['shaoqiguli.com']
    start_urls = ['http://www.shaoqiguli.com/Collection/collect?filter=firstlevel']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        }
    }

    def parse(self, response, **kwargs):
        li_list = response.xpath("/html/body/div[1]/div[3]/div/div/div[1]/ul[2]/li")
        print(len(li_list))
        for li in li_list[0:]:
            item = CollectionItem()
            item["museumID"] = 141
            item["museumName"] = "刘少奇故居纪念馆"
            item['collectionName'] = li.xpath("./a/p").xpath('string(.)').extract_first()
            item['collectionImageLink'] = str(li.xpath(
                "./a/div/div/@style").extract_first().replace('background-image: url("','').replace('");',''))
            item['collectionIntroduction'] = StrFilter.filter(
                li.xpath("./a/p").xpath('string(.)').extract_first())
            print(item)
            yield(item)
