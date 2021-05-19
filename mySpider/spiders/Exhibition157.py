#
from ..items import *
from ..str_filter import *

class Exhibition157(scrapy.Spider):
    name = "Exhibition157"
    allowed_domains = ['guilinmuseum.org.cn']
    start_urls = ['http://www.guilinmuseum.org.cn/Exhibition/Temporary/lszl']

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
            "/html/body/div[4]/div/div/ul/li")
        print(len(li_list))
        for li in li_list:
            item = ExhibitionItem()
            item["museumID"] = 157
            item["museumName"] = "桂林博物馆"
            item["exhibitionImageLink"] =str(li.xpath(
                "./a/div/img/@src").extract_first())
            item["exhibitionName"] = StrFilter.filter_2(li.xpath("./div/a[1]/h3/text()").extract_first())
            item["exhibitionTime"] = None
            item['exhibitionIntroduction'] = StrFilter.filter_2(li.xpath("./div/div/p/text()").extract_first())
            print(item)
            yield item
