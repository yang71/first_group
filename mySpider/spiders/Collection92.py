from ..items import *
from ..str_filter import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options  # 使用无头浏览器

# 无头浏览器设置
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")

class Collection92(scrapy.Spider):
    name = "Collection92"
    allowed_domains = ['crt.com.cn']
    start_urls = ['http://www.crt.com.cn/mx/gcww.html']

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
            #/html/body/div/div/div/div[1]/ul/li[1]
        li_list = response.xpath("/html/body/div/div/div/div[1]/ul/li")
        for li in li_list:
            item = CollectionItem()
            item["museumID"] = 92
            item["museumName"] = "中央苏区（闽西）历史博物馆"

            # 名字的xpath都一样
            #/html/body/div/div/div/div[1]/ul/li[1]/span
            r = re.compile(u"\\n|\\r|\\[.*?]|\\t")
            item['collectionName'] = li.xpath("./span/text()").extract_first()
            item["collectionName"] = "".join(item["collectionName"].split())
            item["collectionName"] = re.sub(r, '', item["collectionName"])

            # 注意是否为全路径，一般后缀为@src有的是@oldsrc
            #/html/body/div/div/div/div[1]/ul/li[1]/img
            #http://www.crt.com.cn/mx/gcwwpig/1.jpg
            item['collectionImageLink'] = "http://www.crt.com.cn/mx/" + li.xpath("./img/@src").extract_first()

            item["collectionIntroduction"] = item['collectionName']
            print(item)
            yield item
