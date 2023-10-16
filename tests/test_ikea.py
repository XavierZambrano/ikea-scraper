import unittest
from scrapy.crawler import CrawlerProcess
from ikea_scraper.spiders.ikea import IkeaSpider
from ikea_scraper.utils.helpers import fake_response_from_file


if 'unittest.util' in __import__('sys').modules:
    # Show full diff in self.assertEqual.
    __import__('sys').modules['unittest.util']._MAX_LENGTH = 999999999


class TestIkeaScraper(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None
        self.spider = IkeaSpider(url='')
        process = CrawlerProcess(install_root_handler=False)
        crawler = process.create_crawler(IkeaSpider)
        self.spider.crawler = crawler

    def test_parse(self):
        fake_response = fake_response_from_file('assets/30360468.html')
        expected_result = {'data_product_id': '30360468', 'data_product_type': 'ART', 'data_product_rating': '4.5', 'data_online_sellable': 'true', 'data_product_price': '299.99', 'data_use_observe_product_details': 'true', 'data_product_name': 'MALM'}

        result = self.spider.parse(fake_response)
        result = list(result)

        self.assertEqual(1, len(result))
        result = result[0]

        self.assertEqual(result['data_product_name'], 'MALM')
        self.assertEqual(expected_result, result)

