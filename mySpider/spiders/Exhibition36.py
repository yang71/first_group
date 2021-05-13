from ..items import *
from ..str_filter import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options  # 使用无头浏览器

# 无头浏览器设置
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")

class Exhibition36(scrapy.Spider):
    name = "Exhibition36"
    allowed_domains = ['lvshunmuseum.org']
    start_urls = ['http://www.lvshunmuseum.org/Exhibition/Default.aspx?SortID=27&Page=1']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.ExhibitionPipeLine': 302,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.Exhibition36Middleware': 2349,
        },
    }

    # 实例化一个浏览器对象
    def __init__(self):
        self.browser = webdriver.Chrome(chrome_options=chrome_options)
        super().__init__()

    # 整个爬虫结束后关闭浏览器
    def close(self, spider):
        self.browser.quit()


    def parse(self, response, **kwargs):
            #/html/body/div/div/div/div[2]/div[2]/div[1]/div/div[2]/div/div[2]/ul/li[1]
        li_list = response.xpath("/html/body/div/div/div/div[2]/div[2]/div[1]/div/div[2]/div/div[2]/ul/li")
        # print(li_list)
        for li in li_list:
            item = ExhibitionItem()
            item["museumID"] = 36
            item["museumName"] = "旅顺博物馆"

            #名字的xpath都一样
            #/html/body/div/div/div/div[2]/div[2]/div[1]/div/div[2]/div/div[2]/ul/li[1]/a/div[2]/h1
            item['exhibitionName'] = li.xpath("./a/div[2]/h1/text()").extract_first()

            #/html/body/div/div/div/div[2]/div[2]/div[1]/div/div[2]/div/div[2]/ul/li[1]/a/div[1]/img
            #http://www.lvshunmuseum.org/Exhibition/ /Upload/Product-Pictures/201903/20190315094704_446x334HW.jpg
            str1 = 'http://www.lvshunmuseum.org/'
            str2 = str(li.xpath(
                "./a/div[1]/img/@src").extract_first())
            item["exhibitionImageLink"] = str1+str2[1:]
            item["exhibitionTime"] = None

            #http://www.lvshunmuseum.org/Exhibition/%20/Exhibition/ProductDetail.aspx?ID=297
            #/html/body/div/div/div/div[2]/div[2]/div[1]/div/div[2]/div/div[2]/ul/li[1]/a
            url = "http://www.lvshunmuseum.org/" + str(li.xpath("./a/@href").extract_first())

            yield scrapy.Request(
                url,
                callback=self.parseAnotherPage,
                meta={"item": item}
            )

    def parseAnotherPage(self, response):
        item = response.meta["item"]
        #/html/body/div[3]/div/div/div[1]/div/div[2]/div/div[1]/div[2]/div[3]
        item['exhibitionIntroduction'] = item['exhibitionName']
        print(item)
        yield item
