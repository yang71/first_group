from ..items import *
from ..str_filter import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options  # 使用无头浏览器

# 无头浏览器设置
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")

class Exhibition37(scrapy.Spider):
    name = "Exhibition37"
    allowed_domains = ['sypm.org.cn']
    start_urls = ['http://www.sypm.org.cn/news_list5/newsCategoryId=9.html']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.ExhibitionPipeLine': 302,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.Exhibition37Middleware': 2350,
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
            #/html/body/div[1]/div[4]/div[1]/div/div[2]/div/div[2]/div/div/div[2]/div/div/div[1]/ul/li[1]
            #/html/body/div[1]/div[4]/div[1]/div/div[2]/div/div[2]/div/div/div[2]/div/div/div[1]/ul/li[3]
        li_list = response.xpath("/html/body/div[1]/div[4]/div[1]/div/div[2]/div/div[2]/div/div/div[2]/div/div/div[1]/ul/li")
        # print(li_list)
        k = 1
        for li in li_list:
            if(k%2 == 1):
                k = k+1
                item = ExhibitionItem()
                item["museumID"] = 37
                item["museumName"] = "沈阳故宫博物院"

                #名字的xpath都一样
                #/html/body/div[1]/div[4]/div[1]/div/div[2]/div/div[2]/div/div/div[2]/div/div/div[1]/ul/li[1]/div/ul/li[1]/h3/a
                item['exhibitionName'] = StrFilter.filter(
                li.xpath("./div/ul/li[1]/h3/a").xpath('string(.)').extract_first())

                #http://www.sypm.org.cn/news_detail/newsId=208.html
                #/html/body/div[1]/div[4]/div[1]/div/div[2]/div/div[2]/div/div/div[2]/div/div/div[1]/ul/li[1]/div/ul/li[1]/h3/a
                url = "http://www.sypm.org.cn/" + str(li.xpath("./div/ul/li[1]/h3/a/@href").extract_first())

                yield scrapy.Request(
                    url,
                    callback=self.parseAnotherPage,
                    meta={"item": item}
                )

    def parseAnotherPage(self, response):
        item = response.meta["item"]

        # /html/body/div[1]/div[4]/div[1]/div/div[1]/div[2]/form/div/div[2]/div/div/div[1]/div[2]/div[3]/p[3]/img
        # http://www.sypm.org.cn/imageRepository/0b7a31ce-769d-41c2-935e-70cc287cf79b.jpg
        str1 = "http://www.sypm.org.cn/"
        str2 = str(response.xpath(
            "/html/body/div[1]/div[4]/div[1]/div/div[1]/div[2]/form/div/div[2]/div/div/div[1]/div[2]/div[3]/p[3]/img/@src").extract_first())
        item["exhibitionImageLink"] = str1 + str2

        # /html/body/div[1]/div[4]/div[1]/div/div[1]/div[2]/form/div/div[2]/div/div/div[1]/div[2]/div[3]/p[1]
        item["exhibitionTime"] = StrFilter.filter(
                response.xpath("/html/body/div[1]/div[4]/div[1]/div/div[1]/div[2]/form/div/div[2]/div/div/div[1]/div[2]/div[3]/p[1]").xpath('string(.)').extract_first())

        #/html/body/div[1]/div[4]/div[1]/div/div[1]/div[2]/form/div/div[2]/div/div/div[1]/div[2]/div[3]/p[4]
        item['exhibitionIntroduction'] = StrFilter.filter(
            response.xpath("/html/body/div[1]/div[4]/div[1]/div/div[1]/div[2]/form/div/div[2]/div/div/div[1]/div[2]/div[3]/p[4]").xpath('string(.)').extract_first())
        print(item)
        yield item
