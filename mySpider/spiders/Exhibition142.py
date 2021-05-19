#
from ..items import *
from ..str_filter import *

class Exhibition142(scrapy.Spider):
    name = "Exhibition142"
    allowed_domains = ['chinajiandu.cn']
    start_urls = ['http://www.chinajiandu.cn/Exhibition/Index']

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
            "/html/body/div[3]/div/div/div/ul/li")
        print(len(li_list))
        for li in li_list:
            item = ExhibitionItem()
            item["museumID"] = 142
            item["museumName"] = "长沙简牍博物馆"
            item["exhibitionImageLink"] =str(li.xpath(
                "./a/img/@src").extract_first())
            item["exhibitionName"] = StrFilter.filter_2(li.xpath("./div/a/h3").extract_first())
            item["exhibitionTime"] = None
            item['exhibitionIntroduction'] = None
            print(item)
            yield item
