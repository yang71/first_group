from ..items import *
from ..str_filter import *

class Collection58(scrapy.Spider):
    name = "Collection58"
    allowed_domains = ['ntmuseum.com']
    start_urls = ['http://www.ntmuseum.com/colunm2/col1/list_17_1.html',
                  'http://www.ntmuseum.com/colunm2/col1/list_17_2.html',
                  'http://www.ntmuseum.com/colunm2/col1/list_17_3.html',
                  'http://www.ntmuseum.com/colunm2/col1/list_17_4.html',
                  'http://www.ntmuseum.com/colunm2/col1/list_17_5.html']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        }
    }

    def parse(self, response, **kwargs):
        #/html/body/section[2]/div[3]/div[1]/ul/li[1]
        li_list = response.xpath("/html/body/section[2]/div[3]/div[1]/ul/li")
        for li in li_list:
            item = CollectionItem()
            item["museumID"] = 58
            item["museumName"] = "南通博物苑"

            # 名字的xpath都一样
            #/html/body/section[2]/div[3]/div[1]/ul/li
            #/html/body/section[2]/div[3]/div[1]/ul/li[1]/a/span
            item['collectionName'] = li.xpath("./a/span/text()").extract_first()


            # 注意是否为全路径，一般后缀为@src有的是@oldsrc
            #/html/body/section[2]/div[3]/div[1]/ul/li[1]/a/img
            item['collectionImageLink'] = li.xpath("./a/img/@src").extract_first()

            #注意是否是全路径
            #怎么判断是否是全路径
            #/html/body/section[2]/div[3]/div[1]/ul/li[1]/a
            url = str(li.xpath("./a/@href").extract_first())

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
            'normalize-space(/html/body/section[2]/div[3]/div/div/ul/li[3]/div[2])').extract_first()
        item["collectionIntroduction"] = "".join(item["collectionIntroduction"].split())
        item["collectionIntroduction"] = re.sub(r, '', item["collectionIntroduction"])
        print(item)
        yield item
