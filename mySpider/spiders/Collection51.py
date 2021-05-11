from ..items import *
from ..str_filter import *


class Collection51(scrapy.Spider):
    name = "Collection51"
    allowed_domains = ['zgyd1921.com']
    start_urls = ['http://www.zgyd1921.com/zgyd/node3/n17/n18/index.html',
                  'http://www.zgyd1921.com/zgyd/node3/n17/n18/index1.html',
                  'http://www.zgyd1921.com/zgyd/node3/n17/n18/index2.html',
                  'http://www.zgyd1921.com/zgyd/node3/n17/n18/index3.html']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.DefaultMiddleware': 0,
        },
    }

    def parse(self, response, **kwargs):
        #/html/body/div[5]/ul
        li_list = response.xpath("/html/body/div[5]/ul/li")
        for li in li_list:
            item = CollectionItem()
            item["museumID"] = 51
            item["museumName"] = "中国共产党第一次全国代表大会会址纪念馆"

            # 名字的xpath都一样
            #/html/body/div[5]/ul/li[1]/p/a
            item['collectionName'] = li.xpath("./p/a/text()").extract_first()

            # 注意是否为全路径，一般后缀为@src有的是@oldsrc
            #http://www.zgyd1921.com/images/thumbnailimg/month_1710/201710150250058209.jpg
            #/html/body/div[5]/ul/li[1]/a/img

            item['collectionImageLink'] = "http://www.zgyd1921.com/"+li.xpath(
                "./a/img/@src").extract_first()

            #注意是否是全路径
            #怎么判断是否是全路径
            #http://www.zgyd1921.com/zgyd/node3/n17/n18/ulai176.html
            #/html/body/div[5]/ul/li[1]/a
            url = "http://www.zgyd1921.com/"+str(li.xpath("./a/@href").extract_first())

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
        item["collectionIntroduction"] = response.xpath(
            'normalize-space(/html/body/div[5]/div[3]/div[6]/p)').extract_first()
        item["collectionIntroduction"] = "".join(item["collectionIntroduction"].split())
        item["collectionIntroduction"] = re.sub(r, '', item["collectionIntroduction"])
        print(item)
        yield item
