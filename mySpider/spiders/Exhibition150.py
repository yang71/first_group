#
from ..items import *
from ..str_filter import *

class Exhibition150(scrapy.Spider):
    name = "Exhibition150"
    allowed_domains = ['baike.baidu.com']
    start_urls = ['https://baike.baidu.com/item/%E5%B9%BF%E4%B8%9C%E6%B0%91%E9%97%B4%E5%B7%A5%E8%89%BA%E5%8D%9A%E7%89%A9%E9%A6%86/1627374?fr=aladdin#2']

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
            "/html/body/div[3]/div[2]/div/div[1]")
        print(len(li_list))
        for li in li_list:
            item = ExhibitionItem()
            item["museumID"] = 150
            item["museumName"] = "广东民间工艺博物馆"
            item["exhibitionImageLink"] =str(li.xpath(
                "./div[22]/div/a/img/@src").extract_first())
            item["exhibitionName"] = StrFilter.filter_2(li.xpath("./div[22]/text()").extract_first())
            item["exhibitionTime"] = None
            item['exhibitionIntroduction'] = StrFilter.filter(li.xpath("./div[22]").extract_first())
            print(item)
            yield item
