#
from ..items import *
from ..str_filter import *

class Collection119(scrapy.Spider):
    name = "Collection119"
    allowed_domains = ['tzhhxsg.com']
    start_urls = ['http://www.tzhhxsg.com/index.php?c=content&a=list&catid=45']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        }
    }

    def parse(self, response, **kwargs):
        li_list = response.xpath("/html/body/div[4]/div[3]/div/div[2]/div[2]/div[2]/a")
        print(len(li_list))
        for li in li_list[1:]:
            item = CollectionItem()
            item["museumID"] = 119
            item["museumName"] = "滕州市汉画像石馆"
            item['collectionName'] = li.xpath("./p").xpath('string(.)').extract_first()
            item['collectionImageLink'] = 'http://www.tzhhxsg.com' + str(li.xpath(
                "./div/div/@style").extract_first().replace('background-image:url(','').replace(');',''))
            item['collectionIntroduction'] = StrFilter.filter(
                li.xpath("./p").xpath('string(.)').extract_first())
            print(item)
            yield(item)
