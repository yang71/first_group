#
from ..items import *
from ..str_filter import *

class Exhibition155(scrapy.Spider):
    name = "Exhibition155"
    allowed_domains = ['gxmuseum.cn']
    start_urls = ['http://www.gxmuseum.cn/a/exhibition/11/index.html']

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
            "/html/body/div/div[2]/div[2]/div[2]/div")
        print(len(li_list))
        for li in li_list:
            item = ExhibitionItem()
            item["museumID"] = 155
            item["museumName"] = "广西壮族自治区博物馆"
            item["exhibitionImageLink"] ='http://www.gxmuseum.cn'+str(li.xpath(
                "./div[1]/a/img/@src").extract_first())
            item["exhibitionName"] = StrFilter.filter_2(li.xpath("./div[2]/p[1]/a/text()").extract_first())
            item["exhibitionTime"] = None
            item['exhibitionIntroduction'] = StrFilter.filter_2(li.xpath("./div[2]/p[1]/a/text()").extract_first())
            print(item)
            yield item
