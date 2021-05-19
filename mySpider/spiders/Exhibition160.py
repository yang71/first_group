#
from ..items import *
from ..str_filter import *

class Exhibition160(scrapy.Spider):
    name = "Exhibition160"
    allowed_domains = ['zdm.cn']
    start_urls = ['http://www.zdm.cn/cooperation.html']

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
            "/html/body/section[2]/div[3]/div[2]/div")
        print(len(li_list))
        for li in li_list:
            item = ExhibitionItem()
            item["museumID"] = 160
            item["museumName"] = "自贡恐龙博物馆"
            item["exhibitionImageLink"] =str(li.xpath(
                "./a/div/img/@src").extract_first())
            item["exhibitionName"] = StrFilter.filter_2(li.xpath("./a/p/text()").extract_first())
            item["exhibitionTime"] = None
            item['exhibitionIntroduction'] = StrFilter.filter_2(li.xpath("./a/p/text()").extract_first())
            print(item)
            yield item
