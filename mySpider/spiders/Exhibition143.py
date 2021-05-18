#
from ..items import *
from ..str_filter import *

class Exhibition143(scrapy.Spider):
    name = "Exhibition143"
    allowed_domains = ['baike.baidu.com']
    start_urls = ['https://baike.baidu.com/item/%E9%95%BF%E6%B2%99%E5%B8%82%E5%8D%9A%E7%89%A9%E9%A6%86/8711557?fr=aladdin#2_2']

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
            item["museumID"] = 143
            item["museumName"] = "长沙市博物馆"
            item["exhibitionImageLink"] ='https://baike.baidu.com' +str(li.xpath(
                "/html/body/div[3]/div[2]/div/div[1]/div[24]/div/a/@href").extract_first())
            item["exhibitionName"] = StrFilter.filter_2(li.xpath("./ul[2]/li/div/b").extract_first().replace('<b>','').replace('</b>',''))
            item["exhibitionTime"] = None
            item['exhibitionIntroduction'] = StrFilter.filter_2(li.xpath("./div[24]/text()[1]").extract_first())
            print(item)
            yield item
