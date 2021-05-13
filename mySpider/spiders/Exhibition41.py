from ..items import *
from ..str_filter import *

class Exhibition41(scrapy.Spider):
    name = "Exhibition41"
    allowed_domains = ['jlmuseum.org']
    start_urls = ['http://www.jlmuseum.org/display']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.ExhibitionPipeLine': 302,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.DefaultMiddleware': 0,
        },
    }

    def parse(self, response, **kwargs):
            #/html/body/div[2]/div[2]/div[2]/ul/li[1]
        li_list = response.xpath("/html/body/div[2]/div[2]/div[2]/ul/li")
        # print(li_list)
        for li in li_list:
            item = ExhibitionItem()
            item["museumID"] = 40
            item["museumName"] = "吉林省博物院"

            #名字的xpath都一样
            #/html/body/div[2]/div[2]/div[2]/ul/li[1]/div/div
            item['exhibitionName'] = StrFilter.filter(
            li.xpath("./div/div").xpath('string(.)').extract_first())

            #/html/body/div[2]/div[2]/div[2]/ul/li[1]/a/img
            #http://www.jlmuseum.org/Uploads/201609/57eb3ed74d65d.jpg
            str1 = 'http://www.jlmuseum.org/'
            str2 = str(li.xpath(
                "./a/img/@src").extract_first())
            item["exhibitionImageLink"] = str1 + str2

            #/html/body/div/div[3]/div[1]/div[2]/ul/li[1]/a/div[2]/div/div/div/p[1]
            item["exhibitionTime"] = None

            #http://www.jlmuseum.org/display/show/1599.html
            #/html/body/div[2]/div[2]/div[2]/ul/li[1]/a
            url = "http://www.jlmuseum.org/" + str(li.xpath("./a/@href").extract_first())

            yield scrapy.Request(
                url,
                callback=self.parseAnotherPage,
                meta={"item": item}
            )

    def parseAnotherPage(self, response):
        item = response.meta["item"]

        #/html/body/div[6]
        item['exhibitionIntroduction'] = StrFilter.filter(
            response.xpath("/html/body/div[2]/div[2]/div[2]/div").xpath('string(.)').extract_first())
        print(item)
        yield item
