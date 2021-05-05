from ..items import *
from ..str_filter import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options  # 使用无头浏览器

# 无头浏览器设置
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")

class Collection97(scrapy.Spider):
    name = "Collection97"
    allowed_domains = ['aymuseum.com']
    start_urls = ['http://www.aymuseum.com/nr.jsp?_jcp=4_2#_np=120_0']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        }
    }

    # 实例化一个浏览器对象
    def __init__(self):
        self.browser = webdriver.Chrome(chrome_options=chrome_options)
        super().__init__()

    # 整个爬虫结束后关闭浏览器
    def close(self, spider):
        self.browser.quit()

    def parse(self, response, **kwargs):
        #/html/body/div[1]/div[8]/div/div/div[2]/div[2]/div[2]/table/tbody/tr/td[2]/div[1]/div/div/div/div/div[1]/div/div[1]
        #/html/body/div[1]/div[8]/div/div/div[2]/div[2]/div[2]/table/tbody/tr/td[2]/div[1]/div/div/div/div/div[1]/div/div[3]
        #/html/body/div[1]/div[8]/div/div/div[2]/div[2]/div[2]/table/tbody/tr/td[2]/div[1]/div/div/div/div/div[1]/div/div[5]
        #/html/body/div[1]/div[8]/div/div/div[2]/div[2]/div[2]/table/tbody/tr/td[2]/div[1]/div/div/div/div/div[1]/div/div[7]
        #/html/body/div[1]/div[8]/div/div/div[2]/div[2]/div[2]/table/tbody/tr/td[2]/div[1]/div/div/div/div/div[1]/div/div[9]

        li_list = response.xpath("/html/body/div[1]/div[8]/div/div/div[2]/div[2]/div[2]/table/tbody/tr/td[2]/div[1]/div/div/div/div/div[1]/div/div")
        for div in li_list[::2]:
            item = CollectionItem()
            item["museumID"] = 97
            item["museumName"] = "安源路矿工人运动纪念馆"

            r = re.compile(u"\\n|\\r|\\[.*?]|\\t")

            item['collectionName'] = div.xpath("./table//tr/td[2]/a/text()").extract_first()
            item["collectionName"] = "".join(item["collectionName"].split())
            item["collectionName"] = re.sub(r, '', item["collectionName"])

            url = "http://www.aymuseum.com/" + str(div.xpath("./table//tr/td[2]/a/@href").extract_first())

            yield scrapy.Request(
                url,
                callback=self.parseAnotherPage,
                meta={"item": item}
            )
    # 翻页
    def parseAnotherPage(self, response):
        r = re.compile(u"\\n|\\r|\\[.*?]|\\t")
        item = response.meta["item"]

        # /html/body/div[1]/div[8]/div/div/div[2]/div[2]/div[2]/table/tbody/tr/td[2]/div[1]/div/div/div/div/div/div[2]/p[1]/span/img
        item['collectionImageLink'] = "http:" + response.xpath("/html/body/div[1]/div[8]/div/div/div[2]/div[2]/div[2]/table//tr/td[2]/div[1]/div/div/div/div/div/div[2]/p[1]/span/img/@src").extract_first()

        r = re.compile(u"\\n|\\r|\\[.*?]|\\t")

        item["collectionIntroduction"] = response.xpath(
            'normalize-space(/html/body/div[1]/div[8]/div/div/div[2]/div[2]/div[2]/table//tr/td[2]/div[1]/div/div/div/div/div/div[2])').extract_first()

        item["collectionIntroduction"] = "".join(item["collectionIntroduction"].split())
        item["collectionIntroduction"] = re.sub(r, '', item["collectionIntroduction"])
        print(item)
        yield item
