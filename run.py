# -*- coding: utf-8 -*-

from scrapy import cmdline

#设置图片存放目录
image_dir = "/opt/images"

cmdstr = 'scrapy crawl tttt8 -s FILES_STORE=' + image_dir
cmdline.execute(cmdstr.split())