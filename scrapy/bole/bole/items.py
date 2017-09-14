# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JobBoleArticleItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    create_time = scrapy.Field()
    url = scrapy.Field()
    url_object_id = scrapy.Field()
    font_image_url = scrapy.Field()
    font_image_path = scrapy.Field()
    up_num = scrapy.Field()
    fav_num = scrapy.Field()
    comment_num = scrapy.Field()
    tags = scrapy.Field()
    content = scrapy.Field()




