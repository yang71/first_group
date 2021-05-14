from ..items import *
from ..str_filter import *

class Exhibition59(scrapy.Spider):
    name = "Exhibition59"
    allowed_domains = ['szmuseum.com']
    start_urls = ['https://www.szmuseum.com/Exhibition/Temporary?startYear=2021-05-13']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.ExhibitionPipeLine': 302,
        },
         'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.DefaultMiddleware': 0,
        },
    }


    def parse(self, response, **kwargs):
            #/html/body/div[4]/div[3]/div[1]/ul/li[1]
        li_list = response.xpath("/html/body/div[4]/div[3]/div[1]/ul/li")
        # print(li_list)
        for li in li_list:
            item = ExhibitionItem()
            item["museumID"] = 59
            item["museumName"] = "苏州博物馆"

            #名字的xpath都一样
            #/html/body/div[4]/div[3]/div[1]/ul/li[1]/div/h1/a
            item['exhibitionName'] = StrFilter.filter(
                li.xpath("./div/h1/a").xpath('string(.)').extract_first())

            #/html/body/div[4]/div[3]/div[1]/ul/li[1]/div/div/div/p[1]/span[2]
            item["exhibitionTime"] = StrFilter.filter(
                li.xpath("./div/div/div/p[1]/span[2]").xpath('string(.)').extract_first())

            #/html/body/div[4]/div[3]/div[1]/ul/li[1]/a/i/img
            # str1 = 'http://www.ntmuseum.com/'
            str2 = str(li.xpath(
                "./a/i/img/@src").extract_first())
            item["exhibitionImageLink"] = str2

            #https://www.szmuseum.com/Exhibition/TemporaryDetails/074036b4-63bd-46cf-a7f9-d644eefdd5c8?startYear=2021-05-13
            #/html/body/div[4]/div[3]/div[1]/ul/li[1]/div/h1/a
            str3 = "https://www.szmuseum.com/" + str(li.xpath("./div/h1/a/@href").extract_first())
            url = str3

            yield scrapy.Request(
                url,
                callback=self.parseAnotherPage,
                meta={"item": item}
            )

    def parseAnotherPage(self, response):
        item = response.meta["item"]

        #/html/body/div[4]/div[3]/div/div[2]
        item['exhibitionIntroduction'] = StrFilter.filter(
            response.xpath("/html/body/div[4]/div[3]/div/div[2]").xpath('string(.)').extract_first())
        print(item)
        yield item
