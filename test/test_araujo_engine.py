import unittest
from test.base import BaseTestCase
from druglord.engines import araujo
from druglord.models.product import Product


class TestAraujoEngine(BaseTestCase):
    def test_engine(self):
        e = araujo.Engine(self.browser)
        self.assertTrue(e)

    def test_search(self):
        e = araujo.Engine(self.browser)
        results = e.search('ibuprofeno')
        self.assertIsInstance(results, list)
        self.assertIsInstance(results[0], Product)
        self.assertEqual(results[0].supplier, 'ARAUJO')


if __name__ == '__main__':
    unittest.main()
