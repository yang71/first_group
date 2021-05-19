#
from ..items import *
from ..str_filter import *

class Exhibition167(scrapy.Spider):
    name = "Exhibition167"
    allowed_domains = ['zgshm.cn']
    start_urls = ['http://www.zgshm.cn/imglist.jsp?id=78abd44f3517405da73197aa6e9b0ccb']

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
            "/html/body/ul/li")
        print(len(li_list))
        for li in li_list:
            item = ExhibitionItem()
            item["museumID"] = 167
            item["museumName"] = "自贡市盐业历史博物馆"
            item["exhibitionImageLink"] ='http://www.zgshm.cn'+str(li.xpath(
                "./img/@src").extract_first())
            item["exhibitionName"] = StrFilter.filter_2(li.xpath("./div/label/text()").extract_first())
            item["exhibitionTime"] = "常设展览"
            item['exhibitionIntroduction'] = StrFilter.filter_2(li.xpath("./div/p/text()").extract_first())
            print(item)
            yield item
