from ..items import *
from ..str_filter import *

class Collection82(scrapy.Spider):
    name = "Collection82"
    allowed_domains = ['ahm.cn']
    start_urls = ['https://www.ahm.cn/Collection/List/tcq#page=1',
                  'https://www.ahm.cn/Collection/List/qtq#page=1',
                  'https://www.ahm.cn/Collection/List/zgsh#page=1']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        }
    }

    def parse(self, response, **kwargs):
            #/html/body/div[3]/div/div[5]/ul/li[1]
        li_list = response.xpath("/html/body/div[3]/div/div[5]/ul/li")
        for li in li_list:
            item = CollectionItem()
            item["museumID"] = 82
            item["museumName"] = "安徽省博物馆"

            # 名字的xpath都一样
            #/html/body/div[3]/div/div[5]/ul/li[1]/a/div[2]/h3
            r = re.compile(u"\\n|\\r|\\[.*?]|\\t")
            item['collectionName'] = li.xpath("./a/div[2]/h3/text()").extract_first()
            item["collectionName"] = "".join(item["collectionName"].split())
            item["collectionName"] = re.sub(r, '', item["collectionName"])

            # 注意是否为全路径，一般后缀为@src有的是@oldsrc
            #/html/body/div[3]/div/div[5]/ul/li[1]/a/div[1]/img
            #http://www.portmuseum.cn/graphic/2020/09/15/103055.jpg
            item['collectionImageLink'] = li.xpath("./a/div[1]/img/@src").extract_first()


            #注意是否是全路径
            #怎么判断是否是全路径
            #https://www.ahm.cn/Collection/Details/tcq?nid=561
            #/html/body/div[3]/div/div[5]/ul/li[1]/a
            url = "https://www.ahm.cn/" + str(li.xpath("./a/@href").extract_first())

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
            'normalize-space(/html/body/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[3])').extract_first()

        item["collectionIntroduction"] = "".join(item["collectionIntroduction"].split())
        item["collectionIntroduction"] = re.sub(r, '', item["collectionIntroduction"])
        print(item)
        yield item
