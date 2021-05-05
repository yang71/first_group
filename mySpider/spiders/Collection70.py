from ..items import *
from ..str_filter import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options # 使用无头浏览器

#无头浏览器设置
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")


class Collection70(scrapy.Spider):
    name = "Collection70"
    allowed_domains = ['zmnh.com']
    start_urls = ['http://www.zmnh.com/henryhtml/collection.html?subid=1&sindex=0',
                  'http://www.zmnh.com/henryhtml/collection.html?subid=2&sindex=1',
                  'http://www.zmnh.com/henryhtml/collection.html?subid=3&sindex=2',
                  'http://www.zmnh.com/henryhtml/collection.html?subid=4&sindex=3']

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
            #/html/body/div/div/div[2]/div/div[4]/div[1]/div/div/div[1]
        li_list = response.xpath("/html/body/div/div/div[2]/div/div[4]/div[1]/div/div/div")
        for div in li_list:
            item = CollectionItem()
            item["museumID"] = 70
            item["museumName"] = "浙江自然博物院"

            # 名字的xpath都一样
            #/html/body/div/div/div[2]/div/div[4]/div[1]/div/div/div[1]/div/div/span
            r = re.compile(u"\\n|\\r|\\[.*?]|\\t")
            item['collectionName'] = div.xpath("./div/div/span/text()").extract_first()
            item["collectionName"] = "".join(item["collectionName"].split())
            item["collectionName"] = re.sub(r, '', item["collectionName"])

            # 注意是否为全路径，一般后缀为@src有的是@oldsrc
            #/html/body/div/div/div[2]/div/div[4]/div[1]/div/div/div[1]/div/img
            #http://www.zj-museum.com.cn/zjbwg/upload/image/2016/10/26/c77518090f884f399cb267729804242c_185x185.jpg
            item['collectionImageLink'] = div.xpath("./div/img/@src").extract_first()

            r = re.compile(u"\\n|\\r|\\[.*?]|\\t")

            item["collectionIntroduction"] = div.xpath("./div/div/span/text()").extract_first()
            item["collectionIntroduction"] = "".join(item["collectionIntroduction"].split())
            item["collectionIntroduction"] = re.sub(r, '', item["collectionIntroduction"])
            print(item)
            yield item
