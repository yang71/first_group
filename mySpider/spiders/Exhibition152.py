#
from ..items import *
from ..str_filter import *

class Exhibition152(scrapy.Spider):
    name = "Exhibition152"
    allowed_domains = ['zgkjbwg.com']
    start_urls = ['http://www.zgkjbwg.com/zwgk/zl/zlhg/t20181031_625.htm']

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
            "/html/body/div[1]/div[2]/div[2]/div[2]")
        print(len(li_list))
        for li in li_list:
            item = ExhibitionItem()
            item["museumID"] = 152
            item["museumName"] = "广东中国客家博物馆"
            item["exhibitionImageLink"] ='http://www.zgkjbwg.com'+str(li.xpath(
                "./div[3]/section[1]/section/section/p[2]/span/span/a/@href").extract_first())
            item["exhibitionName"] = StrFilter.filter_2(li.xpath("./div[1]/h1").extract_first().replace('<h1>','').replace('</h1>',''))
            item["exhibitionTime"] = None
            item['exhibitionIntroduction'] = StrFilter.filter_2(li.xpath("./div[3]/section[3]/section/section/section[2]/section/section/p[2]/span/span[3]/text()").extract_first())
            print(item)
            yield item
