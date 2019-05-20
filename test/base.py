import unittest
from druglord.browser import Chrome


class BaseTestCase(unittest.TestCase):
    def setUp(self):
        self.browser = Chrome(headless=True)
