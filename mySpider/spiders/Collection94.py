from ..items import *
from ..str_filter import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options  # 使用无头浏览器

# 无头浏览器设置
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")

class Collection94(scrapy.Spider):
    name = "Collection94"
    allowed_domains = ['jxmuseum.cn']
    start_urls = ['http://www.jxmuseum.cn/collection/jpxs?page=1',
                  'http://www.jxmuseum.cn/collection/jpxs?page=2']

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
            #/html/body/div[1]/div[2]/div/div[2]/ul/li[1]
        li_list = response.xpath("/html/body/div[1]/div[2]/div/div[2]/ul/li")
        for li in li_list:
            item = CollectionItem()
            item["museumID"] = 94
            item["museumName"] = "江西省博物馆"


            # 名字的xpath都一样
            #/html/body/div[1]/div[2]/div/div[2]/ul/li[1]/a[1]/p
            r = re.compile(u"\\n|\\r|\\[.*?]|\\t")
            item['collectionName'] = li.xpath("./a[1]/p/text()").extract_first()
            item["collectionName"] = "".join(item["collectionName"].split())
            item["collectionName"] = re.sub(r, '', item["collectionName"])

            # 注意是否是全路径
            # 怎么判断是否是全路径
            # http://www.portmuseum.cn/cp_read.php?id=47
            # /html/body/div[3]/div[2]/ul/li[1]/a
            url = "http://www.portmuseum.cn/" + str(li.xpath("./a/@href").extract_first())

            yield scrapy.Request(
                url,
                callback=self.parseAnotherPage,
                meta={"item": item}
            )

            # 翻页
            def parseAnotherPage(self, response):
                r = re.compile(u"\\n|\\r|\\[.*?]|\\t")
                item = response.meta["item"]

                item['collectionImageLink'] = response.xpath(
                    "/html/body/div[1]/div[2]/div/div/div[1]/div[2]/img/@src").extract_first()

                item["collectionIntroduction"] = response.xpath(
                    'normalize-space(/html/body/div[1]/div[2]/div/div/div[2])').extract_first()

                item["collectionIntroduction"] = "".join(item["collectionIntroduction"].split())
                item["collectionIntroduction"] = re.sub(r, '', item["collectionIntroduction"])
                print(item)
                yield item

