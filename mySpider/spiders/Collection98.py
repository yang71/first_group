from ..items import *
from ..str_filter import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options  # 使用无头浏览器

# 无头浏览器设置
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")

class Collection98(scrapy.Spider):
    name = "Collection98"
    allowed_domains = ['bdsrjng.cn']
    start_urls = ['http://www.bdsrjng.cn/article/getItemList.htm?teguid=982001d0a3fe4c8c93101f4a1aa687ad']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.Collection81Middleware': 2346,
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
            #/html/body/div[1]/div[4]/div[2]/div/div/ul/li[1]
        li_list = response.xpath("/html/body/div[1]/div[4]/div[2]/div/div/ul/li")
        for li in li_list:
            item = CollectionItem()
            item["museumID"] = 98
            item["museumName"] = "八大山人纪念馆"

            r = re.compile(u"\\n|\\r|\\[.*?]|\\t")
            #注意是否为全路径，一般后缀为@src有的是@oldsrc
            #/html/body/div[1]/div[4]/div[2]/div/div/ul/li[1]/a/span
            item['collectionName'] = li.xpath("./a/span/text()").extract_first()
            item["collectionName"] = "".join(item["collectionName"].split())
            item["collectionName"] = re.sub(r, '', item["collectionName"])

            #/html/body/div[1]/div[4]/div[2]/div/div/ul/li[1]/a
            #http://www.bdsrjng.cn/article/collections_detail.htm?isguid=95cdb97e831c4376a2d06fb3869877e3
            url = "http://www.bdsrjng.cn/article/" + str(li.xpath("./a/@href").extract_first())

            yield scrapy.Request(
                url,
                callback=self.parseAnotherPage,
                meta={"item": item}
            )
    # 翻页
    def parseAnotherPage(self, response):
        r = re.compile(u"\\n|\\r|\\[.*?]|\\t")
        item = response.meta["item"]

        # /html/body/div[1]/div[4]/div[2]/div/div/ul/li[1]/a/img
        item['collectionImageLink'] = response.xpath(
            "/html/body/div[1]/div[4]/div[2]/div[3]/center[1]/a/img/@src").extract_first()

        r = re.compile(u"\\n|\\r|\\[.*?]|\\t")

        item["collectionIntroduction"] = item["collectionName"]
        print(item)
        yield item
