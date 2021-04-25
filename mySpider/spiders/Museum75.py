#lay
from ..items import *


class Museum75(scrapy.Spider):
    name = "Museum75"
    allowed_domains = ['westlakemuseum.com']
    start_urls = ['http://www.westlakemuseum.com/index.php/bwggk/bwgjj']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.MuseumPipeLine': 300,
        }
    }

    def parse(self, response, **kwargs):
        item = MuseumBasicInformationItem()
        item["museumID"] = 75
        item["museumName"] = "杭州西湖博物馆总馆"
        item["address"] = "杭州市南山路89号"
        # str(response.xpath(
        # "/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[1]/dd[3]/text()").extract_first()).replace("\n", "")
        item["openingTime"] = "开放时间 8:00-17:00，全年开放"
        # str(response.xpath(
        # "/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[2]/dd[3]/text()").extract_first()).replace("\n", "")
        item["consultationTelephone"] = "87882333"
        item["publicityVideoLink"] = None
        item["longitude"] = "120.164279"
        item["latitude"] = "30.248032"
        item["introduction"] = response.xpath(
            '//*[@id="main"]/div[2]/div[2]/table[2]/tbody/tr/td[1]/text()[1]').extract()
        # str(response.xpath("/html/body/div[3]/div[2]/div/div[1]/div[4]/div[2]").xpath(
        # "string(.)").extract_first()).split("\n")[0]
        print(item)
        yield item
