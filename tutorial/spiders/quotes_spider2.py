import scrapy


class QuotesSpider2(scrapy.Spider):
    
    name = "quotes2"

    # Alternativ zu start_requests():
    # setze als Attribut 'start_urls' Liste von URLS
    # von diesen ausgehend wird mit default start_requests() gesucht
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
        'http://quotes.toscrape.com/page/2/',
    ]

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
        