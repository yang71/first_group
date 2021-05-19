#
from ..items import *
from ..str_filter import *

class Exhibition169(scrapy.Spider):
    name = "Exhibition169"
    allowed_domains = ['jc-museum.cn']
    start_urls = ['https://www.jc-museum.cn/display/list-7/']

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
            "/html/body/div[2]/div[4]/div[2]/ul/li")
        print(len(li_list))
        for li in li_list:
            item = ExhibitionItem()
            item["museumID"] = 169
            item["museumName"] = "四川省建川博物馆"
            item["exhibitionImageLink"] ='https://www.jc-museum.cn'+str(li.xpath(
                "./a/span/img/@src").extract_first())
            item["exhibitionName"] = StrFilter.filter_2(li.xpath("./a/p/text()").extract_first())
            item["exhibitionTime"] = "常设展览"
            item['exhibitionIntroduction'] = StrFilter.filter_2(li.xpath("./a/p/text()").extract_first())
            print(item)
            yield item
