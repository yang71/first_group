from ..items import *
from ..str_filter import *

class Exhibition45(scrapy.Spider):
    name = "Exhibition45"
    allowed_domains = ['aihuihistorymuseum.org.cn']
    start_urls = ['http://www.aihuihistorymuseum.org.cn/lpiclist.aspx?type=358']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.ExhibitionPipeLine': 302,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.DefaultMiddleware': 0,
        },
    }

    def parse(self, response, **kwargs):
            #/html/body/form/div[4]/div[1]/div[1]/div[2]/div[1]/div/ul/li[1]
        li_list = response.xpath("/html/body/form/div[4]/div[1]/div[1]/div[2]/div[1]/div/ul/li")
        # print(li_list)
        for li in li_list:
            item = ExhibitionItem()
            item["museumID"] = 45
            item["museumName"] = "爱辉历史陈列馆"

            # 名字的xpath都一样
            # /html/body/form/div[4]/div[1]/div[1]/div[2]/div[1]/div/ul/li[1]/a/div[2]
            item['exhibitionName'] = "临时展览"

            #/html/body/form/div[4]/div[1]/div[1]/div[2]/div[1]/div/ul/li[1]/a/div[1]/img
            #http://www.aihuihistorymuseum.org.cn/manager/Public/Newsfile/202105041021418bd0.jpg
            str1 = 'http://www.aihuihistorymuseum.org.cn/'
            str2 = str(li.xpath(
                "./a/div[1]/img/@src").extract_first())
            item["exhibitionImageLink"] = str1 + str2

            #/html/body/div[3]/div/div[1]/div/div[2]/div/div[1]/div[1]/div[2]/div[1]
            item["exhibitionTime"] = "不详"

            #http://www.aihuihistorymuseum.org.cn/jquetu.aspx?pid=386
            #/html/body/form/div[4]/div[1]/div[1]/div[2]/div[1]/div/ul/li[1]/a
            url = "http://www.aihuihistorymuseum.org.cn/" + str(li.xpath("./a/@href").extract_first())

            yield scrapy.Request(
                url,
                callback=self.parseAnotherPage,
                meta={"item": item}
            )

    def parseAnotherPage(self, response):
        item = response.meta["item"]

        #/html/body/form/div[4]/div[1]/div/div[2]/div[1]/span[2]
        item['exhibitionIntroduction'] = StrFilter.filter(
            response.xpath("/html/body/form/div[4]/div[1]/div/div[2]/div[1]/span[2]").xpath('string(.)').extract_first())
        print(item)
        yield item
