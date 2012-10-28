# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html

from scrapy.exceptions import DropItem
from lexiscrape_crawler import settings
from data_processing import remove_nonalpha, add_tags, strip_stopwords

from string import lower

class CleanBody(object):
    def process_item(self, item, spider):
        if item['body_raw']:
            item['body_bag'] = lower(remove_nonalpha(" ".join(item['body_raw'])))
        else:
            raise DropItem("Missing the raw body in %s" % item)
        return item
            


class CleanTitle(object):
    def process_item(self, item, spider):
        if item['title']:
            item['title'] = lower(remove_nonalpha(item['title']))
        else:
            raise DropItem("Missing title in %s" % item)
        return item

class GenerateTags(object):
    def process_item(self, item, spider):
        if item['body_bag'] and item['title']:
            tags = {}
            tags = add_tags(item['body_bag'], tags, settings.BODY_WEIGHT)
            tags = add_tags(item['title'], tags, settings.TITLE_WEIGHT)
            item['tags'] = tags
        else:
            raise DropItem("Missing body bag of words or title in %s" % item)
        return item

