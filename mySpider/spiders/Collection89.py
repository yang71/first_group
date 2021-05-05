from ..items import *
from ..str_filter import *

class Collection89(scrapy.Spider):
    name = "Collection89"
    allowed_domains = ['gthyjng.com']
    start_urls = ['http://www.gthyjng.com/gcww/wwjs/jfzzsq/']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        }
    }

    def parse(self, response, **kwargs):
            #/html/body/div[4]/div/div[2]/div[2]/ul/li[1]
        li_list = response.xpath("/html/body/div[4]/div/div[2]/div[2]/ul/li")
        for li in li_list:
            item = CollectionItem()
            item["museumID"] = 89
            item["museumName"] = "古田会议纪念馆"

            # 注意是否为全路径，一般后缀为@src有的是@oldsrc
            #http://www.gthyjng.com/gcww/wwjs/jfzzsq/202006/W020200618312957120750.jpg
            #/html/body/div[4]/div/div[2]/div[2]/ul/li[1]/a/div/img
            item['collectionImageLink'] = li.xpath("./a/div/img/@src").extract_first()
            str1 = item['collectionImageLink']
            item['collectionImageLink'] = "http://www.gthyjng.com/gcww/wwjs/jfzzsq/" + str1[1:]

            #注意是否是全路径
            #怎么判断是否是全路径
            #http://www.gthyjng.com/gcww/wwjs/jfzzsq/202006/t20200618_550887.htm
            #/html/body/div[4]/div/div[2]/div[2]/ul/li[1]/a
            str2 = str(li.xpath("./a/@href").extract_first())
            url = "http://www.gthyjng.com/gcww/wwjs/jfzzsq/" + str2[1:]

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
        # /html/body/div[4]/div/div[2]/div[2]/ul/li[1]/a/span/p
        r = re.compile(u"\\n|\\r|\\[.*?]|\\t")
        item['collectionName'] = response.xpath("/html/body/div[4]/div/div[2]/div[1]/h1/text()").extract_first()
        item["collectionName"] = "".join(item["collectionName"].split())
        item["collectionName"] = re.sub(r, '', item["collectionName"])

        item["collectionIntroduction"] = response.xpath(
            'normalize-space(/html/body/div[4]/div/div[2]/div[3]/div/div[2]/div/div/div/ol/li[1])').extract_first()

        item["collectionIntroduction"] = "".join(item["collectionIntroduction"].split())
        item["collectionIntroduction"] = re.sub(r, '', item["collectionIntroduction"])

        print(item)
        yield item
