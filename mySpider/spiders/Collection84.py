from ..items import *
from ..str_filter import *

class Collection84(scrapy.Spider):
    name = "Collection84"
    allowed_domains = ['ahgm.org.cn']
    start_urls = ['http://www.ahgm.org.cn/ahgm/ahgm/gcjp/kw/index.html',
                  'http://www.ahgm.org.cn/ahgm/ahgm/gcjp/ys/index.html',
                  'http://www.ahgm.org.cn/ahgm/ahgm/gcjp/gswhs/index.html']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.DefaultMiddleware': 0,
        },
    }

    def parse(self, response, **kwargs):
            #/html/body/div[6]/div/ul/li[1]
        li_list = response.xpath("/html/body/div[6]/div/ul/li")
        for li in li_list:
            item = CollectionItem()
            item["museumID"] = 84
            item["museumName"] = "安徽省地质博物馆"


            # 注意是否为全路径，一般后缀为@src有的是@oldsrc
            #/html/body/div[6]/div/ul/li[1]/a/img
            #http://www.ahgm.org.cn/ahgm/upload/image/2021/02/05/639d5d897d5b41c98b4d672bce876312_283x288.jpg
            item['collectionImageLink'] = "http://www.ahgm.org.cn/" + li.xpath("./a/img/@src").extract_first()


            #注意是否是全路径
            #怎么判断是否是全路径
            #http://www.ahgm.org.cn/ahgm/ahgm/gcjp/kw/2021/02/08/2c90e48e7730d27001777133f3ef13f7.html
            #/html/body/div[6]/div/ul/li[1]/a
            url = "http://www.ahgm.org.cn/" + str(li.xpath("./a/@href").extract_first())

            yield scrapy.Request(
                url,
                callback=self.parseAnotherPage,
                meta={"item": item}
            )
    # 翻页
    def parseAnotherPage(self, response):
        r = re.compile(u"\\n|\\r|\\[.*?]|\\t")
        item = response.meta["item"]

        # 名字的xpath都一样
        # /html/body/div[6]/div/ul/li[1]/div/span[1]
        r = re.compile(u"\\n|\\r|\\[.*?]|\\t")
        item['collectionName'] = response.xpath("/html/body/div[6]/div/div[2]/div[1]/text()").extract_first()
        item["collectionName"] = "".join(item["collectionName"].split())
        item["collectionName"] = re.sub(r, '', item["collectionName"])

        item["collectionIntroduction"] = response.xpath(
            'normalize-space(/html/body/div[6]/div/div[2]/div[2])').extract_first()

        item["collectionIntroduction"] = "".join(item["collectionIntroduction"].split())
        item["collectionIntroduction"] = re.sub(r, '', item["collectionIntroduction"])
        print(item)
        yield item
