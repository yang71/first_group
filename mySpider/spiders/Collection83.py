from ..items import *
from ..str_filter import *

class Collection83(scrapy.Spider):
    name = "Collection83"
    allowed_domains = ['hzwhbwg.com']
    start_urls = ['http://www.hzwhbwg.com/index.php/list-3.html',
                  'http://www.hzwhbwg.com/index.php/list-3-2.html',
                  'http://www.hzwhbwg.com/index.php/list-3-3.html',
                  'http://www.hzwhbwg.com/index.php/list-3-4.html',
                  'http://www.hzwhbwg.com/index.php/list-3-5.html']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.DefaultMiddleware': 0,
        },
    }

    def parse(self, response, **kwargs):
            #/html/body/div[6]/div[2]/ul/li[1]
        li_list = response.xpath("/html/body/div[6]/div[2]/ul/li")
        for li in li_list:
            item = CollectionItem()
            item["museumID"] = 83
            item["museumName"] = "安徽中国徽州文化博物馆"


            item['collectionName'] = "中国徽州文化博物馆藏品"

            # 注意是否为全路径，一般后缀为@src有的是@oldsrc
            #/html/body/div[6]/div[2]/ul/li[1]/a/img
            #http://www.hzwhbwg.com/upfiles/image/15006200800.jpg
            item['collectionImageLink'] = "http://www.hzwhbwg.com/" + li.xpath("./a/img/@src").extract_first()



            item["collectionIntroduction"] = "中国徽州文化博物馆藏品"
            print(item)
            yield item
