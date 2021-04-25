#lay
from ..items import *


class Museum76(scrapy.Spider):
    name = "Museum76"
    allowed_domains = ['teamuseum.cn']
    start_urls = ['http://www.teamuseum.cn/index.htm']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.MuseumPipeLine': 300,
        }
    }

    def parse(self, response, **kwargs):
        item = MuseumBasicInformationItem()
        item["museumID"] = 76
        item["museumName"] = "中国茶叶博物馆"
        item["address"] = "杭州市龙井路88号、杭州市翁家山268号"
        # str(response.xpath(
        # "/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[1]/dd[3]/text()").extract_first()).replace("\n", "")
        item["openingTime"] = "开放时间19：00-16：30,每周一为闭馆日，节假日时间照常开放"
        # str(response.xpath(
        # "/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[2]/dd[3]/text()").extract_first()).replace("\n", "")
        item["consultationTelephone"] = "0571-87964221"
        item["publicityVideoLink"] = None
        item["longitude"] = "120.127463"
        item["latitude"] = "30.238608"
        item["introduction"] = "中国茶叶博物馆位于杭州，是我国唯一以茶和茶文化为主题的国家级专题博物馆。目前，中国茶叶博物馆分为两个馆区，双峰馆区位于龙井路88号，占地4.7公顷，1991年4月对外开放；龙井馆区位于翁家山268号，占地7.7公顷，2015年5月对外开放。两馆建筑面积共约1.3万平方米，集文化展示、科普宣传、科学研究、学术交流、茶艺培训、互动体验及品茗、餐饮、会务、休闲等服务功能于一体，是中国与世界茶文化的展示交流中心，也是茶文化主题旅游综合体。"
        # str(response.xpath("/html/body/div[3]/div[2]/div/div[1]/div[4]/div[2]").xpath(
        # "string(.)").extract_first()).split("\n")[0]
        yield item
