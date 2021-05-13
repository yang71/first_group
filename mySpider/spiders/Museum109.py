#lay
from ..items import *


class Museum109(scrapy.Spider):
    name = "Museum109"
    allowed_domains = ['ytmuseum.com']
    start_urls = ['http://www.ytmuseum.com/article']

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
        item["museumID"] = 109
        item["museumName"] = "潍坊市博物馆"
        item["address"] = "山东省潍坊市奎文区东风东街6616号"
        # str(response.xpath(
        # "/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[1]/dd[3]/text()").extract_first()).replace("\n", "")
        item["openingTime"] = "周二至周日,09:00-16:30"

        # str(response.xpath(
        # "/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[2]/dd[3]/text()").extract_first()).replace("\n", "")
        item["consultationTelephone"] = "(0536)8865529"
        item["publicityVideoLink"] = None
        item["longitude"] = "119.168378"
        item["latitude"] = "36.712652"
        item["introduction"] = "潍坊市博物馆始建于1962年，由山东省潍坊市人民政府委员会批准成立。新馆于1999年建成，占地面积24053.5㎡，建筑面积18669.7㎡；2007年11月，单位类别划为公益一类事业单位；2016年科室调整为办公室、财务科、宣教科、陈列科、保管科、文保科、考古科、物管科、保卫科等9个正科级科室，核定编制人员56人，其中馆长1名，党支部书记1名，副馆长2名。专业技术职称方面，研究馆员5人，副研究馆员5人，馆员26人，助理馆员10人，专业技术人员占在编人数的90%。"
        print(item)
        yield item
