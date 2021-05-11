#
from ..items import *
from ..str_filter import *

class Collection120(scrapy.Spider):
    name = "Collection120"
    allowed_domains = ['jiningmuseum.com']
    start_urls = ['http://www.jiningmuseum.com/list/article_list.do?channelId=210']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        }
    }

    def parse(self, response, **kwargs):
        li_list = response.xpath("/html/body/div[3]/div[2]/div[2]/ul/li")
        print(len(li_list))
        for li in li_list[1:]:
            item = CollectionItem()
            item["museumID"] = 120
            item["museumName"] = "济宁市博物馆"
            item['collectionName'] = li.xpath("./a/div[2]/h4").xpath('string(.)').extract_first().replace('\xa0','').replace(' ','')
            item['collectionImageLink'] = str(li.xpath(
                "./a/div[1]/img/@src").extract_first())
            item['collectionIntroduction'] = StrFilter.filter(
                li.xpath("./a/div[2]/p[1]").xpath('string(.)').extract_first())
            print(item)
            yield(item)
