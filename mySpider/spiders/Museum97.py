#lay
from ..items import *


class Museum97(scrapy.Spider):
    name = "Museum97"
    allowed_domains = ['aymuseum.com']
    start_urls = ['http://www.aymuseum.com/nd.jsp?id=51#_jcp=1&_np=101_0']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.MuseumPipeLine': 300,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.DefaultMiddleware': 0,
        },
    }

    def parse(self, response, **kwargs):
        item = MuseumBasicInformationItem()
        item["museumID"] = 97
        item["museumName"] = "安源路矿工人运动纪念馆"
        item["address"] = "江西省萍乡市安源区正街路"
        # str(response.xpath(
        # "/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[1]/dd[3]/text()").extract_first()).replace("\n", "")
        item["openingTime"] = "10月1日-4月30日周二至周日09:00-16:20,5月1日-9月30日周二至周日09:00-16:50"
        # str(response.xpath(
        # "/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[2]/dd[3]/text()").extract_first()).replace("\n", "")
        item["consultationTelephone"] = "(0799)7101123"
        item["publicityVideoLink"] = None
        item["longitude"] = "104.090883"
        item["latitude"] = "30.681497"
        item["introduction"] = response.xpath(
            '//*[@id="module12"]/div/div/div/div/div[2]/div/p[3]/span/text()').extract()

        print(item)
        yield item
