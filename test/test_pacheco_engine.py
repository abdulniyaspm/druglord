import unittest
from test.base import BaseTestCase
from druglord.engines import pacheco
from druglord.models.product import Product


class TestPachecoEngine(BaseTestCase):
    def test_engine(self):
        e = pacheco.Engine(self.browser)
        self.assertTrue(e)

    def test_search(self):
        e = pacheco.Engine(self.browser)
        results = e.search('ibuprofeno')
        self.assertIsInstance(results, list)
        self.assertIsInstance(results[0], Product)
        self.assertEqual(results[0].supplier, 'PACHECO')


if __name__ == '__main__':
    unittest.main()
