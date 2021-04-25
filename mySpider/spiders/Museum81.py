#lay
from ..items import *


class Museum81(scrapy.Spider):
    name = "Museum81"
    allowed_domains = ['zsbwg.com']
    start_urls = ['http://www.zsbwg.com/#/lindaojieshao/lindaojieshao2/:id?orderId=1&bool=true']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.MuseumPipeLine': 300,
        }
    }

    def parse(self, response, **kwargs):
        item = MuseumBasicInformationItem()
        item["museumID"] = 81
        item["museumName"] = "舟山博物馆"
        item["address"] = "舟山海洋文化艺术中心"
        # str(response.xpath(
        # "/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[1]/dd[3]/text()").extract_first()).replace("\n", "")
        item["openingTime"] = "9:00-17:00（16:00以后停止入馆），周一闭馆，国家法定节假日除外"
        # str(response.xpath(
        # "/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[2]/dd[3]/text()").extract_first()).replace("\n", "")
        item["consultationTelephone"] = "0580-8230565"
        item["publicityVideoLink"] = None
        item["longitude"] = "122.21064"
        item["latitude"] = "29.988599"
        item["introduction"] = "舟山博物馆是市级综合性博物馆，属国家所有社会公益性事业单位，成立于上世纪50年代后期，后因文革开始停办。1984年8月再次筹建舟山博物馆，把祖印寺作为博物馆馆舍，1986年10月开馆。90年代初为落实宗教政策把祖印寺归还佛协，舟山博物馆闭馆。1995年，舟山博物馆再次开始筹建，1998年馆舍落成，2000年迁入定海环城南路，2000年1月对外开放，占地面积5552平方米，建筑面积3693平方米，其中展厅面积为1350平方米。"
        # str(response.xpath("/html/body/div[3]/div[2]/div/div[1]/div[4]/div[2]").xpath(
        # "string(.)").extract_first()).split("\n")[0]
        print(item)
        yield item
