# -*- coding: utf-8 -*-
import scrapy
import re


class GithubSpider(scrapy.Spider):
    name = 'github'
    allowed_domains = ['github.com']
    start_urls = ['https://github.com/login']

    def parse(self, response):
        commit = response.xpath("//input[@name='commit']/@value").extract_first()
        utf8 = response.xpath("//input[@name='utf8']/@value").extract_first()
        authenticity_token = response.xpath("//input[@name='authenticity_token']/@value").extract_first()
        ga_id = response.xpath("//input[@name='ga_id']/@value").extract_first()
        login = "Dancing - in -air"
        password = ""
        webauthn_support = response.xpath("//input[@name='webauthn-support']/@value").extract_first()
        webauthn_iuvpaa_support = response.xpath("//input[@name='webauthn-iuvpaa-support']/@value").extract_first()
        # required_field = response.xpath("//input[@type='text' and @hidden]/@name").extract_first()
        timestamp = response.xpath("//input[@name='timestamp']/@value").extract_first()
        timestamp_secret = response.xpath("//input[@name='timestamp_secret']/@value").extract_first()
        post_data = dict(commit=commit, utf8=utf8, authenticity_token=authenticity_token, ga_id=ga_id, login=login,
                         password=password, webauthn_support=webauthn_support,
                         webauthn_iuvpaa_support=webauthn_iuvpaa_support,
                         timestamp=timestamp, timestamp_secret=timestamp_secret)
        yield scrapy.FormRequest("https://github.com/session", formdata=post_data, callback=self.after_login)

    def after_login(self, response):
        ret = re.findall("Dancing-in-air", response.body.decode())
        print(ret)
