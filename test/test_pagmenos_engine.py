import unittest
from test.base import BaseTestCase
from druglord.engines import pagmenos
from druglord.models.product import Product


class TestPagMenosEngine(BaseTestCase):
    def test_engine(self):
        e = pagmenos.Engine(self.browser)
        self.assertTrue(e)

    def test_search(self):
        e = pagmenos.Engine(self.browser)
        results = e.search('ibuprofeno')
        self.assertIsInstance(results, list)
        self.assertIsInstance(results[0], Product)
        self.assertEqual(results[0].supplier, 'PAGMENOS')


if __name__ == '__main__':
    unittest.main()
