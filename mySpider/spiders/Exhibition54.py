from ..items import *
from ..str_filter import *

class Exhibition54(scrapy.Spider):
    name = "Exhibition54"
    allowed_domains = ['shmmc.com.cn']
    start_urls = ['https://www.shmmc.com.cn/Home/ZxzlList']

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
        item["museumID"] = 54
        item["museumName"] = "上海中国航海博物馆"

        # 名字的xpath都一样
        #/html/body/div[2]/div[2]/div/div[2]/div[2]/div/div[1]/div[2]/div[1]/a
        item['exhibitionName'] = StrFilter.filter(
            response.xpath("/html/body/div[2]/div[2]/div/div[2]/div[2]/div/div[1]/div[2]/div[1]/a").xpath('string(.)').extract_first())

        #/html/body/div[2]/div[2]/div/div[2]/div[2]/div/div[1]/div[1]/a/img
        #https://www.shmmc.com.cn/mup/image/20201217090232_2024.jpg
        str1 = 'https://www.shmmc.com.cn/'
        str2 = str(response.xpath(
                "/html/body/div[2]/div[2]/div/div[2]/div[2]/div/div[1]/div[1]/a/img/@src").extract_first())
        item["exhibitionImageLink"] = str1 + str2

        #/html/body/div[2]/div[2]/div/div[2]/div[2]/div/div[1]/div[2]/div[2]
        item["exhibitionTime"] = StrFilter.filter(
            response.xpath("/html/body/div[2]/div[2]/div/div[2]/div[2]/div/div[1]/div[2]/div[2]").xpath('string(.)').extract_first())

        #/html/body/div[2]/div[2]/div/div[2]/div[2]/div/div[1]/div[2]/div[4]
        item['exhibitionIntroduction'] = StrFilter.filter(
            response.xpath("/html/body/div[2]/div[2]/div/div[2]/div[2]/div/div[1]/div[2]/div[4]").xpath('string(.)').extract_first())
        print(item)
        yield item