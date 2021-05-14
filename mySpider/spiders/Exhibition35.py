from ..items import *
from ..str_filter import *

class Exhibition35(scrapy.Spider):
    name = "Exhibition35"
    allowed_domains = ['918museum.org.cn']
    start_urls = ['http://www.918museum.org.cn/index.php/article/listarticle/pid/118/rel/media/sidebar/sidebar']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.ExhibitionPipeLine': 302,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.DefaultMiddleware': 0,
        },
    }


    def parse(self, response, **kwargs):
            # /html/body/div[3]/div/div/div[1]/div/div[2]/div/ul[1]
        li_list = response.xpath("/html/body/div[3]/div/div/div[1]/div/div[2]/div/ul")
        # print(li_list)
        for ul in li_list:
            item = ExhibitionItem()
            item["museumID"] = 35
            item["museumName"] = "九·一八”历史博物馆"

            # 名字的xpath都一样
            # /html/body/div[3]/div/div/div[1]/div/div[2]/div/ul[1]/a/li/div/span
            item['exhibitionName'] = ul.xpath("./a/li/div/span/text()").extract_first()

            #/html/body/div[3]/div/div/div[1]/div/div[2]/div/ul[1]/a/li/img
            #http://www.918museum.org.cn/public/uploads/images/2019/05/17/th_20190517163820450w.jpg
            item["exhibitionImageLink"] = "http://www.918museum.org.cn/" + str(ul.xpath(
                "./a/li/img/@src").extract_first())

            item["exhibitionTime"] = '见exhibitionIntroduction'

            #/html/body/div[3]/div/div/div[1]/div/div[2]/div/ul[1]/a
            #http://www.918museum.org.cn/index.php/article/detail/uuid/28f1e509-3785-4890-9137-2b6553929c85/sidebar/sidebar
            url = "http://www.918museum.org.cn/" + str(ul.xpath("./a/@href").extract_first())

            yield scrapy.Request(
                url,
                callback=self.parseAnotherPage,
                meta={"item": item}
            )

    def parseAnotherPage(self, response):
        item = response.meta["item"]
        #/html/body/div[3]/div/div/div[1]/div/div[2]/div/div[1]/div[2]/div[3]
        item['exhibitionIntroduction'] = StrFilter.filter_2(
            response.xpath("/html/body/div[3]/div/div/div[1]/div/div[2]/div/div[1]/div[2]/div[3]").xpath('string(.)').extract_first())
        print(item)
        yield item
