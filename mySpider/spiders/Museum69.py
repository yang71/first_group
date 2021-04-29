#lay
from ..items import *


class Museum69(scrapy.Spider):
    name = "Museum69"
    allowed_domains = ['zhejiangmuseum.com']
    start_urls = ['http://www.zhejiangmuseum.com/Survey/Introduction']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.MuseumPipeLine': 300,
        }
    }

    def parse(self, response, **kwargs):
        item = MuseumBasicInformationItem()
        item["museumID"] = 69
        item["museumName"] = "浙江省博物馆"
        item["address"] = "浙江省杭州市孤山路25号"
        # str(response.xpath(
        # "/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[1]/dd[3]/text()").extract_first()).replace("\n", "")
        item["openingTime"] = "周一闭馆，法定节假日除外，周二至周日9:00 - 17:00，16:30观众停止入场，16:50开始清场。"
        # str(response.xpath(
        # "/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[2]/dd[3]/text()").extract_first()).replace("\n", "")
        item["consultationTelephone"] = "0571-86013085"
        item["publicityVideoLink"] = None
        item["longitude"] = "120.149943"
        item["latitude"] = "30.257342"
        item["introduction"] ="浙江省博物馆始建于1929年，缘起于首届杭州西湖博览会，初名“浙江省西湖博物馆”，1976年更名为“浙江省博物馆”。2006年，浙江革命历史纪念馆归并浙江省博物馆管理。2009年武林馆区（包括浙江革命历史纪念馆）建成对外开放。经过九十余年的发展，浙江省博物馆（浙江革命历史纪念馆）已成为浙江省内规模最大的综合性人文科学博物馆，形成了包括孤山馆区、武林馆区、沙孟海旧居、黄宾虹纪念室、古荡文物保护科研基地等在内的集收藏、研究、保护、展示和教育等多功能、广范围的新格局。"


        print(item)
        yield item
