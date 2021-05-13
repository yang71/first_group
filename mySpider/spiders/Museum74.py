#lay
from ..items import *


class Museum74(scrapy.Spider):
    name = "Museum74"
    allowed_domains = ['wzmuseum.cn']
    start_urls = ['http://www.wzmuseum.cn/Col/Col7/Index.aspx']

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
        item["museumID"] = 74
        item["museumName"] = "温州博物馆"
        item["address"] = "浙江省温州市市府路"
        # str(response.xpath(
        # "/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[1]/dd[3]/text()").extract_first()).replace("\n", "")
        item["openingTime"] = "09:00—17:00(16:00停止入馆，周一闭馆)"
        # str(response.xpath(
        # "/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[2]/dd[3]/text()").extract_first()).replace("\n", "")
        item["consultationTelephone"] = "0577-56988280"
        item["publicityVideoLink"] = None
        item["longitude"] = "120.704546"
        item["latitude"] = "27.994791"
        item["introduction"] = "温州博物馆是一所综合性地方博物馆，创建于1958年，原址在江心屿。2003年，位于世纪广场西侧的新馆落成并正式对外开放。"
        # str(response.xpath("/html/body/div[3]/div[2]/div/div[1]/div[4]/div[2]").xpath(
        # "string(.)").extract_first()).split("\n")[0]
        print(item)
        yield item
