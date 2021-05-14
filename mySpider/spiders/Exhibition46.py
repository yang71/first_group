from ..items import *
from ..str_filter import *

class Exhibition46(scrapy.Spider):
    name = "Exhibition46"
    allowed_domains = ['hljmuseum.com']
    start_urls = ['http://www.hljmuseum.com/clzl/lszl/myyx/']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.ExhibitionPipeLine': 302,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.DefaultMiddleware': 0,
        },
    }

    def parse(self, response, **kwargs):
            #/html/body/div[2]/div[3]/div[1]/div[1]/ul/div[1]
        li_list = response.xpath("/html/body/div[2]/div[3]/div[1]/div[1]/ul/div")
        # print(li_list)
        for div in li_list:
            item = ExhibitionItem()
            item["museumID"] = 46
            item["museumName"] = "黑龙江省博物馆"

            # 名字的xpath都一样
            # /html/body/div[2]/div[3]/div[1]/div[1]/ul/div[1]/li/a
            item['exhibitionName'] = StrFilter.filter(
                div.xpath("./li/a").xpath('string(.)').extract_first())

            # /html/body/div[2]/div[3]/div[1]/div[1]/ul/div[1]/li/span
            item["exhibitionTime"] = StrFilter.filter(
                div.xpath("./li/span").xpath('string(.)').extract_first())

            #/html/body/div[2]/div[3]/div[1]/div[1]/ul/div[1]/li/a
            #http://www.hljmuseum.com/system/202105/105282.html
            url = "http://www.hljmuseum.com/" + str(div.xpath("./li/a/@href").extract_first())

            yield scrapy.Request(
                url,
                callback=self.parseAnotherPage,
                meta={"item": item}
            )

    def parseAnotherPage(self, response):
        item = response.meta["item"]

        #/html/body/div[2]/div[3]/div[1]/div[1]/div[2]/div[1]/center/img
        #/html/body/div[2]/div[3]/div[1]/div[1]/div[2]/div[1]/center/img
        #http://www.hljmuseum.com/att/news/202105/10/251206172440.jpg
        str1 = 'http://www.hljmuseum.com/'
        str2 = str(response.xpath(
            "/html/body/div[2]/div[3]/div[1]/div[1]/div[2]/div[1]/center/img/@src").extract_first())
        item["exhibitionImageLink"] = str1 + str2

        #/html/body/div[2]/div[3]/div[1]/div[1]/div[2]/div[1]
        item['exhibitionIntroduction'] = StrFilter.filter(
            response.xpath("/html/body/div[2]/div[3]/div[1]/div[1]/div[2]/div[1]").xpath('string(.)').extract_first())
        print(item)
        yield item
