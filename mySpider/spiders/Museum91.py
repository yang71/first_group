#lay
from ..items import *


class Museum91(scrapy.Spider):
    name = "Museum91"
    allowed_domains = ['mtybwg.org.cn']
    start_urls = ['http://www.mtybwg.org.cn/about/924.aspx']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.MuseumPipeLine': 300,
        }
    }

    def parse(self, response, **kwargs):
        item = MuseumBasicInformationItem()
        item["museumID"] = 91
        item["museumName"] = "中国闽台缘博物馆"
        item["address"] = "福建泉州北清东路212号"
        # str(response.xpath(
        # "/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[1]/dd[3]/text()").extract_first()).replace("\n", "")
        item["openingTime"] = "周一闭馆，开放时间：9:00-17:00（16:30起停止入场)"
        # str(response.xpath(
        # "/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[2]/dd[3]/text()").extract_first()).replace("\n", "")
        item["consultationTelephone"] = "0595-22751800"
        item["publicityVideoLink"] = None
        item["longitude"] = "118.596435"
        item["latitude"] = "24.941018"
        item["introduction"] = "中国闽台缘博物馆是反映祖国大陆（福建）与宝岛台湾历史关系的国家级专题博物馆，座落于中国历史文化名城泉州市区西北侧，北倚国家级风景区清源山，南接风景秀丽的西湖之畔"
        print(item)
        yield item
