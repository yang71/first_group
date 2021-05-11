from ..items import *
from ..str_filter import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options  # 使用无头浏览器

# 无头浏览器设置
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")

class Collection77(scrapy.Spider):
    name = "Collection77"
    allowed_domains = ['hangzhou.gov.cn']
    start_urls = ['https://ywj.hangzhou.gov.cn/ymj-ms-collect-gm/']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.Collection77Middleware': 2339,
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
            #/html/body/div/div/div/div/div[3]/ul/li[1]
        li_list = response.xpath("/html/body/div/div/div/div/div[3]/ul/li")
        #print(li_list)
        for li in li_list:
            item = CollectionItem()
            item["museumID"] = 77
            item["museumName"] = "杭州工艺美术博物馆"

            # 名字的xpath都一样
            #/html/body/div/div/div/div/div[3]/ul/li[1]/a/p[2]
            r = re.compile(u"\\n|\\r|\\[.*?]|\\t")
            item['collectionName'] = li.xpath("./a/p[2]/text()").extract_first()
            item["collectionName"] = "".join(item["collectionName"].split())
            item["collectionName"] = re.sub(r, '', item["collectionName"])

            # 注意是否为全路径，一般后缀为@src有的是@oldsrc
            #/html/body/div/div/div/div/div[3]/ul/li[1]/a/p[1]/img
            item['collectionImageLink'] = li.xpath("./a/p[1]/img/@src").extract_first()

            #/html/body/div/div/div/div/div[3]/ul/li[1]/a/p[4]
            r = re.compile(u"\\n|\\r|\\[.*?]|\\t")
            item["collectionIntroduction"] = li.xpath(
                'normalize-space(./a/p[4])').extract_first()

            item["collectionIntroduction"] = "".join(item["collectionIntroduction"].split())
            item["collectionIntroduction"] = re.sub(r, '', item["collectionIntroduction"])
            print(item)
            yield item
