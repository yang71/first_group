#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/5/1 15:56 
# @Author  : ana
# @File    : Collection24.py
# @Software: PyCharm

from ..items import *
from ..str_filter import *


class Collection24(scrapy.Spider):
    name = "Collection24"
    allowed_domains = ['hdmuseum.org']
    start_urls = ['https://www.hdmuseum.org/Home/collect_index']

    custom_settings = {
        'ITEM_PIPELINES': {
            'mySpider.pipelines.CollectionPipeLine': 301,
        }
    }

    def parse(self, response, **kwargs):
        names = ['红玛瑙带钩',
                 '清末青花褐彩妇人枕',
                 '碳化核桃',
                 '玉柄形器',
                 '磁州窑“康熙八年”文字酒缸']
        imgs = [
            'https://www.hdmuseum.org/UploadFile/2021-02-02/22716133a69c4d2d9b9444b9017ff448.jpg',
            'https://www.hdmuseum.org/UploadFile/2021-02-01/3f10f60bc25f4995aee1e610b9799ca2.JPG',
            'https://www.hdmuseum.org/UploadFile/2021-02-01/220536571623446a91817322d6cd45e8.JPG',
            'https://www.hdmuseum.org/UploadFile/2021-02-01/8866a91d515f470595a96e2c6ee4e7c4.JPG',
            'https://www.hdmuseum.org/UploadFile/2020-08-01/8a85107cbce7477eb99b656905527e2c.JPG'
        ]
        intros = [
            '红玛瑙带钩由整块玛瑙雕琢而成，体型硕大。是古代贵族和文人武士所系腰带的挂钩，古又称“犀比”。深红与青黄双色，正面深红色，可见斑状、枝条及水波状天然纹理；背面中部青黄，有絮状结构，不透明；钩首呈鸭嘴形，短颈，双层肩；腹部呈半圆形，表面略鼓，背面齐平，正中为较大的圆柄状钮。这件玛瑙带钩是战国时期玉带钩中的精品。如此体量和重量的器物当不是日常生活用品，而是特殊场合使用的礼仪用器。',
            '清末青花褐彩妇人枕，造型中妇人侧卧枕书，眉清目秀，清秀娴静，身着当时色彩艳丽的传统装束，蓝衣红裤，三寸金莲，自然屈身躺卧，腰身处凹陷的身形作为枕面，可谓是实用性与美观性的和谐统一。',
            '碳化胡桃，发现于磁山遗址的两座有树籽堆积层灰坑中，这就是磁山的第二项世界之最。这个容器中盛放的就是已经炭化了的胡桃，也就是核桃。磁山出土的炭化胡桃经缜密的碳14测定，距今已有7700年，从而否定了“引进”之说，证实了早在新石器时代，中原地区就已出现了核桃。',
            '商代玉礼器，早期又名“琴拨”、“簪形器”、“大圭”、“石祖”等，具体用途尚有争议，考古界因其形状构造而命名为“柄形器”，是一种代表墓主人身份兼具祭祀功能的器物。整体呈长条状,由柄首与柄身构成,柄首两侧弧形内收为颈,柄身两侧平直，通体素面无纹，呈青白色，部分钙化，打磨精良，为商代柄形器的典型样式。玉柄形器为夏至春秋时期中原地区常见的礼器，常出土于墓葬或祭祀坑中，二里头遗址中出土多件形制多样、纹饰精美的玉柄形器，商周时期玉柄形器的出土更为普遍，尤其是商代晚期至西周，数量大增，但大都形制简单，素面无纹，降至东周基本消失。',
            '磁州窑“康熙八年”文字酒缸，周身以颈部、肩部两组双水波纹和下腹部一周弦纹分割为三部分，下腹部空白，腹部饰一周花草纹，肩部一圈打油诗则十分有趣：“康熙八年，造下此坛。出在山西，郡名凌川，附城镇上，西南子山。” 这句话交代了此物的制作地点，接下来的词句，可算是大幅的广告语：“放酒酒好，成醋醋酸，放水不漏，淹菜菜咸，诸般都放，放密更甜；买上一个，君常喜欢，人人爱买，不论价钱，使了想使，胜活十年，请君先看，许多诗言，我要讨价，细细五钱。可好可好，直钱直钱。休走休走，快还快还，真正白货，去而何南。”不仅实用，而且物美价廉。这段打油诗版广告，读起来朗朗上口，市井之间买家与卖家讨价还价的场面被描绘得淋漓尽致，文字中虽有很多错别字，但意思表述清晰，字里行间透露出淳朴的民窑气息和民俗文化特色。'
        ]
        for i in range(4):
            item = CollectionItem()
            item["museumID"] = 24
            item["museumName"] = "邯郸市博物馆"
            item['collectionName'] = names[i]
            item['collectionImageLink'] = imgs[i]
            item['collectionIntroduction'] = intros[i]
            print(item)
            yield item
