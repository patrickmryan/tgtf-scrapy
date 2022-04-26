import scrapy
from scrapy.spiders import CrawlSpider

# https://coderslegacy.com/python/scrapy-extract-links-from-web-pages/
# https://doc.scrapy.org/en/latest/intro/overview.html#

# class QuotesSpider(scrapy.Spider):
#     name = 'quotes'
#     start_urls = [
#         'https://theregoesthefear.com/',
#     ]
#
#     def parse(self, response):
#         for quote in response.css('div.quote'):
#             yield {
#                 'author': quote.xpath('span/small/text()').get(),
#                 'text': quote.css('span.text::text').get(),
#             }
#
#         next_page = response.css('li.next a::attr("href")').get()
#         if next_page is not None:
#             yield response.follow(next_page, self.parse)

class SuperSpider(CrawlSpider):
    name = 'extractor'
    allowed_domains = ['theregoesthefear.com/']
    start_urls = ['https://theregoesthefear.com/']
    base_url = 'https://theregoesthefear.com/'

    def parse(self, response):
        for link in response.xpath('//div/p/a'):
            yield {
                "link": self.base_url + link.xpath('.//@href').get()
            }
