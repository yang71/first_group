from ..items import *
from ..str_filter import *

class Collection73(scrapy.Spider):
    name = "Collection73"
    allowed_domains = ['nbmuseum.cn']
    start_urls = ['http://www.nbmuseum.cn/col/col701/index.html']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.DefaultMiddleware': 0,
        },
    }

    def parse(self, response, **kwargs):
            #/html/body/div[1]/div/div[1]
        li_list = response.xpath("/html/body/div[1]/div/div")
        for div in li_list:
            item = CollectionItem()
            item["museumID"] = 73
            item["museumName"] = "宁波博物院"
            item['collectionName'] = "越窑青瓷"
            item['collectionImageLink'] = None
            #/html/body/div[1]/div/div[1]
            #/html/body/div[1]/div/div[3]
            r = re.compile(u"\\n|\\r|\\[.*?]|\\t")
            item["collectionIntroduction"] = div.xpath(
                'normalize-space(.)').extract_first()

            item["collectionIntroduction"] = "".join(item["collectionIntroduction"].split())
            item["collectionIntroduction"] = re.sub(r, '', item["collectionIntroduction"])
            print(item)
            yield item
