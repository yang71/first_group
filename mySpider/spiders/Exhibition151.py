#
from ..items import *
from ..str_filter import *

class Exhibition151(scrapy.Spider):
    name = "Exhibition151"
    allowed_domains = ['www.gzam.com.cn']
    start_urls = ['https://www.gzam.com.cn/zzzc/info_18.aspx?itemid=36864&State=0']

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
            "/html/body/div/div[1]/div[1]/section/section/div[2]/article/div")
        print(len(li_list))
        for li in li_list:
            item = ExhibitionItem()
            item["museumID"] = 151
            item["museumName"] = "广州艺术博物院"
            item["exhibitionImageLink"] ='https://www.gzam.com.cn'+str(li.xpath(
                "/html/body/div/div[1]/div[1]/aside/div[1]/ul/li[1]/a/img/@src").extract_first())
            item["exhibitionName"] = StrFilter.filter_2(li.xpath("./h3/text()").extract_first())
            item["exhibitionTime"] = None
            item['exhibitionIntroduction'] = StrFilter.filter_2(li.xpath("./article[2]/div[1]/section[2]/p[4]/span/text()").extract_first())
            print(item)
            yield item
