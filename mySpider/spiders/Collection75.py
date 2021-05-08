from ..items import *
from ..str_filter import *

class Collection75(scrapy.Spider):
    name = "Collection75"
    allowed_domains = ['westlakemuseum.com']
    start_urls = ['http://www.westlakemuseum.com/index.php/gcjp/jpzs2']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.DefaultMiddleware': 0,
        },
    }

    def parse(self, response, **kwargs):
            #/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div/form/table//tr[1]
        li_list = response.xpath("/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div/form/table//tr")
        for tr in li_list:
            item = CollectionItem()
            item["museumID"] = 75
            item["museumName"] = "杭州西湖博物馆总馆"

            # 名字的xpath都一样
            #/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div/form/table//tr[1]/td/a
            r = re.compile(u"\\n|\\r|\\[.*?]|\\t")
            item['collectionName'] = tr.xpath("./td/a/text()").extract_first()
            item["collectionName"] = "".join(item["collectionName"].split())
            item["collectionName"] = re.sub(r, '', item["collectionName"])

            #注意是否是全路径
            #怎么判断是否是全路径
            #/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div/form/table//tr[1]/td/a
            #http://www.westlakemuseum.com/index.php/gcjp/jpzs2/847-gcjp-001.html
            url = "http://www.westlakemuseum.com" + str(tr.xpath("./td/a/@href").extract_first())

            yield scrapy.Request(
                url,
                callback=self.parseAnotherPage,
                meta={"item": item}
            )
    # 翻页
    def parseAnotherPage(self, response):
        r = re.compile(u"\\n|\\r|\\[.*?]|\\t")
        item = response.meta["item"]

        # 注意是否为全路径，一般后缀为@src有的是@oldsrc
        # /html/body/div[1]/div/div[2]/div[2]/div/div[3]/table/tbody/tr/td[2]/img
        # http://www.westlakemuseum.com/images/images2020/gcjp01.jpg
        item['collectionImageLink'] = "http://www.westlakemuseum.com" + response.xpath(
            "/html/body/div[1]/div/div[2]/div[2]/div/div[3]/table//tr/td[2]/img/@src").extract_first()

        item["collectionIntroduction"] = response.xpath(
            'normalize-space(/html/body/div[1]/div/div[2]/div[2]/div/div[3]/p[2])').extract_first()

        item["collectionIntroduction"] = "".join(item["collectionIntroduction"].split())
        item["collectionIntroduction"] = re.sub(r, '', item["collectionIntroduction"])
        print(item)
        yield item
