from ..items import *
from ..str_filter import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options  # 使用无头浏览器

# 无头浏览器设置
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")


class Exhibition56(scrapy.Spider):
    name = "Exhibition56"
    allowed_domains = ['njmuseum.com']
    start_urls = ['http://www.njmuseum.com/zh/exhibitionList?id=3&pid=0']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.ExhibitionPipeLine': 302,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.Exhibition56Middleware': 2357,
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
        # /html/body/div/div[3]/div/section/div[3]/div/div[2]/ul/li[1]
        li_list = response.xpath("/html/body/div/div[3]/div/section/div[3]/div/div[2]/ul/li")
        # print(li_list)
        for li in li_list:
            item = ExhibitionItem()
            item["museumID"] = 56
            item["museumName"] = "南京博物院"

            # 名字的xpath都一样
            # /html/body/div/div[3]/div/section/div[3]/div/div[2]/ul/li[1]/a/div[3]/div[1]
            item['exhibitionName'] = StrFilter.filter(
                li.xpath("./a/div[3]/div[1]").xpath('string(.)').extract_first())

            # /html/body/div/div[3]/div/section/div[3]/div/div[2]/ul/li[1]/a/div[2]/img
            # http://www.njmuseum.com/files/nb/exhibition/images/2021/04/08/0209f2c17ee7cc2991b02abcc77a927a.jpg
            str1 = 'http://www.njmuseum.com/'
            str2 = str(li.xpath(
                "./a/div[2]/img/@data-src").extract_first())
            item["exhibitionImageLink"] = str1 + str2

            # /html/body/div/div[3]/div/section/div[3]/div/div[2]/ul/li[1]/a/div[3]/div[2]/span[2]/em
            item["exhibitionTime"] = StrFilter.filter(
                li.xpath("./a/div[3]/div[2]/span[2]/em").xpath('string(.)').extract_first())

            # /html/body/div/div[3]/div/section/div[3]/div/div[2]/ul/li[1]/a
            # http://www.njmuseum.com/zh/generalDetails?id=936
            url = "http://www.njmuseum.com" + str(
                li.xpath("./a/@href").extract_first())
            yield scrapy.Request(
                url,
                callback=self.parseAnotherPage,
                meta={"item": item}
            )

    def parseAnotherPage(self, response):
        item = response.meta["item"]
        item['exhibitionIntroduction'] = StrFilter.filter(
            response.xpath("/html/body/div/div[3]/div/section/div[3]/div/div[1]/div/div[1]").xpath(
                'string(.)').extract_first())
        print(item)
        yield item
