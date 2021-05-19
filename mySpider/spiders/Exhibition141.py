#
from ..items import *
from ..str_filter import *

class Exhibition141(scrapy.Spider):
    name = "Exhibition141"
    allowed_domains = ['shaoqiguli.com']
    start_urls = ['http://www.shaoqiguli.com/Exhibition/tempexh']

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
            "/html/body/div[1]/div[3]/div/ul[2]/li")
        print(len(li_list))
        for li in li_list:
            item = ExhibitionItem()
            item["museumID"] = 141
            item["museumName"] = "刘少奇故居纪念馆"
            item["exhibitionImageLink"] = StrFilter.getDoamin(response) + li.xpath(
                "./a/div[2]/div").extract_first().replace('background-image: url("','').replace('");','')
            item["exhibitionName"] = StrFilter.filter_2(li.xpath("./a/div[1]/h3").extract_first())
            item["exhibitionTime"] = None
            item['exhibitionIntroduction'] = None
            print(item)
            #yield item
