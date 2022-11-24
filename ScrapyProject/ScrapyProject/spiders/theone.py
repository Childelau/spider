import scrapy


class TheoneSpider(scrapy.Spider):
    name = 'theone'
    allowed_domains = ['www.theone.art']
    start_urls = ['http://www.theone.art/']

    def parse(self, response):
        pass
