#
from ..items import *
from ..str_filter import *

class Exhibition161(scrapy.Spider):
    name = "Exhibition161"
    allowed_domains = ['sxd.cn']
    start_urls = ['http://www.sxd.cn/showinfo.asp?id=1821&bigclass=23']

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
            "/html/body/div/div[2]/div[2]/table[2]/tbody/tr/td[2]/table/tbody/tr[2]/td/table")
        print(len(li_list))
        for li in li_list:
            item = ExhibitionItem()
            item["museumID"] = 161
            item["museumName"] = "三星堆博物馆"
            item["exhibitionImageLink"] ='http://www.sxd.cn'+str(li.xpath(
                "./tbody/tr[2]/td/p[4]/img/@src").extract_first())
            item["exhibitionName"] = StrFilter.filter_2(li.xpath("./tbody/tr[1]/td").extract_first())
            item["exhibitionTime"] = None
            item['exhibitionIntroduction'] = StrFilter.filter_2(li.xpath("./tbody/tr[2]/td/p[2]/text()").extract_first())
            print(item)
            #yield item
