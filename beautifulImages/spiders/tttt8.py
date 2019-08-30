# -*- coding: utf-8 -*-
import scrapy
from beautifulImages.items import Tttt8Item


class Tttt8Spider(scrapy.Spider):
    name = 'tttt8'
    allowed_domains = ['tttt8.net']
    start_urls = [
        'http://www.tttt8.net/tgod/',
        'http://www.tttt8.net/category/xiurenwang/',
        'http://www.tttt8.net/category/ugirls/',
        'http://www.tttt8.net/category/legbaby/',
        'http://www.tttt8.net/category/kelagirls/',
        'http://www.tttt8.net/category/aiss/',
        'http://www.tttt8.net/category/girlt/',
        'http://www.tttt8.net/category/partycat/',
        'http://www.tttt8.net/category/zatu/'
    ]

    def parse(self, response):
        items = response.css("#post_container li")
        for item in items:
            target = item.css(".article a")
            title_name = target.xpath("text()").get()
            link = target.xpath("@href").get()
            yield response.follow(link, callback=self.parse_item, cb_kwargs={"title_name": title_name})

        next_page = response.css(".pagination .next::attr(href)").get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

    def parse_item(self, response, title_name):
        pagelist = response.css(".pagelist a::attr(href)").getall()
        if pagelist:
            for next_part in pagelist:
                yield response.follow(next_part, callback=self.parse_item, cb_kwargs={"title_name": title_name})

        image_urls = response.css("#post_content img::attr(src)").getall()
        tttt8Item = Tttt8Item()
        tttt8Item['file_urls'] = image_urls
        tttt8Item['title_name'] = title_name
        yield tttt8Item
