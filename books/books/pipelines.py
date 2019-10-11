import re

from scrapy.exceptions import DropItem

class BooksPipeline(object):
    def process_item(self, item, spider):
        if item.get('stars') in ['Four', 'Five']:
            item['stock'] = int(re.search('\d+', item.get('stock'))[0])
            return item
        else:
            raise DropItem('The ' + item['title'] + ' book is too bad')
