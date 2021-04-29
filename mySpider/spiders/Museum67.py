#lay
from ..items import *


class Museum67(scrapy.Spider):
    name = "Museum67"
    allowed_domains = ['csmuseum.cn']
    start_urls = ['http://www.csmuseum.cn/#/info/index/1']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.MuseumPipeLine': 300,
        }
    }

    def parse(self, response, **kwargs):
        item = MuseumBasicInformationItem()
        item["museumID"] = 67
        item["museumName"] = "常熟博物馆"
        item["address"] = "江苏省常熟市北门大街1号"
        # str(response.xpath(
        # "/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[1]/dd[3]/text()").extract_first()).replace("\n", "")
        item["openingTime"] = "每星期二至星期日9:00-16:30（16:00以后停止入场），每星期一闭馆（国家法定节假日除外）"
        # str(response.xpath(
        # "/html/body/div[3]/div[2]/div/div[1]/div[7]/dl[2]/dd[3]/text()").extract_first()).replace("\n", "")
        item["consultationTelephone"] = "0512-52776855"
        item["publicityVideoLink"] = None
        item["longitude"] = "120.746936"
        item["latitude"] = "31.65304"
        item["introduction"] = "常熟博物馆于1997年9月28日对外开放，为省级爱国主义教育基地，曾获“江苏省优秀博物馆”等荣誉。虞山派古琴艺术馆和王石谷纪念馆为下辖的两个分馆。2005年被国家文物局列为全国六家“博物馆展示•服务提升项目”试点单位之一；2009年扩建改造，获评国家二级博物馆；2020年12月获评国家一级博物馆。馆内设有馆藏玉器、瓷器、书画、文玩等固定展览，并设有临时展厅，每年举办各类展览30次左右。近年来，常熟博物馆致力于打造精品展览，展览多次入选江苏省文物局文物巡回展项目，还先后在北京、上海、西安、广州、东莞、深圳、福州、青岛、银川、贵阳、南京等城市举办各类文物精品展览，尤其是2016年“两朝帝师翁同龢及翁氏家族文物特展”在北京颐和园等四馆巡展、2017年“山水清晖——虞山画派精品特展”暨虞山画派艺术国际学术研讨会、2018年“万里江海通——江南与海上丝绸之路特展”等获得较大的社会反响。"
        print(item)
        yield item
