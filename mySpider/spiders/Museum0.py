from ..items import *


class Museum0(scrapy.Spider):
    name = "Museum0"
    allowed_domains = ['dpm.org.cn']
    start_urls = ['https://www.dpm.org.cn/Home.html']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.MuseumPipeLine': 300,
        }
    }

    def parse(self, response, **kwargs):
        item = MuseumBasicInformationItem()
        item["museumID"] = 0
        item["museumName"] = '故宫博物院'
        item["address"] = '北京市东城区景山前街4号'

        data = response.xpath("//div[@class='list']/ul/li[@class='transition translateX-100']/p/text()").extract()
        time = response.xpath("//div[@class='list']/ul/li[@class='transition translateX-100']/h1/text()").extract()
        # newdata = response.xpath( "//div[@class='list']/ul/li[@class='transition translateX-100 last']/p/text(
        # )").extract_first() newtime = response.xpath( "//div[@class='list']/ul/li[@class='transition translateX-100
        # last']/h1/text()").extract_first() opentime = data[0] + time[0] + "   " + data[1] + time[1] + "   " + data[
        # 2] + time[2] + "   " + newdata + newtime

        item["openingTime"] = "opentime"
        item["consultationTelephone"] = 'gugong@dpm.org.cn'
        item["introduction"] = response.xpath("//meta[@name='description']/@content").extract()
        item["publicityVideoLink"] = "https://img.dpm.org.cn/Uploads/video/8dazuo_hubiao.mp4"
        item["longitude"] = "116.403414"
        item["latitude"] = "39.924091"
        yield item
