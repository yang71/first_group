from ..items import *
from ..str_filter import *


class Collection71(scrapy.Spider):
    name = "Collection71"
    allowed_domains = ['chinasilkmuseum.com']
    start_urls = ['https://www.chinasilkmuseum.com/zggd/list_21.aspx?page=1',
                  'https://www.chinasilkmuseum.com/zggd/list_21.aspx?page=2',
                  'https://www.chinasilkmuseum.com/zggd/list_21.aspx?page=3']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.DefaultMiddleware': 0,
        },
    }

    def parse(self, response, **kwargs):
            #/html/body/div[1]/div/div[8]/div/ul/li[1]
        li_list = response.xpath("/html/body/div[1]/div/div[8]/div/ul/li")
        #print(li_list)
        for li in li_list:
            item = CollectionItem()
            item["museumID"] = 71
            item["museumName"] = "中国丝绸博物馆"

            # 名字的xpath都一样
            #/html/body/div[1]/div/div[8]/div/ul/li[1]/p/a
            item['collectionName'] = li.xpath("./p/a/text()").extract_first()

            # 注意是否为全路径，一般后缀为@src有的是@oldsrc
            #https://www.chinasilkmuseum.com/uploadfiles/downloadimg/20171229172558390.jpg
            #/html/body/div[1]/div/div[8]/div/ul/li[1]/a/img

            item['collectionImageLink'] = "https://www.chinasilkmuseum.com/"+li.xpath(
                "./a/img/@src").extract_first()

            #注意是否是全路径
            #怎么判断是否是全路径
            #/html/body/div[1]/div/div[8]/div/ul/li[1]/a
            #https://www.chinasilkmuseum.com/zggd/info_21.aspx?itemid=3316
            url = "https://www.chinasilkmuseum.com/"+str(li.xpath("./a/@href").extract_first())

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
        #/html/body/div[1]/div/div[2]/div/div[2]/p[6]
        item["collectionIntroduction"] = response.xpath(
            'normalize-space(/html/body/div[1]/div/div[2]/div/div[2])').extract_first()
        item["collectionIntroduction"] = "".join(item["collectionIntroduction"].split())
        item["collectionIntroduction"] = re.sub(r, '', item["collectionIntroduction"])
        print(item)
        yield item
