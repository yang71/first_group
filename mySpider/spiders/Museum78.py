#lay
from ..items import *


class Museum78(scrapy.Spider):
    name = "Museum78"
    allowed_domains = ['tianyige.com.cn']
    start_urls = ['http://www.tianyige.com.cn/survey#introduction']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.MuseumPipeLine': 300,
        }
    }

    def parse(self, response, **kwargs):
        item = MuseumBasicInformationItem()
        item["museumID"] = 78
        item["museumName"] = "宁波市天一阁博物馆"
        item["address"] = "宁波市海曙区天一街10号"
        # str(response.xpath(
        # "/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[1]/dd[3]/text()").extract_first()).replace("\n", "")
        item["openingTime"] = "5月1日-10月31日,8:30 - 17:30,11月1日-4月30日,8:30 - 17:00,每周一上午闭馆（法定节假日除外，下午1:30开馆）。"
        # str(response.xpath(
        # "/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[2]/dd[3]/text()").extract_first()).replace("\n", "")
        item["consultationTelephone"] = "0574-87293029"
        item["publicityVideoLink"] = None
        item["longitude"] = "121.545818"
        item["latitude"] = "29.876464"
        item["introduction"] = "宁波市天一阁博物馆，国家二级博物馆，位于浙江省宁波市海曙区天一街10号。是一个以藏书文化为核心，集藏书的研究、保护、管理、陈列、社会教育、旅游观光于一体的专题性博物馆。占地面积约为34000平方米， [1]  分藏书文化区、园林休闲区、陈列展览区。"
        # str(response.xpath("/html/body/div[3]/div[2]/div/div[1]/div[4]/div[2]").xpath(
        # "string(.)").extract_first()).split("\n")[0]
        yield item
