import scrapy as scrapy

from ..items import *

class Museum24(scrapy.Spider):
    name = "Museum24"
    allowed_domains = ['hdmuseum.org']
    start_urls = ['https://www.hdmuseum.org/']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.MuseumPipeLine': 300,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.DefaultMiddleware': 0,
        },
    }
    # 需要重写的部分
    def parse(self, response, **kwargs):
        item = MuseumBasicInformationItem()
        item["museumID"] = 24
        item["museumName"] = response.xpath('/html/head/title').xpath("string(.)").extract_first()
        item["address"] = response.xpath('/html/body/div[1]/div/footer/div/div[2]/div/div[3]').extract_first()
        item["openingTime"] = response.xpath("/html/body/div[1]/div/section[5]/div/div/div[2]/div/div[2]/div[2]").xpath("string(.)").extract_first()
        item["consultationTelephone"] = "0310--3012739"
        item["introduction"] = "邯郸市博物馆现为国家一级博物馆、河北省爱国主义教育基地、第一批河北省社会科学普及基地和河北省志愿者实践基地。邯郸市博物馆成立于1984年，前身为成立于1968年的“毛泽东思想胜利万岁邯郸展览馆”。"
        item["publicityVideoLink"] = None
        item["longitude"] = "114.5308"
        item["latitude"] = "36.6154"
        print(item)
        yield item
