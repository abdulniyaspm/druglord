import unittest
from test.base import BaseTestCase
from druglord.engines import raia
from druglord.models.product import Product


class TestRaiaEngine(BaseTestCase):
    def test_engine(self):
        e = raia.Engine(self.browser)
        self.assertTrue(e)

    def test_search(self):
        e = raia.Engine(self.browser)
        results = e.search('ibuprofeno')
        self.assertIsInstance(results, list)
        self.assertIsInstance(results[0], Product)
        self.assertEqual(results[0].supplier, 'RAIA')


if __name__ == '__main__':
    unittest.main()
