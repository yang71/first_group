#
from ..items import *
from ..str_filter import *

class Exhibition154(scrapy.Spider):
    name = "Exhibition154"
    allowed_domains = ['msrmuseum.com']
    start_urls = ['https://www.msrmuseum.com/News/Index/27']

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
            "/html/body/div[1]/div[3]/div/div[1]/ul/li")
        print(len(li_list))
        for li in li_list:
            item = ExhibitionItem()
            item["museumID"] = 154
            item["museumName"] = "广东海上丝绸之路博物馆"
            item["exhibitionImageLink"] ='https://www.msrmuseum.com'+str(li.xpath(
                "./a/span/img/@src").extract_first())
            item["exhibitionName"] = StrFilter.filter_2(li.xpath("./a/strong/text()").extract_first())
            item["exhibitionTime"] = None
            item['exhibitionIntroduction'] = StrFilter.filter_2(li.xpath("./a/strong/text()").extract_first())
            print(item)
            yield item
