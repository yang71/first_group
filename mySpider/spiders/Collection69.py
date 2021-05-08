from ..items import *
from ..str_filter import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options # 使用无头浏览器

#无头浏览器设置
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")

class Collection69(scrapy.Spider):
    name = "Collection69"
    allowed_domains = ['zhejiangmuseum.com']
    start_urls = ['http://www.zhejiangmuseum.com/Collection/ExcellentCollection?page=1',
                  'http://www.zhejiangmuseum.com/Collection/ExcellentCollection?page=2',
                  'http://www.zhejiangmuseum.com/Collection/ExcellentCollection?page=3',]

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.Collection69Middleware': 2336,
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
            #/html/body/div[1]/div/div/div/div/main/ul/li[1]

        li_list = response.xpath("/html/body/div[1]/div/div/div/div/main/ul/li")
        for li in li_list:
            item = CollectionItem()
            item["museumID"] = 69
            item["museumName"] = "浙江省博物馆"

            # 名字的xpath都一样
            #/html/body/div[1]/div/div/div/div/main/ul/li[1]/a/h3
            r = re.compile(u"\\n|\\r|\\[.*?]|\\t")
            item['collectionName'] = li.xpath("./a/h3/text()").extract_first()
            item["collectionName"] = "".join(item["collectionName"].split())
            item["collectionName"] = re.sub(r, '', item["collectionName"])

            # 注意是否为全路径，一般后缀为@src有的是@oldsrc
            #/html/body/div[1]/div/div/div/div/main/ul/li[1]/a/figure/img
            item['collectionImageLink'] = str(li.xpath("./a/figure/img/@src").extract_first())


            #注意是否是全路径
            #怎么判断是否是全路径
            #http://www.zhejiangmuseum.com/Collection/ExcellentCollection/6039zonghepingtaiexhibit/6039zonghepingtaiexhibit
            #/html/body/div[1]/div/div/div/div/main/ul/li[1]/a
            url = "http://www.zhejiangmuseum.com/" + str(li.xpath("./a/@href").extract_first())

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
            'normalize-space(/html/body/div[1]/div/div/div/div/main/div/div[3])').extract_first()

        item["collectionIntroduction"] = "".join(item["collectionIntroduction"].split())
        item["collectionIntroduction"] = re.sub(r, '', item["collectionIntroduction"])
        print(item)
        yield item
