#
from ..items import *
from ..str_filter import *

class Exhibition168(scrapy.Spider):
    name = "Exhibition168"
    allowed_domains = ['cdmuseum.com']
    start_urls = ['https://www.cdmuseum.com/zhanlan/']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.ExhibitionPipeLine': 302,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.DefaultMiddleware': 0,
        },
    }

    def parse(self, response, **kwargs):
        li_list = response.xpath(
            "/html/body/div[3]/div[2]/ul/li")
        print(len(li_list))
        for li in li_list:
            item = ExhibitionItem()
            item["museumID"] = 168
            item["museumName"] = "成都博物馆"
            item["exhibitionImageLink"] ='https://www.cdmuseum.com'+str(li.xpath(
                "./a/div[1]/img/@src").extract_first())
            item["exhibitionName"] = StrFilter.filter_2(li.xpath("./a/div[2]/div[1]/div[1]/p[2]/text()").extract_first())
            item["exhibitionTime"] = StrFilter.filter_2(li.xpath("./a/div[2]/div[1]/div[2]/p[2]/text()").extract_first())
            item['exhibitionIntroduction'] = StrFilter.filter_2(li.xpath("./a/div[2]/div[2]/p/text()").extract_first())
            print(item)
            yield item
