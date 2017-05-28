import scrapy

class QuotesSpider3(scrapy.Spider):
    
    name = "quotes3"

    start_urls = [
        'http://quotes.toscrape.com/page/1/',
    ]

    def parse(self, response):
        self.logger.info('handling response of {}'.format(response.url))
        for quote in response.css('div.quote'):
            
            # Daten holen
            quote_data = {
                'text': quote.css('span.text::text').extract_first(),
                'author': quote.css('small.author::text').extract_first(),
                'tags': quote.css('div.tags a.tag::text').extract()
            }
            yield quote_data
            
            # selektiere passende <a>-Elemente
            next_pages = response.css('li.next a::attr(href)').extract()
            self.log('extracted next_pages {}'.format(next_pages))            
            for href in next_pages:                
                # durchsuche die URL href mit demselben parse() als callback
                # .follow() liefert ein Request-Objekt -> dieses wird automatisch von scrapy ausgewertet?
                yield response.follow(href, callback=self.parse)
                
                