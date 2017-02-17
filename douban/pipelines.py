# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import codecs, json

class FilterKeyPipeline(object):

    keys = ["十里堡"]

    def process_item(self, item, spider):
        if reduce(lambda x, y: x or self.contains(y, item), ['group_title', 'group_desc', 'group_replys'], False):
            return item
        else:
            raise DoubanGroupItem("no contains keys in %s" % item)

    def contains(self, k, item):
        return reduce(lambda x, y: x and y in item[k].encode('utf-8'), self.keys, True)

class CharPipeline(object):
    def __init__(self):
        self.file = codecs.open("out.json", "wb", encoding="utf-8")

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(line)
        return item

    def spider_closed(self, spider):
        self.file.close()
