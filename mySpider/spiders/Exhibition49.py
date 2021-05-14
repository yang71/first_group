from ..items import *
from ..str_filter import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options  # 使用无头浏览器

# 无头浏览器设置
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")

class Exhibition49(scrapy.Spider):
    name = "Exhibition49"
    allowed_domains = ['shanghaimuseum.net']
    start_urls = ['https://www.shanghaimuseum.net/mu/frontend/pg/display/offline-exhibit']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.ExhibitionPipeLine': 302,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.Exhibition49Middleware': 2353,
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
            #/html/body/div[5]/div/div/ul[2]/li[1]
        li_list = response.xpath("/html/body/div[5]/div/div/ul[2]/li")
        # print(li_list)
        for li in li_list:
            item = ExhibitionItem()
            item["museumID"] = 49
            item["museumName"] = "上海博物馆"

            # 名字的xpath都一样
            # /html/body/div[5]/div/div/ul[2]/li[1]/div[2]
            item['exhibitionName'] = StrFilter.filter(
                li.xpath("./div[2]").xpath('string(.)').extract_first())

            #/html/body/div[5]/div/div/ul[2]/li[1]/div[1]/a
            #https://www.shanghaimuseum.net/mu/frontend/pg/article/id/E00004118
            url = "https://www.shanghaimuseum.net/mu/" + str(li.xpath("./div[1]/a/@href").extract_first())

            yield scrapy.Request(
                url,
                callback=self.parseAnotherPage,
                meta={"item": item}
            )

    def parseAnotherPage(self, response):
        item = response.meta["item"]

        # /html/body/div[4]/div/div/div[1]/img
        # https://www.shanghaimuseum.net/mu/upload/202101/616e74ab-1674-4a6c-8cdc-9590c3cb3eb8.jpg
        str1 = 'https://www.shanghaimuseum.net/mu/'
        str2 = str(response.xpath(
            "/html/body/div[4]/div/div/div[1]/img/@src").extract_first())
        item["exhibitionImageLink"] = str1 + str2

        #/html/body/div[4]/div/div/div[2]/div[2]
        item["exhibitionTime"] = StrFilter.filter(
                response.xpath("/html/body/div[4]/div/div/div[2]/div[2]").xpath('string(.)').extract_first())

        #/html/body/div[4]/div/div/div[2]
        item['exhibitionIntroduction'] = StrFilter.filter(
            response.xpath("/html/body/div[4]/div/div/div[2]").xpath('string(.)').extract_first())
        print(item)
        yield item
