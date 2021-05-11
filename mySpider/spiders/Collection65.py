from ..items import *
from ..str_filter import *

class Collection65(scrapy.Spider):
    name = "Collection65"
    allowed_domains = ['wxmuseum.com']
    start_urls = ['http://www.wxmuseum.com/Collection/BookList/shbk?page=1',
                  'http://www.wxmuseum.com/Collection/BookList/shbk?page=2',
                  'http://www.wxmuseum.com/Collection/BookList/shbk?page=3']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.DefaultMiddleware': 0,
        },
    }

    def parse(self, response, **kwargs):
        #/html/body/div[5]/div/div/div/div[2]/ul[2]/li[1]
        li_list = response.xpath("/html/body/div[5]/div/div/div/div[2]/ul[2]/li")
        for li in li_list:
            item = CollectionItem()
            item["museumID"] = 65
            item["museumName"] = "无锡博物院"

            # 名字的xpath都一样
            #/html/body/div[5]/div/div/div/div[2]/ul[2]/li[1]/a/div/h3
            r = re.compile(u"\\n|\\r|\\[.*?]|\\t")
            item['collectionName'] = li.xpath("./a/div/h3/text()").extract_first()
            item["collectionName"] = "".join(item["collectionName"].split())
            item["collectionName"] = re.sub(r, '', item["collectionName"])

            # 注意是否为全路径，一般后缀为@src有的是@oldsrc
            #/html/body/div[5]/div/div/div/div[2]/ul[2]/li[1]/a/i/img
            item['collectionImageLink'] = li.xpath("./a/i/img/@src").extract_first()


            #注意是否是全路径
            #怎么判断是否是全路径
            #http://www.wxmuseum.com/Collection/BookDetails/ed39c2e5-d3ad-4e45-92a1-cb95f4f4d9db
            #/html/body/div[5]/div/div/div/div[2]/ul[2]/li[1]/a
            url = "http://www.wxmuseum.com/" + str(li.xpath("./a/@href").extract_first())

            yield scrapy.Request(
                url,
                callback=self.parseAnotherPage,
                meta={"item": item}
            )
    # 翻页
    def parseAnotherPage(self, response):
        r = re.compile(u"\\n|\\r|\\[.*?]|\\t")
        item = response.meta["item"]

        item["collectionIntroduction"] = response.xpath(
            'normalize-space(/html/body/div[5]/div/div/div/div[2]/div[2]/div[2])').extract_first()

        item["collectionIntroduction"] = "".join(item["collectionIntroduction"].split())
        item["collectionIntroduction"] = re.sub(r, '', item["collectionIntroduction"])
        print(item)
        yield item
