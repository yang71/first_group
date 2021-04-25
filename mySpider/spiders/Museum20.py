import scrapy as scrapy

from ..items import *

class Museum20(scrapy.Spider):
    name = "Museum20"
    allowed_domains = ['mzhoudeng.com']
    start_urls = ['http://mzhoudeng.com/about.aspx?cateid=138']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.MuseumPipeLine': 300,
        }
    }
    # 需要重写的部分
    def parse(self, response, **kwargs):
        item = MuseumBasicInformationItem()
        item["museumID"] = 20
        item["museumName"] = response.xpath('/html/head/title').xpath("string(.)").extract_first()
        item["address"] = "天津市南开区水上公园西路9号"
        item["openingTime"] = response.xpath("/html/body/div[3]/div/div[1]/div[2]/div[2]/p[2]/span/text()").extract_first()
        item["consultationTelephone"] = "022-23592257"
        item["introduction"] = "周恩来邓颖超纪念馆坐落在风光旖旎、景色怡人的水上公园风景区，占地70000平方米，建筑面积13000平方米，建于1998年2月28日周恩来诞辰百年纪念日前夕。馆内藏品丰富，文物价值弥足珍贵。纪念馆基本陈列分为三大展区即主展厅、按1:1比例仿建的北京中南海西花厅专题陈列厅和专机陈列厅。主展厅内有：周恩来生平展“人民总理周恩来”、邓颖超专题展“邓颖超——20世纪中国妇女运动的先驱”；西花厅专题陈列厅设有复原陈列和主题文物展“伟大的情怀”；专机陈列厅陈列着苏联政府赠送给周恩来总理的伊尔—14型678号专机，现为国家二级文物。纪念馆的展览主题突出，天津地域特色鲜明，生动再现了周恩来、邓颖超两位伟人光辉灿烂的一生以及为祖国、为人民鞠躬尽瘁的优秀品质和崇高精神。周恩来邓颖超纪念馆现为全国爱国主义教育示范基地、全国廉政教育基地和国家一级博物馆。"
        item["publicityVideoLink"] = None
        item["longitude"] = "116.4038"
        item["latitude"] = "39.9148"
        # print(item)
        yield item
