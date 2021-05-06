from ..items import *
from ..str_filter import *

class Collection74(scrapy.Spider):
    name = "Collection74"
    allowed_domains = ['wzmuseum.cn']
    start_urls = ['http://www.wzmuseum.cn/Col/Col5/Index_1.aspx',
                  'http://www.wzmuseum.cn/Col/Col5/Index_2.aspx',
                  'http://www.wzmuseum.cn/Col/Col5/Index_3.aspx',
                  'http://www.wzmuseum.cn/Col/Col5/Index_4.aspx',
                  'http://www.wzmuseum.cn/Col/Col5/Index_5.aspx',
                  'http://www.wzmuseum.cn/Col/Col5/Index_6.aspx']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        }
    }

    def parse(self, response, **kwargs):
            #/html/body/div[1]/div[4]/div[2]/div[2]/ul/li[1]
        li_list = response.xpath("/html/body/div[1]/div[4]/div[2]/div[2]/ul/li")
        for li in li_list:
            item = CollectionItem()
            item["museumID"] = 74
            item["museumName"] = "温州博物馆"

            # 名字的xpath都一样
            #/html/body/div[1]/div[4]/div[2]/div[2]/ul/li[1]/a/span
            r = re.compile(u"\\n|\\r|\\[.*?]|\\t")
            item['collectionName'] = li.xpath("./a/span/text()").extract_first()
            item["collectionName"] = "".join(item["collectionName"].split())
            item["collectionName"] = re.sub(r, '', item["collectionName"])

            # 注意是否为全路径，一般后缀为@src有的是@oldsrc
            #/html/body/div[1]/div[4]/div[2]/div[2]/ul/li[1]/a/img
            #http://www.wzmuseum.cn/UploadFile/2014/10/13/20141013191836725.jpg
            item['collectionImageLink'] = "http://www.wzmuseum.cn" + li.xpath("./a/img/@src").extract_first()


            #注意是否是全路径
            #怎么判断是否是全路径
            #/html/body/div[1]/div[4]/div[2]/div[2]/ul/li[1]/a
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
        #/html/body/div/div[4]/div[2]/div[2]/div[2]
        item["collectionIntroduction"] = response.xpath(
            'normalize-space(/html/body/div/div[4]/div[2]/div[2]/div[2])').extract_first()

        item["collectionIntroduction"] = "".join(item["collectionIntroduction"].split())
        item["collectionIntroduction"] = re.sub(r, '', item["collectionIntroduction"])
        print(item)
        yield item
