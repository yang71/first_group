from ..items import *
from ..str_filter import *


class Collection53(scrapy.Spider):
    name = "Collection53"
    allowed_domains = ['cyjng.net']
    start_urls = ['http://www.cyjng.net/Default.aspx?tabid=62&language=zh-CN']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        }
    }

    def parse(self, response, **kwargs):
        li_list = response.xpath("/html/body/form/table//tr/td/table//tr[3]/td/table//tr[3]/td/table//tr/td[3]/div/span/span/div/div/table[1]//tr[1]/td")
        print(li_list)
        for td in li_list:
            item = CollectionItem()
            item["museumID"] = 53
            item["museumName"] = "陈云纪念馆"
            print(111)
            #注意是否是全路径
            #怎么判断是否是全路径
            #/html/body/form/table/tbody/tr/td/table/tbody/tr[3]/td/table/tbody/tr[3]/td/table/tbody/tr/td[3]/div/span/span/div/div/table[1]/tbody/tr[1]/td[1]/table/tbody/tr/td/a
            url = "http://www.cyjng.net/"+str(td.xpath("./table//tr/td/a/@href").extract_first())
            yield scrapy.Request(
                url,
                callback=self.parseAnotherPage,
                meta={"item": item}
            )
    #翻页
    def parseAnotherPage(self, response):

        r = re.compile(u"\\n|\\r|\\[.*?]|\\t")
        item = response.meta["item"]
        # 名字的xpath都一样
        #/html/body/form/div[3]/table/tbody/tr/td/table/tbody/tr[3]/td/table/tbody/tr[3]/td/table/tbody/tr/td/div/div[2]/div/div/div/table[1]/tbody/tr[1]/td/div/span
        #/html/body/form/div[3]/table/tbody/tr/td/table/tbody/tr[3]/td/table/tbody/tr[3]/td/table/tbody/tr/td/div/div[2]/div/div/div/table[1]/tbody/tr[1]/td/div/span
        item['collectionName'] = response.xpath("/html/body/form/div[3]/table//tr/td/table//tr[3]/td/table//tr[3]/td/table//tr/td/div/div[2]/div/div/div/table[1]//tr[1]/td/div/span/text()").extract_first()

        # 注意是否为全路径，一般后缀为@src,有的是@oldsrc
        # http://www.cyjng.net/DesktopModules/Articles/MakeThumbnail.aspx?Image=%2fPortals%2f0%2f%e6%8d%90%e6%ac%be%e6%94%b6%e6%8d%ae+%e6%8b%b7%e8%b4%9d.jpg&tabid=62&w=550&h=400
        # /html/body/form/div[3]/table/tbody/tr/td/table/tbody/tr[3]/td/table/tbody/tr[3]/td/table/tbody/tr/td/div/div[2]/div/div/div/table[2]/tbody/tr/td/table/tbody/tr[1]/td/img
        item['collectionImageLink'] = "http://www.cyjng.net/" + response.xpath(
            "/html/body/form/div[3]/table//tr/td/table//tr[3]/td/table//tr[3]/td/table//tr/td/div/div[2]/div/div/div/table[2]//tr/td/table//tr[1]/td/img/@src").extract_first()

        item["collectionIntroduction"] = response.xpath(
            'normalize-space(/html/body/form/div[3]/table//tr/td/table//tr[3]/td/table//tr[3]/td/table//tr/td/div/div[2]/div/div/div/table[2]//tr/td/table//tr[2]/td/span/p)').extract_first()
        item["collectionIntroduction"] = "".join(item["collectionIntroduction"].split())
        item["collectionIntroduction"] = re.sub(r, '', item["collectionIntroduction"])
        print(item)
        yield item
