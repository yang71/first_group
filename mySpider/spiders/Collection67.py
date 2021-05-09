from ..items import *
from ..str_filter import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options # 使用无头浏览器

#无头浏览器设置
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")


class Collection67(scrapy.Spider):
    name = "Collection67"
    allowed_domains = ['csmuseum.cn']
    start_urls = ['http://www.csmuseum.cn/#/Gc/1']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.Collection67Middleware': 2335,
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
            #/html/body/div[1]/div[2]/div[2]/div[2]/div[1]
        li_list = response.xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div")
        for div in li_list:
            item = CollectionItem()
            item["museumID"] = 67
            item["museumName"] = "常熟博物馆"

            # 名字的xpath都一样
            #/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/p
            r = re.compile(u"\\n|\\r|\\[.*?]|\\t")
            item['collectionName'] = div.xpath("./p/text()").extract_first()
            item["collectionName"] = "".join(item["collectionName"].split())
            item["collectionName"] = re.sub(r, '', item["collectionName"])

            # 注意是否为全路径，一般后缀为@src有的是@oldsrc
            #/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/img
            #/html/body/div[1]/div[2]/div[2]/div[2]/div[2]/div/img
            #http://www.csmuseum.cn/UploadImg/1637347419339557031_a9f9b56a-4e9d-4d57-95c1-ebb3349d9778.jpg
            item['collectionImageLink'] = "http://www.csmuseum.cn/" + str(div.xpath("./div/img/@src").extract_first())

            #注意是否是全路径
            #怎么判断是否是全路径
            #http://www.wxmuseum.com/Collection/BookDetails/ed39c2e5-d3ad-4e45-92a1-cb95f4f4d9db
            #/html/body/div[4]/div/div[2]/div[2]/div[2]/ul/li[1]/a
            url = "https://www.xzmuseum.com/" + str(div.xpath("./a/@href").extract_first())

            item["collectionIntroduction"] = div.xpath("./p/text()").extract_first()
            item["collectionIntroduction"] = "".join(item["collectionIntroduction"].split())
            item["collectionIntroduction"] = re.sub(r, '', item["collectionIntroduction"])

            print(item)
            yield item
