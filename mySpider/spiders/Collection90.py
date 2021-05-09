from ..items import *
from ..str_filter import *

class Collection90(scrapy.Spider):
    name = "Collection90"
    allowed_domains = ['qzhjg.cn']
    start_urls = ['http://www.qzhjg.cn/html/jddc/20180131/681.html#']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.DefaultMiddleware': 0,
        },
    }

    def parse(self, response, **kwargs):
            #/html/body/div[1]/div[2]/div[5]/div[3]/div[2]/div[2]/ul/li[1]
        li_list = response.xpath("/html/body/div[1]/div[2]/div[5]/div[3]/div[2]/div[2]/ul/li")
        for li in li_list:

            item = CollectionItem()
            item["museumID"] = 90
            item["museumName"] = "泉州海外交通史博物馆"

            # 名字的xpath都一样
            # /html/body/div[4]/div/div[2]/div[2]/ul/li[1]/a/span/p
            r = re.compile(u"\\n|\\r|\\[.*?]|\\t")
            item['collectionName'] = li.xpath("./a/img/@text").extract_first()
            item["collectionName"] = "".join(item["collectionName"].split())
            item["collectionName"] = re.sub(r, '', item["collectionName"])

            # 注意是否为全路径，一般后缀为@src有的是@oldsrc
            #http://www.qzhjg.cn/u/cms/www/201802/01155547kxl6.jpgu/cms/www/201802/01155547kxl6.jpg
            #/html/body/div[1]/div[2]/div[5]/div[3]/div[2]/div[2]/ul/li[1]/a/img
            item['collectionImageLink'] = li.xpath("./a/img/@src").extract_first()
            str1 = item['collectionImageLink']
            item['collectionImageLink'] = "http://www.qzhjg.cn" + str1
            item["collectionIntroduction"] = item['collectionName']

            print(item)
            yield item
