import scrapy

class IterSpider(scrapy.Spider):
    
    name = "iter"

    start_urls = [
        'http://quotes.toscrape.com/',
    ]

    def parse(self, response):
        quotes = response.css('div.quote')
        for q in quotes:
            yield {
                'author': q.css('.author::text').extract_first(),
                'text': q.css('.text::text').extract_first()
            }