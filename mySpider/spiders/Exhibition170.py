#
from ..items import *
from ..str_filter import *

class Exhibition170(scrapy.Spider):
    name = "Exhibition170"
    allowed_domains = ['jinshasitemuseum.com']
    start_urls = ['http://www.jinshasitemuseum.com/Exhibition/ExhibitionSpecial']

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
            "/html/body/div[3]/div/div[2]/div[2]/div[2]/div/div/div/div")
        print(len(li_list))
        for li in li_list:
            item = ExhibitionItem()
            item["museumID"] = 170
            item["museumName"] = "5·12汶川特大地震纪念馆"
            item["exhibitionImageLink"] ='https://baike.baidu.com'+str(li.xpath(
                "/html/body/div[3]/div[2]/div/div[1]/div[58]/div/a/@href").extract_first())
            item["exhibitionName"] = StrFilter.filter_2(li.xpath("/html/body/div[3]/div[2]/div/div[1]/div[58]/div/span/text()").extract_first())
            item["exhibitionTime"] = None
            item['exhibitionIntroduction'] = StrFilter.filter_2(li.xpath("/html/body/div[3]/div[2]/div/div[1]/div[58]/text()").extract_first())
            print(item)
            #yield item
