from ..items import *
from ..str_filter import *

class Exhibition43(scrapy.Spider):
    name = "Exhibition43"
    allowed_domains = ['sohu.com']
    start_urls = ['https://www.sohu.com/a/463689482_121107011']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.ExhibitionPipeLine': 302,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.DefaultMiddleware': 0,
        },
    }

    def parse(self, response, **kwargs):
        item = ExhibitionItem()
        item["museumID"] = 43
        item["museumName"] = "东北烈士纪念馆"

        item['exhibitionName'] = "黑土英魂——东北抗日战争和解放战争时期烈士事迹陈列"

        str2 = str(response.xpath(
                "/html/body/div[1]/div[2]/div[2]/div[1]/div/article/p[12]/img/@src").extract_first())
        item["exhibitionImageLink"] = str2

        item["exhibitionTime"] = "2021年5月1日至5日"

        item['exhibitionIntroduction'] = StrFilter.filter(
            response.xpath("/html/body/div[1]/div[2]/div[2]/div[1]/div/article/p[13]/span").xpath('string(.)').extract_first())
        print(item)
        yield item
