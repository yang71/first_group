from ..items import *
from ..str_filter import *


class Collection54(scrapy.Spider):
    name = "Collection54"
    allowed_domains = ['shmmc.com.cn']
    start_urls = ['https://www.shmmc.com.cn/Home/ZdzpList']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.DefaultMiddleware': 0,
        },
    }

    def parse(self, response, **kwargs):
        #/html/body/div[2]/div[2]/div/div[2]/div[2]/div/table/tbody/tr[3]/td/div/div/table/tbody/tr/td[1]/table/tbody/tr/td[8]
        #/html/body/div[2]/div[2]/div/div[2]/div[2]/div/table/tbody/tr[3]/td/div/div/table/tbody/tr/td[1]/table/tbody/tr/td[7]
        li_list = response.xpath("/html/body/div[2]/div[2]/div/div[2]/div[2]/div/table//tr[3]/td/div/div/table//tr/td[1]/table//tr/td")
        #print(li_list)
        for td in li_list:
            item = CollectionItem()
            item["museumID"] = 54
            item["museumName"] = "上海中国航海博物馆"

            # 名字的xpath都一样
            #/html/body/div[2]/div[2]/div/div[2]/div[2]/div/table/tbody/tr[3]/td/div/div/table/tbody/tr/td[1]/table/tbody/tr/td[7]/span
            item['collectionName'] = td.xpath("./span/text()").extract_first()

            # 注意是否为全路径，一般后缀为@src有的是@oldsrc
            #https://www.shmmc.com.cn/mup/image/20170107215348_9198.jpg
            #/html/body/div[2]/div[2]/div/div[2]/div[2]/div/table/tbody/tr[3]/td/div/div/table/tbody/tr/td[1]/table/tbody/tr/td[7]/a/img

            item['collectionImageLink'] = "https://www.shmmc.com.cn/"+td.xpath(
                "./a/img/@src").extract_first()

            #注意是否是全路径
            #怎么判断是否是全路径
            #/html/body/div[2]/div[2]/div/div[2]/div[2]/div/table/tbody/tr[3]/td/div/div/table/tbody/tr/td[1]/table/tbody/tr/td[7]/a
            #https://www.shmmc.com.cn/Home/ww_detail?id=a8c8006cf702e55c
            url = "https://www.shmmc.com.cn/"+str(td.xpath("./a/@href").extract_first())

            yield scrapy.Request(
                url,
                callback=self.parseAnotherPage,
                meta={"item": item}
            )
    #翻页
    #/html/body/div[2]/div[2]/div/div[2]/div[2]/div/table/tbody/tr[3]/td/div/div/table/tbody/tr/td[1]/table/tbody/tr/td[8]/a
    def parseAnotherPage(self, response):
        r = re.compile(u"\\n|\\r|\\[.*?]|\\t")
        item = response.meta["item"]
        #/html/body/div[2]/div[2]/div/div/div[2]/div/div/div/p[1]
        #/html/body/div[2]/div[2]/div/div/div[2]/div/div/div/p[1]
        item["collectionIntroduction"] = response.xpath(
            'normalize-space(/html/body/div[2]/div[2]/div/div/div[2]/div/div/div/p[1])').extract_first()
        item["collectionIntroduction"] = "".join(item["collectionIntroduction"].split())
        item["collectionIntroduction"] = re.sub(r, '', item["collectionIntroduction"])
        print(item)
        yield item
