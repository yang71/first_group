# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MuseumBasicInformationItem(scrapy.Item):
    museumID = scrapy.Field()
    museumName = scrapy.Field()
    openingTime = scrapy.Field()
    address = scrapy.Field()
    consultationTelephone = scrapy.Field()
    introduction = scrapy.Field()
    longitude = scrapy.Field()
    latitude = scrapy.Field()
    publicityVideoLink = scrapy.Field()


class CollectionItem(scrapy.Item):
    collectionID = scrapy.Field()  # collection为自增ID
    collectionName = scrapy.Field()
    collectionIntroduction = scrapy.Field()
    collectionImageLink = scrapy.Field()

    museumID = scrapy.Field()
    museumName = scrapy.Field()


class ExhibitionItem(scrapy.Item):
    exhibitionID = scrapy.Field()  # exhibition为自增ID
    exhibitionName = scrapy.Field()
    exhibitionIntroduction = scrapy.Field()
    exhibitionImageLink = scrapy.Field()
    exhibitionTime = scrapy.Field()

    museumID = scrapy.Field()
    museumName = scrapy.Field()
