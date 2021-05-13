from ..items import *
from ..str_filter import *

class Exhibition50(scrapy.Spider):
    name = "Exhibition50"
    allowed_domains = ['luxunmuseum.cn']
    start_urls = ['http://www.luxunmuseum.cn/news/index/cid/3.html']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.ExhibitionPipeLine': 302,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.DefaultMiddleware': 0,
        },
    }

    def parse(self, response, **kwargs):
            #/html/body/div[3]/div[1]/article[1]
        li_list = response.xpath("/html/body/div[3]/div[1]/article")
        # print(li_list)
        for li in li_list:
            item = ExhibitionItem()
            item["museumID"] = 50
            item["museumName"] = "上海鲁迅纪念馆"

            # 名字的xpath都一样
            # /html/body/div[3]/div[1]/article[1]/h3/a
            item['exhibitionName'] = StrFilter.filter(
                li.xpath("./h3/a").xpath('string(.)').extract_first())

            #/html/body/div[3]/div[1]/article[1]/h3/a
            #http://www.luxunmuseum.cn/news/page/id/200.html
            url = "http://www.luxunmuseum.cn/" + str(li.xpath("./h3/a/@href").extract_first())

            yield scrapy.Request(
                url,
                callback=self.parseAnotherPage,
                meta={"item": item}
            )

    def parseAnotherPage(self, response):
        item = response.meta["item"]

        item["exhibitionImageLink"] = None

        #/html/body/div[3]/div[1]/p
        item["exhibitionTime"] = StrFilter.filter(
                response.xpath("/html/body/div[3]/div[1]/p").xpath('string(.)').extract_first())

        #/html/body/div[3]/div[1]/div[2]
        item['exhibitionIntroduction'] = StrFilter.filter(
            response.xpath("/html/body/div[3]/div[1]/div[2]").xpath('string(.)').extract_first())
        print(item)
        yield item
