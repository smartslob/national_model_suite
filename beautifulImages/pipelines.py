# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem
import logging
from scrapy.pipelines.files import FilesPipeline
import os
from urlparse import urlparse
import scrapy

logger = logging.getLogger(__name__)

class BeautifulimagesPipeline(object):
    def process_item(self, item, spider):
        return item


class Tttt8ImagePipeline(FilesPipeline):
    # EXPIRES = 180
    
    def file_path(self, request, response=None, info=None):
        target_path = request.meta["dirname"] + "/" + os.path.basename(urlparse(request.url).path)
        return target_path

    def get_media_requests(self, item, info):
        # logger.debug("media request: %s", item['title_name'])
        for file_url in item['file_urls']:
            yield scrapy.Request(file_url, meta={"dirname": item["title_name"]})