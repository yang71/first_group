from ..items import *
from ..str_filter import *

class Exhibition48(scrapy.Spider):
    name = "Exhibition48"
    allowed_domains = ['hljsmzbwg.com']
    start_urls = ['http://www.hljsmzbwg.com/lszl.html']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.ExhibitionPipeLine': 302,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.DefaultMiddleware': 0,
        },
    }

    def parse(self, response, **kwargs):
            #/html/body/div[3]/div[2]/div[2]/div/ul/li[1]
        li_list = response.xpath("/html/body/div[3]/div[2]/div[2]/div/ul/li")
        # print(li_list)
        for li in li_list:
            item = ExhibitionItem()
            item["museumID"] = 48
            item["museumName"] = "黑龙江省民族博物馆"

            # 名字的xpath都一样
            # /html/body/div[3]/div[2]/div[2]/div/ul/li[1]/a/p
            item['exhibitionName'] = StrFilter.filter(
                li.xpath("./a/p").xpath('string(.)').extract_first())

            #/html/body/div[3]/div[2]/div[2]/div/ul/li[1]/a/img
            # http://www.hljmuseum.com/att/news/202105/10/251206172440.jpg
            str1 = 'http:'
            str2 = str(li.xpath(
                "./a/img/@src").extract_first())
            item["exhibitionImageLink"] = str1 + str2


            # /html/body/div[2]/div[3]/div[1]/div[1]/ul/div[1]/li/span
            item["exhibitionTime"] = "临时展览"

            #/html/body/div[3]/div[2]/div[2]/div/ul/li[1]/a
            #http://www.hljsmzbwg.com/28071.html
            url = "http://www.hljsmzbwg.com/" + str(li.xpath("./a/@href").extract_first())

            yield scrapy.Request(
                url,
                callback=self.parseAnotherPage,
                meta={"item": item}
            )

    def parseAnotherPage(self, response):
        item = response.meta["item"]

        #/html/body/div[3]/div[2]/div[2]/section[1]/section/section[2]/p
        #/html/body/div[3]/div[2]/div[2]/section[1]/section/section[2]/p
        item['exhibitionIntroduction'] = StrFilter.filter(
            response.xpath("/html/body/div[3]/div[2]/div[2]/section[1]/section/section[2]/p").xpath('string(.)').extract_first())
        print(item)
        yield item
