from ..items import *
from ..str_filter import *

class Collection87(scrapy.Spider):
    name = "Collection87"
    allowed_domains = ['ahbbmuseum.com']
    start_urls = ['https://www.ahbbmuseum.com/?list_4/',
                  'https://www.ahbbmuseum.com/?list_4_2/',
                  'https://www.ahbbmuseum.com/?list_4_3/',
                  'https://www.ahbbmuseum.com/?list_4_15/',
                  'https://www.ahbbmuseum.com/?list_4_21/',
                  'https://www.ahbbmuseum.com/?list_4_35/',
                  'https://www.ahbbmuseum.com/?list_4_45/',
                  'https://www.ahbbmuseum.com/?list_4_60/']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        }
    }

    def parse(self, response, **kwargs):
            #/html/body/div[2]/div[2]/div/div/div[2]/ul/li[1]
        li_list = response.xpath("/html/body/div[2]/div[2]/div/div/div[2]/ul/li")
        for li in li_list:
            item = CollectionItem()
            item["museumID"] = 87
            item["museumName"] = "蚌埠市博物馆"


            # 注意是否为全路径，一般后缀为@src有的是@oldsrc
            #/html/body/div[2]/div[2]/div/div/div[2]/ul/li[1]/a/div[1]/img
            #https://www.ahbbmuseum.com/static/upload/image/20210205/1612490736211016.jpg
            item['collectionImageLink'] = "https://www.ahbbmuseum.com/" + li.xpath("./a/div[1]/img/@src").extract_first()


            #注意是否是全路径
            #怎么判断是否是全路径
            #https://www.ahbbmuseum.com/?list_19/1180.html
            #/html/body/div[2]/div[2]/div/div/div[2]/ul/li[1]/a
            url = "https://www.ahbbmuseum.com/" + str(li.xpath("./a/@href").extract_first())

            yield scrapy.Request(
                url,
                callback=self.parseAnotherPage,
                meta={"item": item}
            )
    # 翻页
    def parseAnotherPage(self, response):
        r = re.compile(u"\\n|\\r|\\[.*?]|\\t")
        item = response.meta["item"]

        # 名字的xpath都一样
        # /html/body/div[6]/div/ul/li[1]/div/span[1]
        r = re.compile(u"\\n|\\r|\\[.*?]|\\t")
        item['collectionName'] = response.xpath("/html/body/div[2]/div[2]/div/div/h1/text()").extract_first()
        item["collectionName"] = "".join(item["collectionName"].split())
        item["collectionName"] = re.sub(r, '', item["collectionName"])

        item["collectionIntroduction"] = response.xpath(
            'normalize-space(/html/body/div[2]/div[2]/div/div/div[2]/div[2]/p[4])').extract_first()
        item["collectionIntroduction"] = StrFilter.filter_2(item["collectionIntroduction"])

        str2 = response.xpath(
            'normalize-space(/html/body/div[2]/div[2]/div/div/div[2]/div[2]/p[6])').extract_first()
        str2 = StrFilter.filter_2(str2)

        str3 = response.xpath(
            'normalize-space(/html/body/div[2]/div[2]/div/div/div[2]/div[2]/p[8])').extract_first()
        str3 = StrFilter.filter_2(str3)
        item["collectionIntroduction"] = item["collectionIntroduction"] + str2 + str3
        print(item)
        yield item
