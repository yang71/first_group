from ..items import *
from ..str_filter import *

class Collection79(scrapy.Spider):
    name = "Collection79"
    allowed_domains = ['portmuseum.cn']
    start_urls = ['http://www.portmuseum.cn/cp_list.php?catg=1&types=1',
                  'http://www.portmuseum.cn/cp_list.php?catg=1&types=2',
                  'http://www.portmuseum.cn/cp_list.php?catg=1&types=3',
                  'http://www.portmuseum.cn/cp_list.php?catg=1&types=4',
                  'http://www.portmuseum.cn/cp_list.php?catg=1&types=5']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        }
    }

    def parse(self, response, **kwargs):
            #/html/body/div[3]/div[2]/ul/li[1]
        li_list = response.xpath("/html/body/div[3]/div[2]/ul/li")
        for li in li_list:
            item = CollectionItem()
            item["museumID"] = 79
            item["museumName"] = "宁波中国港口博物馆"

            # 名字的xpath都一样
            #/html/body/div[3]/div[2]/ul/li[1]/a/div/h3
            r = re.compile(u"\\n|\\r|\\[.*?]|\\t")
            item['collectionName'] = li.xpath("./a/div/h3/text()").extract_first()
            item["collectionName"] = "".join(item["collectionName"].split())
            item["collectionName"] = re.sub(r, '', item["collectionName"])

            # 注意是否为全路径，一般后缀为@src有的是@oldsrc
            #/html/body/div[3]/div[2]/ul/li[1]/a/img
            #http://www.portmuseum.cn/graphic/2020/09/15/103055.jpg
            item['collectionImageLink'] = "http://www.portmuseum.cn/" + li.xpath("./a/img/@src").extract_first()


            #注意是否是全路径
            #怎么判断是否是全路径
            #http://www.portmuseum.cn/cp_read.php?id=47
            #/html/body/div[3]/div[2]/ul/li[1]/a
            url = "http://www.portmuseum.cn/" + str(li.xpath("./a/@href").extract_first())

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
            'normalize-space(/html/body/div[3]/div[3])').extract_first()

        item["collectionIntroduction"] = "".join(item["collectionIntroduction"].split())
        item["collectionIntroduction"] = re.sub(r, '', item["collectionIntroduction"])
        print(item)
        yield item
