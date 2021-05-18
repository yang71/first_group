#
from ..items import *
from ..str_filter import *

class Exhibition146(scrapy.Spider):
    name = "Exhibition146"
    allowed_domains = ['baike.baidu.com']
    start_urls = ['https://baike.baidu.com/item/%E8%A5%BF%E6%B1%89%E5%8D%97%E8%B6%8A%E7%8E%8B%E5%8D%9A%E7%89%A9%E9%A6%86/1786642?fr=aladdin#4']

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
            item["museumID"] = 146
            item["museumName"] = "西汉南越王博物馆"
            item["exhibitionImageLink"] ='https://baike.baidu.com'+str(li.xpath(
                "./div[36]/a[1]/@href").extract_first())
            item["exhibitionName"] = StrFilter.filter_2(li.xpath("./div[35]/h3/text()").extract_first())
            item["exhibitionTime"] = "常设展览"
            item['exhibitionIntroduction'] = StrFilter.filter_2(li.xpath("./div[36]/text()[3]").extract_first())
            print(item)
            yield item
