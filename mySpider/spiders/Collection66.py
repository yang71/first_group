from ..items import *
from ..str_filter import *

class Collection66(scrapy.Spider):
    name = "Collection66"
    allowed_domains = ['xzmuseum.com']
    start_urls = ['https://www.xzmuseum.com/collection_list.aspx?category_id=498',
                  'https://www.xzmuseum.com/collection_list.aspx?category_id=499',
                  'https://www.xzmuseum.com/collection_list.aspx?category_id=500']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.DefaultMiddleware': 0,
        },
    }

    def parse(self, response, **kwargs):
        #/html/body/div[4]/div/div[2]/div[2]/div[2]/ul/li[1]
        li_list = response.xpath("/html/body/div[4]/div/div[2]/div[2]/div[2]/ul/li")
        for li in li_list:
            item = CollectionItem()
            item["museumID"] = 66
            item["museumName"] = "徐州博物馆"

            # 名字的xpath都一样
            #/html/body/div[4]/div/div[2]/div[2]/div[2]/ul/li[1]/a/p
            r = re.compile(u"\\n|\\r|\\[.*?]|\\t")
            item['collectionName'] = li.xpath("./a/p/text()").extract_first()
            item["collectionName"] = "".join(item["collectionName"].split())
            item["collectionName"] = re.sub(r, '', item["collectionName"])

            # 注意是否为全路径，一般后缀为@src有的是@oldsrc
            #/html/body/div[4]/div/div[2]/div[2]/div[2]/ul/li[1]/a/img
            #https://www.xzmuseum.com/upload/photos/09510.jpg
            item['collectionImageLink'] = "https://www.xzmuseum.com/" + li.xpath("./a/img/@src").extract_first()


            #注意是否是全路径
            #怎么判断是否是全路径
            #http://www.wxmuseum.com/Collection/BookDetails/ed39c2e5-d3ad-4e45-92a1-cb95f4f4d9db
            #/html/body/div[4]/div/div[2]/div[2]/div[2]/ul/li[1]/a
            url = "https://www.xzmuseum.com/" + str(li.xpath("./a/@href").extract_first())

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
            'normalize-space(/html/body/div[4]/div/div[2]/div[2]/div[2]/div[3]/p[2])').extract_first()

        item["collectionIntroduction"] = "".join(item["collectionIntroduction"].split())
        item["collectionIntroduction"] = re.sub(r, '', item["collectionIntroduction"])
        print(item)
        yield item
