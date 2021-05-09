from ..items import *
from ..str_filter import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options  # 使用无头浏览器

# 无头浏览器设置
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")

class Collection78(scrapy.Spider):
    name = "Collection78"
    allowed_domains = ['tianyige.com.cn']
    start_urls = ['http://www.tianyige.com.cn/collection/ancientbooks']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.Collection78Middleware': 2340,
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
            #/html/body/div[1]/div[2]/div/div[2]/ul/li[1]
        li_list = response.xpath("/html/body/div[1]/div[2]/div/div[2]/ul/li")
        for tr in li_list:
            item = CollectionItem()
            item["museumID"] = 78
            item["museumName"] = "宁波市天一阁博物馆"

            # 名字的xpath都一样
            #/html/body/div[1]/div[2]/div/div[2]/ul/li[1]/a/div[2]/h3
            r = re.compile(u"\\n|\\r|\\[.*?]|\\t")
            item['collectionName'] = tr.xpath("./a/div[2]/h3/text()").extract_first()
            item["collectionName"] = "".join(item["collectionName"].split())
            item["collectionName"] = re.sub(r, '', item["collectionName"])

            #注意是否是全路径
            #怎么判断是否是全路径
            #/html/body/div[1]/div[2]/div/div[2]/ul/li[1]/a
            #http://www.tianyige.com.cn/collection/ancientbooks/fb1244f60c625e10946fd0642d3846e3
            url = "http://www.tianyige.com.cn" + str(tr.xpath("./a/@href").extract_first())

            yield scrapy.Request(
                url,
                callback=self.parseAnotherPage,
                meta={"item": item}
            )
    # 翻页
    def parseAnotherPage(self, response):
        r = re.compile(u"\\n|\\r|\\[.*?]|\\t")
        item = response.meta["item"]

        # 注意是否为全路径，一般后缀为@src有的是@oldsrc
        #/html/body/div[1]/div[2]/div/div/div/div[1]/img
        #http://www.tianyige.com.cn/file/TIANYIGE_BWG/CMS/CMS_EXHIBIT_INFO_IMG/20191025/10aae75fc1bc49df94f7ec5064053a6c1571994768929.jpg
        item['collectionImageLink'] = response.xpath(
            "/html/body/div[1]/div[2]/div/div/div/div[1]/img/@src").extract_first()

        item["collectionIntroduction"] = response.xpath(
            'normalize-space(/html/body/div[1]/div[2]/div/div/div/div[2])').extract_first()

        item["collectionIntroduction"] = "".join(item["collectionIntroduction"].split())
        item["collectionIntroduction"] = re.sub(r, '', item["collectionIntroduction"])
        print(item)
        yield item
