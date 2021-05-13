from ..items import *
from ..str_filter import *

class Exhibition33(scrapy.Spider):
    name = "Exhibition33"
    allowed_domains = ['cfbwg.org.cn']
    start_urls = ['http://www.cfbwg.org.cn/list-6.html#7']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.ExhibitionPipeLine': 302,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.DefaultMiddleware': 0,
        },
    }

    def parse(self, response, **kwargs):
        item = ExhibitionItem()
        item["museumID"] = 33
        item["museumName"] = "赤峰博物馆"

        # 名字的xpath都一样
        # /html/body/div[2]/div[1]/div/div[1]/div/h3
        item["exhibitionName"] = response.xpath("/html/body/div[2]/div[1]/div/div[1]/div/h3/text()").extract_first()

        #/html/body/div[2]/div[2]/div/div[1]/img
        item["exhibitionImageLink"] = str(response.xpath(
                "/html/body/div[2]/div[1]/div/div[2]/img/@src").extract_first())

        # /html/body/div[2]/div[1]/div/div[1]/div/p[1]
        item["exhibitionTime"] = StrFilter.filter(
                response.xpath("/html/body/div[2]/div[1]/div/div[1]/div/p[1]").xpath('string(.)').extract_first())

        # /html/body/div[2]/div[1]/div/div[1]/div/p[2]
        item['exhibitionIntroduction'] = StrFilter.filter_2(
            response.xpath("/html/body/div[2]/div[1]/div/div[1]/div/p[2]").xpath('string(.)').extract_first())
        print(item)
        yield item
