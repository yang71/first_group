#lay
from ..items import *


class Museum70(scrapy.Spider):
    name = "Museum70"
    allowed_domains = ['baike.baidu.com']
    start_urls = ['https://baike.baidu.com/item/%E6%B5%99%E6%B1%9F%E8%87%AA%E7%84%B6%E5%8D%9A%E7%89%A9%E9%99%A2/22857955?fr=aladdin#10_2']

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
        item["museumID"] = 70
        item["museumName"] = "浙江自然博物院"
        item["address"] = "浙江省杭州市中心西湖文化广场6号"
        # str(response.xpath(
        # "/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[1]/dd[3]/text()").extract_first()).replace("\n", "")
        item["openingTime"] = "周二至周日，周一休馆（国定假日除外）。参观入场时间9:30-16:00"
        # str(response.xpath(
        # "/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[2]/dd[3]/text()").extract_first()).replace("\n", "")
        item["consultationTelephone"] = "0571-88212712"
        item["publicityVideoLink"] = None
        item["longitude"] = "119.65195"
        item["latitude"] = "30.677003"
        item["introduction"] = response.xpath(
            '/html/body/div[3]/div[2]/div/div[1]/div[4]/div[2]/text()[1]').extract()
        # str(response.xpath("/html/body/div[3]/div[2]/div/div[1]/div[4]/div[2]").xpath(
        # "string(.)").extract_first()).split("\n")[0]
        print(item)
        yield item
