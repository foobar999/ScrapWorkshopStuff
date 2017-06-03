import scrapy

class SelectorSpider(scrapy.Spider):
    name = 'selector'
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        res1 = response.css('div small')
        self.logger.info('res1: {}'.format(res1))
        #[<Selector data='<small...">'>, <Selector data='<small...">'>, ...]
        
        res2 = response.css('div small::text')
        self.logger.info('res2: {}'.format(res2))
        #[<Selector data='Albert Einstein'>, <Selector data='J.K. Rowling'>, ...]

        res3 = response.css('div small::text').extract()
        self.logger.info('res3: {}'.format(res3))
        #['Albert Einstein', 'J.K. Rowling', ...]
      
        res4 = response.css('div small::text').extract_first()
        self.logger.info('res4: {}'.format(res4))
        #Albert Einstein
        
        yield {'foo': 'bar'}
