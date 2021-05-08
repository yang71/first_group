from ..items import *
from ..str_filter import *


class Collection63(scrapy.Spider):
    name = "Collection63"
    allowed_domains = ['njiemuseum.com']
    start_urls = ['http://www.njiemuseum.com/index.php/Index/Index/col/c_id/45/page/1.html',
                  'http://www.njiemuseum.com/index.php/Index/Index/col/c_id/45/page/2.html',
                  'http://www.njiemuseum.com/index.php/Index/Index/col/c_id/45/page/3.html']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.DefaultMiddleware': 0,
        },
    }

    def parse(self, response, **kwargs):
            #/html/body/div[2]/div/div[2]/div[2]/div/div[2]/div/ul/li[1]
        li_list = response.xpath("/html/body/div[2]/div/div[2]/div[2]/div/div[2]/div/ul/li")
        #print(li_list)
        for li in li_list:
            item = CollectionItem()
            item["museumID"] = 63
            item["museumName"] = "中国科举博物馆"

            #/html/body/div[2]/div/div[2]/div[2]/div/div[2]/div/ul/li[1]/div[2]/a
            # 名字的xpath都一样
            item['collectionName'] = li.xpath("./div[2]/a/text()").extract_first()

            # 注意是否为全路径，一般后缀为@src有的是@oldsrc
            # http://www.njiemuseum.com/uploadfiles/dd773bcecc1041cca5150d8d41f575ce.JPG
            # /html/body/div[2]/div/div[2]/div[2]/div/div[2]/div/ul/li[1]/div[1]/a[1]/img
            item['collectionImageLink'] = "http://www.njiemuseum.com/" + li.xpath("./div[1]/a[1]/img/@src").extract_first()
            #print(item['collectionImageLink'])

            #注意是否是全路径
            #怎么判断是否是全路径
            #/html/body/div[2]/div/div[2]/div[2]/div/div[2]/div/ul/li[1]/div[1]/a[1]
            #http://www.njiemuseum.com/index.php/Index/Index/art/a_id/480.html
            url = "http://www.njiemuseum.com"+str(li.xpath("./div[1]/a[1]/@href").extract_first())
            #print(url)

            yield scrapy.Request(
                url,
                callback=self.parseAnotherPage,
                meta={"item": item}
            )

    #翻页
    def parseAnotherPage(self, response):
        r = re.compile(u"\\n|\\r|\\[.*?]|\\t")
        item = response.meta["item"]

        #/html/body/div[2]/div/div[2]/div[2]/div/div[3]
        item["collectionIntroduction"] = response.xpath(
            'normalize-space(/html/body/div[2]/div/div[2]/div[2]/div/div[3])').extract_first()

        item["collectionIntroduction"] = "".join(item["collectionIntroduction"].split())
        item["collectionIntroduction"] = re.sub(r, '', item["collectionIntroduction"])
        print(item)
        yield item
