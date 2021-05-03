#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/4/18 20:44 
# @Author  : ana
# @File    : Museum0.py
# @Software: PyCharm
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from ..items import *

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")


class Museum0(scrapy.Spider):
    name = "Museum0"
    allowed_domains = ['dpm.org.cn']
    start_urls = ['https://www.dpm.org.cn/Home.html']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.MuseumPipeLine': 300,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'mySpider.middlewares.Museum0Middleware': 407,
        }
    }

    def __init__(self):
        self.browser = webdriver.Chrome(chrome_options=chrome_options)
        super().__init__()

    def close(self, spider, reason):
        self.browser.quit()

    def parse(self, response, **kwargs):
        item = MuseumBasicInformationItem()
        item["museumID"] = 0
        item["museumName"] = "故宫博物院"
        item["address"] = "北京市东城区景山前街4号"
        entryTime = response.xpath(
            "/html/body/div[5]/div[2]/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/div/div[1]/h1/text()").extract_first()
        ticketClosingTime = response.xpath(
            "//*[@id='container']/div[2]/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/div/div[2]/h1/text()").extract_first()
        stopEntryTime = response.xpath(
            "//*[@id='container']/div[2]/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/div/div[3]/h1/text()").extract_first()
        closeTime = response.xpath(
            "//*[@id='container']/div[2]/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/div/div[4]/h1").extract_first()
        item[
            "openingTime"] = "开放进馆时间：" + str(entryTime) + " 止票时间：" + str(ticketClosingTime) + " 停止入馆时间：" + str(
            stopEntryTime) + " 闭馆时间：" + str(closeTime)
        item["consultationTelephone"] = response.xpath(
            "//*[@id='container']/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/div[3]/div[3]/span[1]/text()").extract_first()
        item["introduction"] = response.xpath("//meta[@name='description']/@content").extract_first()
        item["publicityVideoLink"] = "https://img.dpm.org.cn/Uploads/video/8dazuo_hubiao.mp4"
        item["longitude"] = "116.403414"
        item["latitude"] = "39.924091"
        print(item)
        yield item
