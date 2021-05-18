#lay
from ..items import *


class Museum104(scrapy.Spider):
    name = "Museum104"
    allowed_domains = ['pxmuseum.com']
    start_urls = ['http://www.pxmuseum.com/nd.jsp?id=116#_jcp=1']

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
        item["museumID"] = 104
        item["museumName"] = "青岛市博物馆"
        item["address"] = "青岛市崂山区梅岭东路51号"
        # str(response.xpath(
        # "/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[1]/dd[3]/text()").extract_first()).replace("\n", "")
        item["openingTime"] = "5月至11月 周二至周日 09:00-17:00;11月至5月 周二至周日 09:00-16:30"
        # str(response.xpath(
        # "/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[2]/dd[3]/text()").extract_first()).replace("\n", "")
        item["consultationTelephone"] = "(0532)88896286"
        item["publicityVideoLink"] = None
        item["longitude"] = "120.389455"
        item["latitude"] = "36.072227"
        item["introduction"] = "青岛市博物馆是国家一级博物馆和全国古籍重点保护单位，馆藏文物包括书法、绘画、陶瓷器、铜器、玉器、钱币、玺印、甲骨、竹木牙角器等三十余个门类十多万件，其中书法、陶瓷器、玉器、钱币为馆藏特色。馆内还收藏有4万余件青岛历史发展各阶段留下来的文物资料，反映了青岛建置以来城市的发展，是全面了解青岛历史的重要场所。"
        print(item)
        yield item
