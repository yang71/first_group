from ..items import *
from ..str_filter import *

class Collection96(scrapy.Spider):
    name = "Collection96"
    allowed_domains = ['81-china.com']
    start_urls = ['http://www.81-china.com/collect/60.html']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.DefaultMiddleware': 0,
        },
    }


    def parse(self, response, **kwargs):
            #/html/body/div/div[5]/div[3]/div[2]/ul/li[1]
        li_list = response.xpath("/html/body/div/div[5]/div[3]/div[2]/ul/li")
        for li in li_list:
            item = CollectionItem()
            item["museumID"] = 96
            item["museumName"] = "南昌八一起义纪念馆"


            # 名字的xpath都一样
            #/html/body/div/div[5]/div[3]/div[2]/ul/li[1]/div[1]/a/img
            r = re.compile(u"\\n|\\r|\\[.*?]|\\t")
            item['collectionName'] = li.xpath("./div[1]/a/img/@alt").extract_first()
            item["collectionName"] = "".join(item["collectionName"].split())
            item["collectionName"] = re.sub(r, '', item["collectionName"])

            item['collectionImageLink'] = "http://www.81-china.com/" + li.xpath(
                "./div[1]/a/img/@src").extract_first()

            item["collectionIntroduction"] = item['collectionName']
            print(item)
            yield item

