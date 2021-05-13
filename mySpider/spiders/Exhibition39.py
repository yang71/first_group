from ..items import *
from ..str_filter import *

class Exhibition39(scrapy.Spider):
    name = "Exhibition39"
    allowed_domains = ['dlnm.org.cn']
    start_urls = ['http://www.dlnm.org.cn/?_f=themexihibition']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.ExhibitionPipeLine': 302,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.DefaultMiddleware': 0,
        },
    }

    def parse(self, response, **kwargs):
            #/html/body/div/div[3]/div[1]/div[2]/ul/li[1]
        li_list = response.xpath("/html/body/div/div[3]/div[1]/div[2]/ul/li")
        # print(li_list)
        for li in li_list:
            item = ExhibitionItem()
            item["museumID"] = 39
            item["museumName"] = "大连自然博物馆"

            #名字的xpath都一样
            #/html/body/div/div[3]/div[1]/div[2]/ul/li[1]/a/div[2]/div/div/h4
            item['exhibitionName'] = StrFilter.filter(
            li.xpath("./a/div[2]/div/div/h4").xpath('string(.)').extract_first())

            #/html/body/div/div[3]/div[1]/div[2]/ul/li[1]/a/div[1]/img
            #https://www.dlmodernmuseum.com/static/upload/2020/09/15/0ef3860d4ab67663.jpg
            # str1 = 'https://www.dlmodernmuseum.com/'
            str2 = str(li.xpath(
                "./a/div[1]/img/@src").extract_first())
            item["exhibitionImageLink"] = str2

            #/html/body/div/div[3]/div[1]/div[2]/ul/li[1]/a/div[2]/div/div/div/p[1]
            item["exhibitionTime"] = StrFilter.filter(
                li.xpath("./a/div[2]/div/div/div/p[1]").xpath('string(.)').extract_first())

            #http://www.dlnm.org.cn/?_f=themexihibition_detail&id=33
            #/html/body/div/div[3]/div[1]/div[2]/ul/li[1]/a
            url = "http://www.dlnm.org.cn/" + str(li.xpath("./a/@href").extract_first())

            yield scrapy.Request(
                url,
                callback=self.parseAnotherPage,
                meta={"item": item}
            )

    def parseAnotherPage(self, response):
        item = response.meta["item"]

        #/html/body/div[6]
        item['exhibitionIntroduction'] = StrFilter.filter(
            response.xpath("/html/body/div[1]/div[3]/div[1]/div[2]/div[2]/div[2]/div").xpath('string(.)').extract_first())
        print(item)
        yield item
