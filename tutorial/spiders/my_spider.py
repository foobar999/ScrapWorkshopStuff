import scrapy
import pprint

class MySpider(scrapy.Spider):
    
    name = "myspider"

    start_urls = [
        'http://quotes.toscrape.com/',
    ]

    def parse(self, response):
        entries = response.css('div.row div.quote')
        for i, entry in enumerate(entries):
            entry_data = {
                'author': entry.css('.author::text').extract(),
                'text': entry.css('.text::text').extract()
            }
            print('entry {}:\n{}'.format(i, pprint.pformat(entry_data)))