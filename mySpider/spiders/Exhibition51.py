from ..items import *
from ..str_filter import *

class Exhibition51(scrapy.Spider):
    name = "Exhibition51"
    allowed_domains = ['zgyd1921.com']
    start_urls = ['http://www.zgyd1921.com/zgyd/node3/n11/n15/index.html']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.ExhibitionPipeLine': 302,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.DefaultMiddleware': 0,
        },
    }

    def parse(self, response, **kwargs):
            #/html/body/div[5]/ul/li[1]
        li_list = response.xpath("/html/body/div[5]/ul/li")
        # print(li_list)
        for li in li_list:
            item = ExhibitionItem()
            item["museumID"] = 51
            item["museumName"] = "中国共产党第一次全国代表大会会址纪念馆"

            # 名字的xpath都一样
            # /html/body/div[5]/ul/li[1]/div/p[1]/a
            item['exhibitionName'] = StrFilter.filter(
                li.xpath("./div/p[1]/a").xpath('string(.)').extract_first())

            #/html/body/div[5]/ul/li[1]/a/img
            #http://www.zgyd1921.com/images/thumbnailimg/month_1709/201709280447548475.jpg
            str1 = 'http://www.zgyd1921.com/'
            str2 = str(li.xpath(
                "./a/img/@src").extract_first())
            item["exhibitionImageLink"] = str1 + str2

            # /html/body/div[3]/div[1]/p
            item["exhibitionTime"] = "临时展览"

            #/html/body/div[5]/ul/li[1]/div/p[2]
            item['exhibitionIntroduction'] = StrFilter.filter(
                li.xpath("./div/p[2]").xpath('string(.)').extract_first())
            print(item)
            yield item



