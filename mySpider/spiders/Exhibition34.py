from ..items import *
from ..str_filter import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options  # 使用无头浏览器

# 无头浏览器设置
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")


class Exhibition34(scrapy.Spider):
    name = "Exhibition34"
    allowed_domains = ['lnmuseum.com.cn']
    #http://www.lnmuseum.com.cn/news/?ChannelID=430
    start_urls = ['http://www.lnmuseum.com.cn/news/?ChannelID=430']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.ExhibitionPipeLine': 302,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.Exhibition34Middleware': 2348,
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
            # /html/body/table[2]//tr[2]/td/table//tr/td[4]/table//tr[3]/td/table[1]
        li_list = response.xpath("/html/body/table[2]//tr[2]/td/table//tr/td[4]/table//tr[3]/td/table")
        # print(li_list)
        for table in li_list:
            item = ExhibitionItem()
            item["museumID"] = 34
            item["museumName"] = "辽宁省博物馆"

            # 名字的xpath都一样
            # /html/body/table[2]//tr[2]/td/table//tr/td[4]/table//tr[3]/td/table[1]//tr[1]/td[2]/a
            item['exhibitionName'] = table.xpath(".//tr[1]/td[2]/a/text()").extract_first()

            #/html/body/table[2]//tr[2]/td/table//tr/td[4]/table//tr[3]/td/table[1]//tr[1]/td[1]/a/img
            #http://www.lnmuseum.com.cn/UpLoadFile/image/20180424/20180424154656425642.jpg
            item["exhibitionImageLink"] = "http://www.lnmuseum.com.cn/" + str(response.xpath(
                ".//tr[1]/td[1]/a/img/@src").extract_first())

            #/html/body/table[2]//tr[2]/td/table//tr/td[4]/table//tr[3]/td/table[1]//tr[2]/td
            item["exhibitionTime"] = StrFilter.filter(
                table.xpath(".//tr[2]/td").xpath('string(.)').extract_first())

            item['exhibitionIntroduction'] = None
            print(item)
            yield item
