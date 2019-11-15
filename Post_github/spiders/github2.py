# -*- coding: utf-8 -*-
import scrapy
import re


class Github2Spider(scrapy.Spider):
    name = 'github2'
    allowed_domains = ['github.com']
    start_urls = ['https://github.com/login']

    def parse(self, response):
        data = {"login": "Dancing-in-air", "password": ""}
        yield scrapy.FormRequest.from_response(response, formdata=data, callback=self.parse_page)

    def parse_page(self, response):
        ret = re.findall("Dancing-in-air", response.body.decode())
        print(ret)
