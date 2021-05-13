from ..items import *
from ..str_filter import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options  # 使用无头浏览器

# 无头浏览器设置
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")

class Exhibition53(scrapy.Spider):
    name = "Exhibition53"
    allowed_domains = ['cyjng.net']
    start_urls = ['http://www.cyjng.net/Default.aspx?tabid=229&language=zh-CN',
                  'http://www.cyjng.net/Default.aspx?tabid=230&language=zh-CN',
                  'http://www.cyjng.net/Default.aspx?tabid=231&language=zh-CN',
                  'http://www.cyjng.net/Default.aspx?tabid=232&language=zh-CN',
                  'http://www.cyjng.net/Default.aspx?tabid=233&language=zh-CN']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.ExhibitionPipeLine': 302,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.Exhibition53Middleware': 2355,
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
        item = ExhibitionItem()
        item["museumID"] = 53
        item["museumName"] = "陈云纪念馆"

        # 名字的xpath都一样
        # /html/body/form/table//tr/td/table//tr[3]/td/table//tr[3]/td/table//tr/td[3]/div/div[1]/div[1]/span
        item['exhibitionName'] = StrFilter.filter(
            response.xpath("/html/body/form/table//tr/td/table//tr[3]/td/table//tr[3]/td/table//tr/td[3]/div/div[1]/div[1]/span").xpath('string(.)').extract_first())

        # /html/body/form/table//tr/td/table//tr[3]/td/table//tr[3]/td/table//tr/td[3]/div/div[2]/div/div/div/div[1]/img
        #http://www.cyjng.net/Portals/0/cldg/01/01/01.JPG
        str1 = 'http://www.cyjng.net/'
        str2 = str(response.xpath(
                "/html/body/form/table//tr/td/table//tr[3]/td/table//tr[3]/td/table//tr/td[3]/div/div[2]/div/div/div/div[1]/img/@src").extract_first())
        item["exhibitionImageLink"] = str1 + str2

        #/html/body/div[3]/div[1]/p
        item["exhibitionTime"] = "常设展览"

        #/html/body/form/table//tr/td/table//tr[3]/td/table//tr[3]/td/table//tr/td[3]/div/div[2]
        item['exhibitionIntroduction'] = StrFilter.filter(
            response.xpath("/html/body/form/table//tr/td/table//tr[3]/td/table//tr[3]/td/table//tr/td[3]/div/div[2]").xpath('string(.)').extract_first())
        print(item)
        yield item
