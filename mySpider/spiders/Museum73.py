#lay
from ..items import *


class Museum73(scrapy.Spider):
    name = "Museum73"
    allowed_domains = ['hzmuseum.com']
    start_urls = ['http://hzmuseum.com/#/hangbojianjie']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.MuseumPipeLine': 300,
        }
    }

    def parse(self, response, **kwargs):
        item = MuseumBasicInformationItem()
        item["museumID"] = 73
        item["museumName"] = "杭州博物馆"
        item["address"] = "杭州粮道山18号"
        # str(response.xpath(
        # "/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[1]/dd[3]/text()").extract_first()).replace("\n", "")
        item["openingTime"] = "周一闭馆（法定节假日除外），周二至周日开放时间：9:00--16:30"
        # str(response.xpath(
        # "/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[2]/dd[3]/text()").extract_first()).replace("\n", "")
        item["consultationTelephone"] = "0571-87802660"
        item["publicityVideoLink"] = None
        item["longitude"] = "120.173093"
        item["latitude"] = "30.244426"
        item["introduction"] = "杭州博物馆是一座展现杭州历史变迁和城市文物珍藏的人文类综合性博物馆，是浙江省最具影响力的博物馆之一，也是杭州市博物馆群体中馆藏、展陈和文化活动水平位居前列的骨干博物馆。场馆前身为2001年10月开放的杭州历史博物馆，经过多年积累与发展，已成为文物丰富、区位便捷、展览精美、设施优良的杭州历史文化亮丽窗口。"
        # str(response.xpath("/html/body/div[3]/div[2]/div/div[1]/div[4]/div[2]").xpath(
        # "string(.)").extract_first()).split("\n")[0]
        print(item)
        yield item
