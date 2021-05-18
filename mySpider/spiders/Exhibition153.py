#
from ..items import *
from ..str_filter import *

class Exhibition153(scrapy.Spider):
    name = "Exhibition153"
    allowed_domains = ['baike.baidu.com']
    start_urls = ['https://baike.baidu.com/item/%E9%B8%A6%E7%89%87%E6%88%98%E4%BA%89%E5%8D%9A%E7%89%A9%E9%A6%86/1880085?fr=aladdin#4']

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
            item["museumID"] = 153
            item["museumName"] = "鸦片战争博物馆"
            item["exhibitionImageLink"] ='https://baike.baidu.com'+str(li.xpath(
                "./div[72]/div/a/@href").extract_first())
            item["exhibitionName"] = StrFilter.filter_2(li.xpath("./div[72]/b").extract_first().replace('<b>','').replace('</b>',''))
            item["exhibitionTime"] = "常设展览"
            item['exhibitionIntroduction'] = StrFilter.filter_2(li.xpath("./div[72]/text()").extract_first())
            print(item)
            yield item
