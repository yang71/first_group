from ..items import *
from ..str_filter import *

class Collection68(scrapy.Spider):
    name = "Collection68"
    allowed_domains = ['zj-museum.com.cn']
    start_urls = ['http://www.zj-museum.com.cn/zjbwg/zjbwg/zs/jpww/tcq/index.html',
                  'http://www.zj-museum.com.cn/zjbwg/zjbwg/zs/jpww/tcq/index_1.html',
                  'http://www.zj-museum.com.cn/zjbwg/zjbwg/zs/jpww/tcq/index_2.html']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.DefaultMiddleware': 0,
        },
    }

    def parse(self, response, **kwargs):
            #/html/body/div[3]/div[2]/div[2]/ul/li[1]
        li_list = response.xpath("/html/body/div[3]/div[2]/div[2]/ul/li")
        for li in li_list:
            item = CollectionItem()
            item["museumID"] = 68
            item["museumName"] = "镇江博物馆"

            # 名字的xpath都一样
            #/html/body/div[3]/div[2]/div[2]/ul/li[1]/div
            r = re.compile(u"\\n|\\r|\\[.*?]|\\t")
            item['collectionName'] = li.xpath("./div/text()").extract_first()
            item["collectionName"] = "".join(item["collectionName"].split())
            item["collectionName"] = re.sub(r, '', item["collectionName"])

            # 注意是否为全路径，一般后缀为@src有的是@oldsrc
            #/html/body/div[3]/div[2]/div[2]/ul/li[1]/a/img
            #http://www.zj-museum.com.cn/zjbwg/upload/image/2016/10/26/c77518090f884f399cb267729804242c_185x185.jpg
            item['collectionImageLink'] = "http://www.zj-museum.com.cn/" + li.xpath("./a/img/@src").extract_first()


            #注意是否是全路径
            #怎么判断是否是全路径
            #http://www.zj-museum.com.cn/zjbwg/zjbwg/zs/jpww/tcq/2016/10/26/0b609a9a57fc12f0015800134d0304df.html
            #/html/body/div[3]/div[2]/div[2]/ul/li[1]/a
            url = "http://www.zj-museum.com.cn/" + str(li.xpath("./a/@href").extract_first())

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
            'normalize-space(/html/body/div[3]/div[2]/div[4]/p[2])').extract_first()

        item["collectionIntroduction"] = "".join(item["collectionIntroduction"].split())
        item["collectionIntroduction"] = re.sub(r, '', item["collectionIntroduction"])
        print(item)
        yield item
