#
from ..items import *
from ..str_filter import *

class Exhibition165(scrapy.Spider):
    name = "Exhibition165"
    allowed_domains = ['baike.baidu.com']
    start_urls = ['https://baike.baidu.com/item/%E6%88%90%E9%83%BD%E6%AD%A6%E4%BE%AF%E7%A5%A0%E5%8D%9A%E7%89%A9%E9%A6%86/675256?fr=aladdin#5']

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
            "/html/body/div[3]/div[2]/div/div[1]/div[58]")
        print(len(li_list))
        for li in li_list:
            item = ExhibitionItem()
            item["museumID"] = 165
            item["museumName"] = "四川博物院"
            item["exhibitionImageLink"] ='https://baike.baidu.com'+str(li.xpath(
                "/html/body/div[3]/div[2]/div/div[1]/div[58]/div/a/@href").extract_first())
            item["exhibitionName"] = StrFilter.filter_2(li.xpath("/html/body/div[3]/div[2]/div/div[1]/div[58]/div/span/text()").extract_first())
            item["exhibitionTime"] = None
            item['exhibitionIntroduction'] = StrFilter.filter_2(li.xpath("/html/body/div[3]/div[2]/div/div[1]/div[58]/text()").extract_first())
            print(item)
            #yield item
