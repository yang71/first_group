#
from ..items import *
from ..str_filter import *

class Exhibition145(scrapy.Spider):
    name = "Exhibition145"
    allowed_domains = ['baike.baidu.com']
    start_urls = ['https://baike.baidu.com/item/%E5%B9%BF%E4%B8%9C%E7%9C%81%E5%8D%9A%E7%89%A9%E9%A6%86/1628626?fr=aladdin#3']

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
            "/html/body/div[3]/div[2]/div/div[1]/div")
        print(len(li_list))
        for li in li_list[38:41]:
            item = ExhibitionItem()
            item["museumID"] = 145
            item["museumName"] = "广东省博物馆"
            item["exhibitionImageLink"] ='https://baike.baidu.com'+str(li.xpath(
                "./div/a/@href").extract_first())
            item["exhibitionName"] = StrFilter.filter_2(li.xpath("./div/span/text()").extract_first())
            item["exhibitionTime"] = None
            item['exhibitionIntroduction'] = StrFilter.filter_2(li.xpath("./text()").extract_first())
            print(item)
            yield item
