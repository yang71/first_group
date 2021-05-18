from ..items import *
from ..str_filter import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options  # 使用无头浏览器

# 无头浏览器设置
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")


class Exhibition30(scrapy.Spider):
    name = "Exhibition30"
    allowed_domains = ['linfenmuseum.com']
    start_urls = ['http://www.linfenmuseum.com/index.php/Index/exhibition.html#2019032004']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.ExhibitionPipeLine': 302,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.Exhibition30Middleware': 2347,
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
            # /html/body/div[2]/div[2]/div/div[2]/div[2]/div[2]/div/a[1]
            # /html/body/div[2]/div[2]/div/div[2]/div[2]/div[2]/div/a[2]
        li_list = response.xpath("/html/body/div[2]/div[2]/div/div[2]/div[2]/div[2]/div/a")
        # print(li_list)
        for a in li_list:
            item = ExhibitionItem()
            item["museumID"] = 30
            item["museumName"] = "临汾市博物馆"

            # 名字的xpath都一样
            # /html/body/div[2]/div[2]/div/div[2]/div[2]/div[2]/div/a[1]/div[2]
            item['exhibitionName'] = a.xpath("./div[2]/text()").extract_first()

            # 注意是否是全路径
            # 怎么判断是否是全路径
            # /html/body/div[2]/div[2]/div/div[2]/div[2]/div[2]/div/a[1]
            # http://www.linfenmuseum.com/index.php/Index/exhibitionnews_show?id=93&cid=30
            url = "http://www.linfenmuseum.com/" + str(a.xpath("./@href").extract_first())

            yield scrapy.Request(
                url,
                callback=self.parseAnotherPage,
                meta={"item": item}
            )

    # 翻页
    # /html/body/div[5]/div[3]/div[6]/p/br[4]
    def parseAnotherPage(self, response):
        item = response.meta["item"]
        #/html/body/div[3]/div[2]/div/div/div[2]/div[2]/p[1]/img
        #/html/body/div[3]/div[2]/div/div/div[2]/div[2]/p[1]/img
        item["exhibitionImageLink"] = StrFilter.getDoamin(response) + str(response.xpath(
            "/html/body/div[3]/div[2]/div/div/div[2]/div[2]/p[1]/img/@src").extract_first())
        item["exhibitionTime"] = None
        #/html/body/div[3]/div[2]/div/div/div[2]/div[2]/p[5]/span
        item['exhibitionIntroduction'] = StrFilter.filter_2(
            response.xpath("/html/body/div[3]/div[2]/div/div/div[2]/div[2]/p[5]/span").xpath('string(.)').extract_first())
        print(item)
        yield item
