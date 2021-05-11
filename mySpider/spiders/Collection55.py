from ..items import *
from ..str_filter import *


class Collection55(scrapy.Spider):
    name = "Collection55"
    allowed_domains = ['slmmm.com']
    start_urls = ['https://www.slmmm.com/collection/8/1.html',
                  'https://www.slmmm.com/collection/8/2.html',
                  'https://www.slmmm.com/collection/8/3.html',
                  'https://www.slmmm.com/collection/8/4.html',
                  'https://www.slmmm.com/collection/8/5.html']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.DefaultMiddleware': 0,
        },
    }

    def parse(self, response, **kwargs):
        #/html/body/div[2]/section/div/div[2]/div/div[2]/div[1]
        li_list = response.xpath("/html/body/div[2]/section/div/div[2]/div[1]/div/div")
        #print(li_list)
        for div in li_list:
            item = CollectionItem()
            item["museumID"] = 55
            item["museumName"] = "上海市龙华烈士纪念馆"

            # 名字的xpath都一样
            #/html/body/div[2]/section/div/div[2]/div/div[2]/div[1]
            #/html/body/div[2]/section/div/div[2]/div[1]/div/div[1]/div/div[2]/h3
            item['collectionName'] = div.xpath("./div/div[2]/h3/text()").extract_first()

            # 注意是否为全路径，一般后缀为@src有的是@oldsrc
            #https://www.slmmm.com/data/cultural/M0000000059000037VKOF.jpg
            #/html/body/div[2]/section/div/div[2]/div/div[2]/div[1]
            #/html/body/div[2]/section/div/div[2]/div[1]/div/div[1]/div/div[1]/a/img
            item['collectionImageLink'] = div.xpath("./div/div[1]/a/img/@src").extract_first()

            #注意是否是全路径
            #怎么判断是否是全路径
            #/html/body/div[2]/section/div/div[2]/div[1]/div/div[1]/div/div[1]/a
            #https://www.shmmc.com.cn/Home/ww_detail?id=a8c8006cf702e55c
            url = "https://www.slmmm.com/"+str(div.xpath("./div/div[1]/a/@href").extract_first())

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
        #/html/body/div[2]/section/div/div/div[2]
        item["collectionIntroduction"] = response.xpath(
            'normalize-space(/html/body/div[2]/section/div/div/div[2]/p[6])').extract_first()
        item["collectionIntroduction"] = "".join(item["collectionIntroduction"].split())
        item["collectionIntroduction"] = re.sub(r, '', item["collectionIntroduction"])
        print(item)
        yield item
