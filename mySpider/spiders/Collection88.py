from ..items import *
from ..str_filter import *

class Collection88(scrapy.Spider):
    name = "Collection88"
    allowed_domains = ['fjbwy.com']
    start_urls = ['http://www.fjbwy.com/node_124.html#nav']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        }
    }

    def parse(self, response, **kwargs):

        li_list = response.xpath("//div[@class='zstuk']")
        for div in li_list:

            item = CollectionItem()
            item["museumID"] = 88
            item["museumName"] = "福建博物院"


            # 注意是否为全路径，一般后缀为@src有的是@oldsrc
            #/html/body/div[3]/div[5]/div[1]/a/img
            item['collectionImageLink'] = div.xpath("./div[1]/a/img/@src").extract_first()


            #注意是否是全路径
            #怎么判断是否是全路径
            #https://www.ahbbmuseum.com/?list_19/1180.html
            #/html/body/div[3]/div[5]/div[1]/a
            url = str(div.xpath("./div[1]/a/@href").extract_first())

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
        # /html/body/div[3]/div/div[2]/div[1]
        r = re.compile(u"\\n|\\r|\\[.*?]|\\t")
        item['collectionName'] = response.xpath("/html/body/div[3]/div/div[4]/div[1]/text()").extract_first()

        item["collectionIntroduction"] = response.xpath(
            'normalize-space(/html/body/div[3]/div/div[4]/div[3]/p[2])').extract_first()

        item["collectionIntroduction"] = "".join(item["collectionIntroduction"].split())
        item["collectionIntroduction"] = re.sub(r, '', item["collectionIntroduction"])

        print(item)
        yield item
