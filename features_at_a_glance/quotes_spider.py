import scrapy

# 'code at a glance' - Beispiel
# 'scrapy runspider features_at_a_glance/quotes_spider.py -o quotes.json'
# - scrapy sucht in dieser Datei nach Spider-Klasse
# - scrapy geht URLs in start_urls durch (asnychron)
# - QuotesSpider.parse(response) wird als Callback mit Antwort aufgerufen

# yield:
# - Funktionsaufruf mit 'yield' liefert Generator (der Funktionskörper wird aber *nicht* aufgerufen)
# - über diesen Generator kann iteriert werden -> jede Iteration ruft die Funktion 

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        # Zitate von irgendwelchen Leuten
        'http://quotes.toscrape.com/tag/humor/',
    ]

    def parse(self, response):
        print('response (type{}):\n{}'.format(type(response),response))
        # response.css() findet per CSS-Selektor Abschnitte in Response (<div class="quote">...</div>)
        for quote in response.css('div.quote'):
            yield {
                # quote.css() sucht in diesem Abschnitt wiederum per css
                'text': quote.css('span.text::text').extract_first(),
                'author': quote.xpath('span/small/text()').extract_first(),
            }

        next_page = response.css('li.next a::attr("href")').extract_first()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
            