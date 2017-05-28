import scrapy

# Spider-Klasse
class QuotesSpider1(scrapy.Spider):
    
    # eindeutiger Name für diesen Spider
    name = "quotes1"

    # liefert Request-Objekte als iterable
    # diese werden danach als HTTP-Requests umgesetzt
    # hier: als generator über 'yield' relisiert
    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    # verarbeitet Ergebnis response eines HTTP-Response
    # Datentyp von response: 'TextResponse'
    # hier: hole Seitennummer X aus URL, schreibe Inhalt von Response in Datei "quotes-X.html"
    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        # deprecated! (https://doc.scrapy.org/en/latest/topics/logging.html)
        #self.log('Saved file %s' % filename)
        self.logger.info('saved file {}'.format(filename))
        