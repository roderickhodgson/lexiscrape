# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class Content(Item):
    # define the fields for your item here like:
    # name = Field()
    body_raw = Field()
    body_bag = Field()
    title = Field()
    tags = Field()
