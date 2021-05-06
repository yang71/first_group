from ..items import *
from ..str_filter import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options # 使用无头浏览器

#无头浏览器设置
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")

class Collection61(scrapy.Spider):
    name = "Collection61"
    allowed_domains = ['czmuseum.com']
    start_urls = ['http://www.czmuseum.com/topNewsList?tname=gcjp']

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
            #/html/body/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[1]/div/div[2]/div[1]/div[1]/div/div[1]
        li_list = response.xpath("/html/body/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[1]/div/div[2]/div[1]/div[1]/div/div")
        #print(li_list)
        for div in li_list:
            item = CollectionItem()
            item["museumID"] = 61
            item["museumName"] = "常州博物馆"

            # 名字的xpath都一样
            #/html/body/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[1]/div/div[2]/div[1]/div[1]/div/div[1]/div/p
            item['collectionName'] = div.xpath("./div/p/text()").extract_first()

            # 注意是否为全路径，一般后缀为@src有的是@oldsrc
            #/html/body/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[1]/div/div[2]/div[1]/div[1]/div/div[1]/div/img
            item['collectionImageLink'] = div.xpath("./div/img/@src").extract_first()

            r = re.compile(u"\\n|\\r|\\[.*?]|\\t")
            #/html/body/div/div[3]/div/section/div[2]/div/div/p[1]/span[1]
            item["collectionIntroduction"] = div.xpath(
                'normalize-space(./div/p/text())').extract_first()
            item["collectionIntroduction"] = "".join(item["collectionIntroduction"].split())
            item["collectionIntroduction"] = re.sub(r, '', item["collectionIntroduction"])
            print(item)
            yield item
