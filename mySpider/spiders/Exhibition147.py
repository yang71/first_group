#
from ..items import *
from ..str_filter import *

class Exhibition147(scrapy.Spider):
    name = "Exhibition147"
    allowed_domains = ['sunyat-sen.org']
    start_urls = ['http://www.sunyat-sen.org/index.php?m=content&c=index&a=lists&catid=53']

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
            "/html/body/div[4]/div[2]/ul/li")
        print(len(li_list))
        for li in li_list:
            item = ExhibitionItem()
            item["museumID"] = 147
            item["museumName"] = "孙中山故居纪念馆"
            item["exhibitionImageLink"] ='http://www.sunyat-sen.org'+str(li.xpath(
                "./img/@src").extract_first())
            item["exhibitionName"] = StrFilter.filter_2(li.xpath("./text()").extract_first())
            item["exhibitionTime"] = None
            item['exhibitionIntroduction'] = StrFilter.filter_2(li.xpath("./text()").extract_first())
            print(item)
            yield item
