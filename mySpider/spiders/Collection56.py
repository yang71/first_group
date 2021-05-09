from ..items import *
from ..str_filter import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options # 使用无头浏览器

#无头浏览器设置
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")

class Collection56(scrapy.Spider):
    name = "Collection56"
    allowed_domains = ['njmuseum.com']
    start_urls = ['http://www.njmuseum.com/zh/collectionList']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.Collection56Middleware': 2333,
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
        #/html/body/div/div[3]/div/section/div[3]/div[2]/div[2]/div[1]
        li_list = response.xpath("/html/body/div/div[3]/div/section/div[3]/div[2]/div[2]/div")
        #print(li_list)
        for div in li_list:
            item = CollectionItem()
            item["museumID"] = 56
            item["museumName"] = "南京博物院"

            # 名字的xpath都一样
            #/html/body/div/div[3]/div/section/div[3]/div[2]/div[2]/div[1]
            #/html/body/div/div[3]/div/section/div[3]/div[2]/div[2]/div[1]/a/div[2]/h5
            item['collectionName'] = div.xpath("./a/div[2]/h5/text()").extract_first()

            # 注意是否为全路径，一般后缀为@src有的是@oldsrc
            #http://www.njmuseum.com/files/nb/collection/modify/2020/10/14/0%EF%BC%9A426-A-01.jpg
            #/html/body/div/div[3]/div/section/div[3]/div[2]/div[2]/div[1]
            #/html/body/div/div[3]/div/section/div[3]/div[2]/div[2]/div[1]/a/div[1]/img
            item['collectionImageLink'] = "http://www.njmuseum.com/"+div.xpath("./a/div[1]/img/@src").extract_first()

            #注意是否是全路径
            #怎么判断是否是全路径
            #/html/body/div/div[3]/div/section/div[3]/div[2]/div[2]/div[1]/a
            url = "http://www.njmuseum.com/"+str(div.xpath("./a/@href").extract_first())

            yield scrapy.Request(
                url,
                callback=self.parseAnotherPage,
                meta={"item": item}
            )
    #翻页
    #/html/body/div[5]/div[3]/div[6]/p/br[4]
    def parseAnotherPage(self, response):
        r = re.compile(u"\\n|\\r|\\[.*?]|\\t")
        item = response.meta["item"]
        #/html/body/div/div[3]/div/section/div[2]/div/div/p[1]/span[1]
        item["collectionIntroduction"] = response.xpath(
            'normalize-space(/html/body/div/div[3]/div/section/div[2]/div[1]/div/p[2])').extract_first()
        item["collectionIntroduction"] = "".join(item["collectionIntroduction"].split())
        item["collectionIntroduction"] = re.sub(r, '', item["collectionIntroduction"])
        print(item)
        yield item
