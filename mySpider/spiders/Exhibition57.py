from ..items import *
from ..str_filter import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options  # 使用无头浏览器

# 无头浏览器设置
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")

class Exhibition57(scrapy.Spider):
    name = "Exhibition57"
    allowed_domains = ['19371213.com.cn']
    start_urls = ['http://www.19371213.com.cn/exhibition/temporary/']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.ExhibitionPipeLine': 302,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.Exhibition57Middleware': 2358,
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
            #/html/body/div[8]/div/div/div/div/div[2]/div/div/div[1]/div/div/div[1]
        li_list = response.xpath("/html/body/div[8]/div/div/div/div/div[2]/div/div/div[1]/div/div/div")
        # print(li_list)
        for div in li_list:
            item = ExhibitionItem()
            item["museumID"] = 57
            item["museumName"] = "侵华日军南京大屠杀遇难同胞纪念馆"

            #名字的xpath都一样
            #/html/body/div[8]/div/div/div/div/div[2]/div/div/div[1]/div/div/div[1]/section/div[2]/header/h3/a
            item['exhibitionName'] = StrFilter.filter(
            div.xpath("./section/div[2]/header/h3/a").xpath('string(.)').extract_first())

            #/html/body/div[8]/div/div/div/div/div[2]/div/div/div[1]/div/div/div[1]/section/div[1]/div[1]/a/img
            #http://www.19371213.com.cn/exhibition/temporary/202104/W020210430364887653123.jpg
            str1 = 'http://www.19371213.com.cn/exhibition/temporary/'
            str2 = str(div.xpath(
                "./section/div[1]/div[1]/a/img/@src").extract_first())
            item["exhibitionImageLink"] = str1 + str2[1:]

            #/html/body/div/div[3]/div[1]/div[2]/ul/li[1]/a/div[2]/div/div/div/p[1]
            item["exhibitionTime"] = "临时展览"

            #http://www.19371213.com.cn/exhibition/temporary/202104/t20210430_2902013.html
            #/html/body/div[8]/div/div/div/div/div[2]/div/div/div[1]/div/div/div[1]/section/div[2]/header/h3/a
            str3 = str(div.xpath("./section/div[2]/header/h3/a/@href").extract_first())
            url = "http://www.19371213.com.cn/exhibition/temporary/" + str3[1:]

            yield scrapy.Request(
                url,
                callback=self.parseAnotherPage,
                meta={"item": item}
            )

    def parseAnotherPage(self, response):
        item = response.meta["item"]

        #/html/body/div[8]/div/div/div/div[2]/div/div/article/section/div[2]/div/div/div/div
        item['exhibitionIntroduction'] = item['exhibitionName']
        print(item)
        yield item
