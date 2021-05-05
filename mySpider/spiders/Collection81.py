from ..items import *
from ..str_filter import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options  # 使用无头浏览器

# 无头浏览器设置
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")

class Collection81(scrapy.Spider):
    name = "Collection81"
    allowed_domains = ['zsbwg.com']
    start_urls = ['http://www.zsbwg.com/#/cangpinjiansuo/cangpinjiansuo2/:id?orderId=1&bool=true&sort=8a7aef0958b37e280158b38d781e0033&symbol=1']

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
            #/html/body/div/div[4]/div[2]/div[2]/div/div[1]/div[1]
        li_list = response.xpath("/html/body/div/div[4]/div[2]/div[2]/div/div[1]/div")
        for div in li_list:
            item = CollectionItem()
            item["museumID"] = 81
            item["museumName"] = "舟山博物馆"

            # 名字的xpath都一样
            #/html/body/div/div[4]/div[2]/div[2]/div/div[1]/div[1]/div/div[2]
            r = re.compile(u"\\n|\\r|\\[.*?]|\\t")
            item['collectionName'] = div.xpath("./div/div[2]/text()").extract_first()
            item["collectionName"] = "".join(item["collectionName"].split())
            item["collectionName"] = re.sub(r, '', item["collectionName"])

            r = re.compile(u"\\n|\\r|\\[.*?]|\\t|\)|\;")
            str1 = str(div.xpath("./div/div[1]/@style").extract_first())
            str2 = "http://www.zsbwg.com/"
            item['collectionImageLink'] = str1[str1.index(str2):];  # 获取 "."之后的字符(包含点) 结果.python
            item["collectionImageLink"] = re.sub(r, '', item["collectionImageLink"])


            item["collectionIntroduction"] = item["collectionName"]

            print(item)
            yield item
