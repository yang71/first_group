from ..items import *
from ..str_filter import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options  # 使用无头浏览器

# 无头浏览器设置
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")

class Collection76(scrapy.Spider):
    name = "Collection76"
    allowed_domains = ['teamuseum.cn']
    start_urls = ['http://www.teamuseum.cn/news/holding.htm?newsType=5',
                  'http://www.teamuseum.cn/news/holding.htm?newsType=6',
                  'http://www.teamuseum.cn/news/holding.htm?newsType=7',
                  'http://www.teamuseum.cn/news/holding.htm?newsType=8',
                  'http://www.teamuseum.cn/news/holding.htm?newsType=9',
                  'http://www.teamuseum.cn/news/holding.htm?newsType=10']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        }
    }

    # 实例化一个浏览器对象
    def __init__(self):
        self.browser = webdriver.Chrome(chrome_options=chrome_options)
        super().__init__()

    # 整个爬虫结束后关闭浏览器
    def close(self, spider):
        self.browser.quit()

    def parse(self, response, **kwargs):
            #/html/body/div[4]/div[2]/div/div/div[4]/ul/div[1]/li[1]
        li_list = response.xpath("/html/body/div[4]/div[2]/div/div/div[4]/ul/div[1]/li")
        #print(li_list)
        for li in li_list:
            item = CollectionItem()
            item["museumID"] = 76
            item["museumName"] = "中国茶叶博物馆"

            # 名字的xpath都一样
            #/html/body/div[4]/div[2]/div/div/div[4]/ul/div[1]/li[1]/a/h2
            r = re.compile(u"\\n|\\r|\\[.*?]|\\t")
            item['collectionName'] = li.xpath("./a/h2/text()").extract_first()
            item["collectionName"] = "".join(item["collectionName"].split())
            item["collectionName"] = re.sub(r, '', item["collectionName"])

            # 注意是否为全路径，一般后缀为@src有的是@oldsrc
            #/html/body/div[4]/div[2]/div/div/div[4]/ul/div[1]/li[1]/a/img
            item['collectionImageLink'] = li.xpath("./a/img/@src").extract_first()


            #注意是否是全路径
            #怎么判断是否是全路径
            #http://www.teamuseum.cn/news/holding-detail.htm?id=471
            #/html/body/div[4]/div[2]/div/div/div[4]/ul/div[1]/li[1]/a
            url = "http://www.teamuseum.cn/" + str(li.xpath("./a/@href").extract_first())

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
            'normalize-space(/html/body/div[4]/div[2]/div/div[2]/div/div[3])').extract_first()

        item["collectionIntroduction"] = "".join(item["collectionIntroduction"].split())
        item["collectionIntroduction"] = re.sub(r, '', item["collectionIntroduction"])
        print(item)
        yield item
