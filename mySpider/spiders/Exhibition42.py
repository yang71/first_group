from ..items import *
from ..str_filter import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options  # 使用无头浏览器

# 无头浏览器设置
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")

class Exhibition42(scrapy.Spider):
    name = "Exhibition42"
    allowed_domains = ['wmhg.com.cn']
    start_urls = ['https://www.wmhg.com.cn/exhibtion.html']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.ExhibitionPipeLine': 302,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.Exhibition42Middleware': 2352,
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
            #/html/body/div[3]/div/div[1]/div/div[2]/div/div[1]/div[1]
        li_list = response.xpath("/html/body/div[3]/div/div[1]/div/div[2]/div/div[1]/div")
        # print(li_list)
        for div in li_list:
            item = ExhibitionItem()
            item["museumID"] = 42
            item["museumName"] = "伪满皇宫博物院"

            #/html/body/div[3]/div/div[1]/div/div[2]/div/div[1]/div[1]/div[1]/a/img
            #https://www.wmhg.com.cn/Uploads/Picture/2019/12/09/s5dedba6a59f80.jpg
            str1 = 'https://www.wmhg.com.cn/'
            str2 = str(div.xpath(
                "./div[1]/a/img/@src").extract_first())
            item["exhibitionImageLink"] = str1 + str2

            #/html/body/div[3]/div/div[1]/div/div[2]/div/div[1]/div[1]/div[2]/div[1]
            item["exhibitionTime"] = StrFilter.filter(
                div.xpath("./div[2]/div[1]").xpath('string(.)').extract_first())

            #https://www.wmhg.com.cn/detail/1832.html
            #/html/body/div[3]/div/div[1]/div/div[2]/div/div[1]/div[1]/div[2]/a
            url = "https://www.wmhg.com.cn/" + str(div.xpath("./div[2]/a/@href").extract_first())

            yield scrapy.Request(
                url,
                callback=self.parseAnotherPage,
                meta={"item": item}
            )

    def parseAnotherPage(self, response):
        item = response.meta["item"]

        # 名字的xpath都一样
        # /html/body/div[4]/div/div[1]/div/div
        # /html/body/div[4]/div/div[1]/div/div
        item['exhibitionName'] = StrFilter.filter(
            response.xpath("/html/body/div[4]/div/div[1]/div/div").xpath('string(.)').extract_first())

        #/html/body/div[4]/div/div[2]
        item['exhibitionIntroduction'] = StrFilter.filter(
            response.xpath("/html/body/div[4]/div/div[2]").xpath('string(.)').extract_first())
        print(item)
        yield item
