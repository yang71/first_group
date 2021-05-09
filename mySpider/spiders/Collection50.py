from ..items import *
from ..str_filter import *


class Collection50(scrapy.Spider):
    name = "Collection50"
    allowed_domains = ['luxunmuseum.cn']
    start_urls = ['http://www.luxunmuseum.cn/cp/index/cid/2.html',
                  'http://www.luxunmuseum.cn/cp/index/cid/3.html',
                  'http://www.luxunmuseum.cn/cp/index/cid/4.html']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.DefaultMiddleware': 0,
        },
    }

    def parse(self, response, **kwargs):
        li_list = response.xpath("/html/body/div[3]/div[1]/div[1]/ul/li")
        for li in li_list:
            item = CollectionItem()
            item["museumID"] = 50
            item["museumName"] = "上海鲁迅纪念馆"
            # 名字的xpath都一样
            item['collectionName'] = li.xpath("./div/a/h3/text()").extract_first()

            # 注意是否为全路径，一般后缀为@src有的是@oldsrc
            item['collectionImageLink'] = li.xpath(
                "./div/a/img/@src").extract_first()

            #注意是否是全路径
            #怎么判断是否是全路径
            url = "http://www.luxunmuseum.cn/"+str(li.xpath("./div/a/@href").extract_first())

            yield scrapy.Request(
                url,
                callback=self.parseAnotherPage,
                meta={"item": item}
            )
    #翻页
    def parseAnotherPage(self, response):
        item = response.meta["item"]
        item['collectionIntroduction'] = ''.join(re.sub(StrFilter.r1, "", str(
            response.xpath("/html/body/div[3]/div[1]/div[2]/div").xpath('string(.)').extract_first())).split())

        print(item)
        yield item
