from ..items import *
from ..str_filter import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options  # 使用无头浏览器

# 无头浏览器设置
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")

class Exhibition52(scrapy.Spider):
    name = "Exhibition52"
    allowed_domains = ['sstm.org.cn']
    start_urls = ['http://www.sstm.org.cn/temporaryexhibition']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.ExhibitionPipeLine': 302,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.Exhibition52Middleware': 2354,
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
            #/html/body/div[1]/div/div[3]/div[2]/div[1]
        li_list = response.xpath("/html/body/div[1]/div/div[3]/div[2]/div")
        # print(li_list)
        for div in li_list:
            item = ExhibitionItem()
            item["museumID"] = 52
            item["museumName"] = "上海科技馆"

            # 名字的xpath都一样
            # /html/body/div[1]/div/div[3]/div[2]/div[1]/div[2]
            item['exhibitionName'] = StrFilter.filter(
                div.xpath("./div[2]").xpath('string(.)').extract_first())

            # /html/body/div[1]/div/div[3]/div[2]/div[1]/div[1]/span
            # str1 = 'http://www.zgyd1921.com/'
            str2 = str(div.xpath(
                "./div[1]/span/@data-src").extract_first())
            item["exhibitionImageLink"] = str2

            #/html/body/div[3]/div[1]/p
            item["exhibitionTime"] = "临时展览"

            #/html/body/div[3]/div[1]/div[2]
            item['exhibitionIntroduction'] = item['exhibitionName']
            print(item)
            yield item
