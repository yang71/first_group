from ..items import *
from ..str_filter import *


class Collection60(scrapy.Spider):
    name = "Collection60"
    allowed_domains = ['yzmuseum.com']
    start_urls = ['https://www.yzmuseum.com/website/treasure/list.php?type=1',
                  'https://www.yzmuseum.com/website/treasure/list.php?type=2',
                  'https://www.yzmuseum.com/website/treasure/list.php?type=3',
                  'https://www.yzmuseum.com/website/treasure/list.php?type=4',
                  'https://www.yzmuseum.com/website/treasure/list.php?type=5']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        }
    }

    def parse(self, response, **kwargs):
            #/html/body/div[1]/div[2]/div[2]/div[3]/div[3]/div[1]
        li_list = response.xpath("/html/body/div[1]/div[2]/div[2]/div[3]/div[3]/div")
        #print(li_list)
        for div in li_list:
            item = CollectionItem()
            item["museumID"] = 60
            item["museumName"] = "扬州博物馆"

            # 名字的xpath都一样
            #/html/body/div[1]/div[2]/div[2]/div[3]/div[3]/div[1]/a/span/div/p[1]
            item['collectionName'] = div.xpath("./a/span/div/p[1]/text()").extract_first()


            #注意是否是全路径
            #怎么判断是否是全路径
            #/html/body/div[1]/div[2]/div[2]/div[3]/div[3]/div[1]/a
            #https://www.yzmuseum.com/website/treasure/detail.php?id=753
            url = "https://www.yzmuseum.com/"+str(div.xpath("./a/@href").extract_first())

            yield scrapy.Request(
                url,
                callback=self.parseAnotherPage,
                meta={"item": item}
            )
    #翻页
    #/html/body/div[5]/div[3]/div[6]/p/br[4]
    def parseAnotherPage(self, response):
        item = response.meta["item"]

        # 注意是否为全路径，一般后缀为@src有的是@oldsrc
        # https://www.yzmuseum.com/tess/upload/images/15/150/1503286039_MRm.jpg
        # /html/body/div[1]/div[2]/div[2]/div[3]/div[3]/img
        item['collectionImageLink'] = "https://www.yzmuseum.com/" + response.xpath("/html/body/div[1]/div[2]/div[2]/div[3]/div[3]/img/@src").extract_first()

        r = re.compile(u"\\n|\\r|\\[.*?]|\\t")

        #/html/body/div[1]/div[2]/div[2]/div[3]/div[3]/div[4]
        item["collectionIntroduction"] = response.xpath(
            'normalize-space(/html/body/div[1]/div[2]/div[2]/div[3]/div[3]/div[4])').extract_first()
        item["collectionIntroduction"] = "".join(item["collectionIntroduction"].split())
        item["collectionIntroduction"] = re.sub(r, '', item["collectionIntroduction"])
        print(item)
        yield item
