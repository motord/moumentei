# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class MoumenteiItem(Item):
    # define the fields for your item here like:
    author = Field()
    like = Field()
    dislike = Field()
    published_at = Field()
    content = Field()
    url = Field()
