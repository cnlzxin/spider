import re
import scrapy

from bs4 import BeautifulSoup

class docsspider(scrapy.Spider):

    name = 'docs'
    start_urls = ['https://docs.python.org/3/']

    precompiler_words = re.compile(r'[a-z]{3,}')
    precompiler_url = re.compile(r'https://docs.python.org/3/')


    def parse(self, response):

        html = response.body
        soup = BeautifulSoup(html)
        data = soup.get_text().lower()
        words = self.precompiler_words.findall(data)

        yield {response.url: words}

        next_pages = response.css('body div.body a::attr(href)').extract()
        if len(next_pages) != 0:
            for elem in next_pages:
                next_page = response.urljoin(elem)
                if self.precompiler_url.match(next_page):
                    yield scrapy.Request(next_page, callback=self.parse)
