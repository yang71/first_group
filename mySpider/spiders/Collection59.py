from ..items import *
from ..str_filter import *

class Collection59(scrapy.Spider):
    name = "Collection59"
    allowed_domains = ['szmuseum.com']
    start_urls = ['https://www.szmuseum.com/Collection/List/ltgb?page=1',
                  'https://www.szmuseum.com/Collection/List/ltgb?page=2',
                  'https://www.szmuseum.com/Collection/List/ltgb?page=3']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.DefaultMiddleware': 0,
        },
    }

    def parse(self, response, **kwargs):
            #/html/body/div[10]/div
        li_list = response.xpath("/html/body/div[10]/div")
        for div in li_list:
            item = CollectionItem()
            item["museumID"] = 59
            item["museumName"] = "苏州博物馆"

            # 名字的xpath都一样
            #/html/body/div[10]/div
            #/html/body/div[10]/div[1]/div/div/div/div[1]/div[2]/h2
            item['collectionName'] = div.xpath("./div/div/div/div[1]/div[2]/h2/text()").extract_first()


            # 注意是否为全路径，一般后缀为@src有的是@oldsrc
            #/html/body/div[10]/div[1]/div/div/div/div[1]/div[1]/img
            item['collectionImageLink'] = div.xpath("./div/div/div/div[1]/div[1]/img/@src").extract_first()

            r = re.compile(u"\\n|\\r|\\[.*?]|\\t")
            #/html/body/div[10]/div[1]/div/div/div/div[1]/div[2]/div[2]/div/p[1]
            item["collectionIntroduction"] = div.xpath(
                'normalize-space(./div/div/div/div[1]/div[2]/div[2]/div/p[1])').extract_first()
            item["collectionIntroduction"] = "".join(item["collectionIntroduction"].split())
            item["collectionIntroduction"] = re.sub(r, '', item["collectionIntroduction"])
            print(item)
            yield item
