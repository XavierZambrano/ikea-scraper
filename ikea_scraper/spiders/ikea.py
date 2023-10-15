import scrapy


class IkeaSpider(scrapy.Spider):
    name = "ikea"
    allowed_domains = ["ikea.com"]
    start_urls = ["https://ikea.com"]

    def parse(self, response):
        pass
