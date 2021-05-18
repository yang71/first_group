from ..items import *
from ..str_filter import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options  # 使用无头浏览器

# 无头浏览器设置
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")

class Exhibition38(scrapy.Spider):
    name = "Exhibition38"
    allowed_domains = ['dlmodernmuseum.com']
    start_urls = ['https://www.dlmodernmuseum.com/exhibition/']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.ExhibitionPipeLine': 302,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.Exhibition38Middleware': 2351,
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
            #/html/body/div[6]/ul/li[1]
        li_list = response.xpath("/html/body/div[6]/ul/li")
        # print(li_list)
        for li in li_list:
            item = ExhibitionItem()
            item["museumID"] = 38
            item["museumName"] = "大连博物馆"

            #名字的xpath都一样
            #/html/body/div[6]/ul/li[1]/a/div/div/h1
            item['exhibitionName'] = StrFilter.filter(
            li.xpath("./a/div/div/h1").xpath('string(.)').extract_first())

            #/html/body/div[6]/ul/li[1]/a/div/img
            #https://www.dlmodernmuseum.com/static/upload/2020/09/15/0ef3860d4ab67663.jpg
            str1 = 'https://www.dlmodernmuseum.com/'
            str2 = str(li.xpath(
                "./a/div/img/@src").extract_first())
            item["exhibitionImageLink"] = str1 + str2

            #/html/body/div[6]/ul/li[1]/a/div/div/p
            item["exhibitionTime"] = StrFilter.filter(
                li.xpath("./a/div/div/p").xpath('string(.)').extract_first())

            #http://www.sypm.org.cn/news_detail/newsId=208.html
            #/html/body/div[6]/ul/li[1]/a
            url = str(li.xpath("./a/@href").extract_first())

            yield scrapy.Request(
                url,
                callback=self.parseAnotherPage,
                meta={"item": item}
            )

    def parseAnotherPage(self, response):
        item = response.meta["item"]

        #/html/body/div[6]
        item['exhibitionIntroduction'] = StrFilter.filter(
            response.xpath("/html/body/div[6]").xpath('string(.)').extract_first())
        print(item)
        yield item
