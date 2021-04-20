# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

import pymysql
from twisted.enterprise import adbapi


# 异步更新操作
class MuseumPipeLine(object):
    def __init__(self, dbpool):
        self.dbpool = dbpool

    @classmethod
    def from_settings(cls, settings):  # 函数名固定，会被scrapy调用，直接可用settings的值
        """
        数据库建立连接
        :param settings: 配置参数
        :return: 实例化参数
        """
        adbparams = dict(
            host=settings['MYSQL_HOST'],
            db=settings['MYSQL_DBNAME'],
            user=settings['MYSQL_USER'],
            password=settings['MYSQL_PASSWORD'],
            cursorclass=pymysql.cursors.DictCursor  # 指定cursor类型
        )

        # 连接数据池ConnectionPool，使用pymysql或者Mysqldb连接
        dbpool = adbapi.ConnectionPool('pymysql', **adbparams)
        # 返回实例化参数
        return cls(dbpool)

    def process_item(self, item, spider):
        """
        使用twisted将MySQL插入变成异步执行。通过连接池执行具体的sql操作，返回一个对象
        """
        name = spider.name
        name = name[0:6]
        if name == "Museum":
            query = self.dbpool.runInteraction(self.do_insert, item)  # 指定操作方法和操作数据
            query.addCallback(self.handle_error)  # 处理异常

    def do_insert(self, cursor, item):
        # 对数据库进行插入操作，并不需要commit，twisted会自动commit
        insert_sql = """insert into MuseumBasicInformation(museumID,museumName,openingTime,address,
        consultationTelephone,introduction,longitude,latitude,publicityVideoLink) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,
        %s) """
        cursor.execute(insert_sql, (
            item['museumID'], item['museumName'], item['openingTime'], item['address'],
            item['consultationTelephone'],
            item['introduction'], float(item['longitude']), float(item['latitude']), item['publicityVideoLink']))

    def handle_error(self, failure):
        if failure:
            # 打印错误信息
            print(failure)


class CollectionPipeLine(object):
    def __init__(self, dbpool):
        self.dbpool = dbpool

    @classmethod
    def from_settings(cls, settings):
        adbparams = dict(
            host=settings['MYSQL_HOST'],
            db=settings['MYSQL_DBNAME'],
            user=settings['MYSQL_USER'],
            password=settings['MYSQL_PASSWORD'],
            cursorclass=pymysql.cursors.DictCursor  # 指定cursor类型
        )

        dbpool = adbapi.ConnectionPool('pymysql', **adbparams)
        return cls(dbpool)

    def process_item(self, item, spider):
        name = spider.name
        name = name[0:10]
        if name == "Collection":
            query = self.dbpool.runInteraction(self.do_insert, item)  # 指定操作方法和操作数据
            query.addCallback(self.handle_error)  # 处理异常

    def do_insert(self, cursor, item):
        insert_sql = """insert into Collection(collectionName,collectionImageLink,collectionIntroduction,museumID,
        museumName) VALUES (%s,%s,%s,%s,%s) """

        cursor.execute(insert_sql, (
            item['collectionName'], item['collectionImageLink'], item['collectionIntroduction'], item['museumID'],
            item['museumName']))

    def handle_error(self, failure):
        if failure:
            print(failure)


class ExhibitionPipeLine(object):
    def __init__(self, dbpool):
        self.dbpool = dbpool

    @classmethod
    def from_settings(cls, settings):
        adbparams = dict(
            host=settings['MYSQL_HOST'],
            db=settings['MYSQL_DBNAME'],
            user=settings['MYSQL_USER'],
            password=settings['MYSQL_PASSWORD'],
            cursorclass=pymysql.cursors.DictCursor  # 指定cursor类型
        )

        dbpool = adbapi.ConnectionPool('pymysql', **adbparams)
        return cls(dbpool)

    def process_item(self, item, spider):
        name = spider.name
        name = name[0:10]
        if name == "Exhibition":
            query = self.dbpool.runInteraction(self.do_insert, item)  # 指定操作方法和操作数据
            query.addCallback(self.handle_error)  # 处理异常

    def do_insert(self, cursor, item):
        insert_sql = """insert into Exhibition(exhibitionName,exhibitionImageLink,exhibitionIntroduction,
        exhibitionTime,museumID, museumName) VALUES (%s,%s,%s,%s,%s,%s) """

        cursor.execute(insert_sql, (
            item['exhibitionName'], item['exhibitionImageLink'], item['exhibitionIntroduction'], item['exhibitionTime'],
            item['museumID'], item['museumName']))

    def handle_error(self, failure):
        if failure:
            print(failure)
