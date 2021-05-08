#
from ..items import *
from ..str_filter import *

class Collection113(scrapy.Spider):
    name = "Collection113"
    allowed_domains = ['museum.sdu.edu.cn']
    start_urls = ['http://museum.sdu.edu.cn/gchclist.jsp?urltype=tree.TreeTempUrl&wbtreeid=1052']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        }
    }

    def parse(self, response, **kwargs):
        li_list = response.xpath("/html/body/div[3]/div[1]/div[4]/div/form/div[3]/div/div")
        print(len(li_list))
        for li in li_list[1:]:
            item = CollectionItem()
            item["museumID"] = 113
            item["museumName"] = "山东大学博物馆"
            item['collectionName'] = li.xpath("./div[3]/a").xpath('string(.)').extract_first()
            item['collectionImageLink'] = 'http://museum.sdu.edu.cn' + str(li.xpath(
                "./div[2]/a/img/@src").extract_first())
            item['collectionIntroduction'] = StrFilter.filter(
                li.xpath("./div[4]").xpath('string(.)').extract_first())
            print(item)
            yield(item)
