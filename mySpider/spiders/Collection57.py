from ..items import *
from ..str_filter import *

class Collection57(scrapy.Spider):
    name = "Collection57"
    allowed_domains = ['19371213.com.cn']
    start_urls = ['http://www.19371213.com.cn/collection/featured/']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        }
    }

    def parse(self, response, **kwargs):
        #/html/body/div[6]/div/div/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]
        li_list = response.xpath("/html/body/div[6]/div/div/div/div[2]/div[2]/div/div/div[1]/div/div/div")
        for div in li_list:
            item = CollectionItem()
            item["museumID"] = 57
            item["museumName"] = "侵华日军南京大屠杀遇难同胞纪念馆"

            # 名字的xpath都一样
            #/html/body/div[6]/div/div/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]
            #/html/body/div[6]/div/div/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/section/div[2]/h3/a
            item['collectionName'] = div.xpath("./section/div[2]/h3/a/text()").extract_first()
            #print(div.xpath("./section/div[2]/h3/a/text()"))

            # 注意是否为全路径，一般后缀为@src有的是@oldsrc
            #/html/body/div[6]/div/div/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/section/div[1]/div/a/img
            #/html/body/div[6]/div/div/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]
            #http://www.19371213.com.cn/collection/zdwwjs/201811/W020190408520034958829.jpg
            tt = div.xpath("./section/div[1]/div/a/img/@src").extract_first()
            item['collectionImageLink'] = "http://www.19371213.com.cn/collection/" + tt[2:]
            #print(div.xpath("./section/div[1]/div/a/img/@src"))

            #注意是否是全路径
            #怎么判断是否是全路径
            #http://www.19371213.com.cn/collection/zdwwjs/201811/t20181113_2232506.html
            #/html/body/div[6]/div/div/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/section/div[1]/div/a
            url = str(div.xpath("./section/div[1]/div/a/@href").extract_first())
            url = "http://www.19371213.com.cn/collection/" + url[2:]
            #print(url)

            yield scrapy.Request(
                url,
                callback=self.parseAnotherPage,
                meta={"item": item}
            )
    # 翻页
    def parseAnotherPage(self, response):
        r = re.compile(u"\\n|\\r|\\[.*?]|\\t")
        item = response.meta["item"]

        item["collectionIntroduction"] = response.xpath(
            'normalize-space(/html/body/div[6]/div/div/div/div[2]/div/div/article/section/div[2]/div/div/div/div/p[2])').extract_first()

        item["collectionIntroduction"] = "".join(item["collectionIntroduction"].split())
        item["collectionIntroduction"] = re.sub(r, '', item["collectionIntroduction"])
        print(item)
        yield item
