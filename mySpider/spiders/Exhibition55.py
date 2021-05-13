from ..items import *
from ..str_filter import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options  # 使用无头浏览器

# 无头浏览器设置
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")

class Exhibition55(scrapy.Spider):
    name = "Exhibition55"
    allowed_domains = ['slmmm.com']
    start_urls = ['https://www.slmmm.com/exhibit/subject.html']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.ExhibitionPipeLine': 302,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.Exhibition55Middleware': 2356,
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
            #/html/body/div[2]/section/div/div[2]/div/div[1]/a[1]
        li_list = response.xpath("/html/body/div[2]/section/div/div[2]/div/div[1]/a")
        # print(li_list)
        for a in li_list:
            item = ExhibitionItem()
            item["museumID"] = 55
            item["museumName"] = "上海市龙华烈士纪念馆"

            # 名字的xpath都一样
            #/html/body/div[2]/section/div/div[2]/div/div[1]/a[1]/div/div[2]/h3
            item['exhibitionName'] = StrFilter.filter(
                a.xpath("./div/div[2]/h3").xpath('string(.)').extract_first())

            #/html/body/div[2]/section/div/div[2]/div/div[1]/a[1]
            url = str(a.xpath("./@href").extract_first())

            yield scrapy.Request(
                url,
                callback=self.parseAnotherPage,
                meta={"item": item}
            )

    def parseAnotherPage(self, response):
        item = response.meta["item"]

        item["exhibitionImageLink"] = None

        item["exhibitionTime"] = "专题展览"

        item['exhibitionIntroduction'] = StrFilter.filter(
            response.xpath("/html/body/table//tr/td/table//tr[2]/td/div/p").xpath('string(.)').extract_first())
        print(item)
        yield item
