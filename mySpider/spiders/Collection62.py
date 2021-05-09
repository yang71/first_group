from ..items import *
from ..str_filter import *


class Collection62(scrapy.Spider):
    name = "Collection62"
    allowed_domains = ['njmuseumadmin.com']
    start_urls = ['http://www.njmuseumadmin.com/Antique/lists/p/1',
                  'http://www.njmuseumadmin.com/Antique/lists/p/2',
                  'http://www.njmuseumadmin.com/Antique/lists/p/3',
                  'http://www.njmuseumadmin.com/Antique/lists/p/4',
                  'http://www.njmuseumadmin.com/Antique/lists/p/5']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.DefaultMiddleware': 0,
        },
    }

    def parse(self, response, **kwargs):
            #/html/body/div/div[3]/div[2]/ul/li[1]
        li_list = response.xpath("/html/body/div/div[3]/div[2]/ul/li")
        # print(li_list)
        for li in li_list:
            item = CollectionItem()
            item["museumID"] = 62
            item["museumName"] = "南京市博物总馆"

            # 名字的xpath都一样
            #/html/body/div/div[3]/div[2]/ul/li[1]/a/span
            item['collectionName'] = li.xpath("./a/span/text()").extract_first()

            # 注意是否为全路径，一般后缀为@src有的是@oldsrc
            # http://www.njmuseumadmin.com/Public/Upload/default/2015/10/23/6abdf2e8808076f4c48f1c9ff102e4f0.jpg
            # /html/body/div/div[3]/div[2]/ul/li[1]/a/img
            item['collectionImageLink'] = "http://www.njmuseumadmin.com/" + li.xpath(
                "a/img/@src").extract_first()

            #注意是否是全路径
            #怎么判断是否是全路径
            #/html/body/div/div[3]/div[2]/ul/li[1]/a
            #http://www.njmuseumadmin.com/Antique/show/id/160
            url = "http://www.njmuseumadmin.com/"+str(li.xpath("./a/@href").extract_first())
            #print(url)

            yield scrapy.Request(
                url,
                callback=self.parseAnotherPage,
                meta={"item": item}
            )
    #翻页
    #/html/body/div[5]/div[3]/div[6]/p/br[4]
    def parseAnotherPage(self, response):
        r = re.compile(u"\\n|\\r|\\[.*?]|\\t")
        item = response.meta["item"]

        #一开始爬的时候总是爬不出来介绍，标签上移得以解决
        #/html/body/div/div[3]/div[2]/div/div[2]/div[3]/div/div[1]/p/text()
        item["collectionIntroduction"] = response.xpath(
            'normalize-space(/html/body/div/div[3]/div[2]/div/div[2]/div[3])').extract_first()

        item["collectionIntroduction"] = "".join(item["collectionIntroduction"].split())
        item["collectionIntroduction"] = re.sub(r, '', item["collectionIntroduction"])
        print(item)
        yield item
