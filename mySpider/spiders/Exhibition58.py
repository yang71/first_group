from ..items import *
from ..str_filter import *

class Exhibition58(scrapy.Spider):
    name = "Exhibition58"
    allowed_domains = ['ntmuseum.com']
    start_urls = ['http://www.ntmuseum.com/colunm3/col4/']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.ExhibitionPipeLine': 302,
        },
         'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.DefaultMiddleware': 0,
        },
    }


    def parse(self, response, **kwargs):
            #/html/body/section[2]/div[3]/div[1]/ul/li[1]
        li_list = response.xpath("/html/body/section[2]/div[3]/div[1]/ul/li")
        # print(li_list)
        for li in li_list:
            item = ExhibitionItem()
            item["museumID"] = 58
            item["museumName"] = "南通博物苑"

            #名字的xpath都一样
            #/html/body/section[2]/div[3]/div[1]/ul/li[1]/a
            item['exhibitionName'] = StrFilter.filter(
                li.xpath("./a").xpath('string(.)').extract_first())

            #/html/body/section[2]/div[3]/div[1]/ul/li[1]/span
            item["exhibitionTime"] = StrFilter.filter(
                li.xpath("./span").xpath('string(.)').extract_first())

            #http://www.19371213.com.cn/exhibition/temporary/202104/t20210430_2902013.html
            #/html/body/section[2]/div[3]/div[1]/ul/li[1]/a
            str3 = str(li.xpath("./a/@href").extract_first())
            url = str3

            yield scrapy.Request(
                url,
                callback=self.parseAnotherPage,
                meta={"item": item}
            )

    def parseAnotherPage(self, response):
        item = response.meta["item"]

        #/html/body/section[2]/div[3]/div/div/ul/li[3]/div[1]/img
        #/html/body/section[2]/div[3]/div/div/ul/li[3]/div[1]/img
        #http://www.ntmuseum.com/uploads/allimg/201231/1-20123114595U07.jpg
        str1 = 'http://www.ntmuseum.com/'
        str2 = str(response.xpath(
            "/html/body/section[2]/div[3]/div/div/ul/li[3]/div[1]/img/@src").extract_first())
        item["exhibitionImageLink"] = str1 + str2

        #/html/body/section[2]/div[3]/div/div/ul/li[3]
        item['exhibitionIntroduction'] = StrFilter.filter(
            response.xpath("/html/body/section[2]/div[3]/div/div/ul/li[3]").xpath('string(.)').extract_first())
        print(item)
        yield item
