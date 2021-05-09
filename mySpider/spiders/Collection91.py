from ..items import *
from ..str_filter import *

class Collection91(scrapy.Spider):
    name = "Collection91"
    allowed_domains = ['mtybwg.org.cn']
    start_urls = ['http://www.mtybwg.org.cn/cangpin/164-1.aspx',
                  'http://www.mtybwg.org.cn/cangpin/164-2.aspx',
                  'http://www.mtybwg.org.cn/cangpin/164-3.aspx']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.DefaultMiddleware': 0,
        },
    }

    def parse(self, response, **kwargs):
            #/html/body/div[2]/div[2]/ul/li[1]
        li_list = response.xpath("/html/body/div[2]/div[2]/ul/li")
        for li in li_list:
            item = CollectionItem()
            item["museumID"] = 91
            item["museumName"] = "中国闽台缘博物馆"

            # 名字的xpath都一样
            #/html/body/div[2]/div[2]/ul/li[1]/a[2]
            r = re.compile(u"\\n|\\r|\\[.*?]|\\t")
            item['collectionName'] = li.xpath("./a[2]/text()").extract_first()
            item["collectionName"] = "".join(item["collectionName"].split())
            item["collectionName"] = re.sub(r, '', item["collectionName"])

            # 注意是否为全路径，一般后缀为@src有的是@oldsrc
            #/html/body/div[2]/div[2]/ul/li[1]/a[1]/img
            #http://www.mtybwg.org.cn/upload/201605/04/201605041517133593.JPG
            item['collectionImageLink'] = "http://www.mtybwg.org.cn/" + li.xpath("./a[1]/img/@src").extract_first()


            #注意是否是全路径
            #怎么判断是否是全路径
            #http://www.mtybwg.org.cn/cangpin/show/664.aspx
            #/html/body/div[2]/div[2]/ul/li[1]/a[1]
            url = "http://www.mtybwg.org.cn/" + str(li.xpath("./a[1]/@href").extract_first())

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
            'normalize-space(/html/body/div[2]/div[2]/ul)').extract_first()

        item["collectionIntroduction"] = "".join(item["collectionIntroduction"].split())
        item["collectionIntroduction"] = re.sub(r, '', item["collectionIntroduction"])
        item["collectionIntroduction"] = StrFilter.filter_2(item["collectionIntroduction"])
        print(item)
        yield item
