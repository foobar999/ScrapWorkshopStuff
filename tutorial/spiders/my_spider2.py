import scrapy

class MySpider2(scrapy.Spider):
    
    name = "myspider2"

    start_urls = [
        'http://quotes.toscrape.com/',
    ]

    def parse(self, response):
        entries = response.css('div.row div.quote')
        for entry in entries:
            entry_data = {
                'author': entry.css('.author::text').extract(),
                'text': entry.css('.text::text').extract(),
                # Attributzugriff
                'prop': entry.css('.author::attr(itemprop)').extract()
            }
            # gibt Ergebnis-Datenstruktur an scrapy zurück
            # falls scrapy mit "-o <OUTFILE>" aufgerufen: schreibts in ne Datei
            yield entry_data