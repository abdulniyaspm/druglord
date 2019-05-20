from abc import ABC, abstractmethod
from bs4 import BeautifulSoup
from typing import List
from ..models.product import Product


class GenericEngine(ABC):

    def __init__(self, browser):
        self.browser = browser

    @abstractmethod
    def search(self, term: str) -> List[Product]:
        pass

    @staticmethod
    @abstractmethod
    def parse_name(item) -> str:
        pass

    @staticmethod
    @abstractmethod
    def parse_price(item) -> float:
        pass

    def _get_soup(self, url: str) -> BeautifulSoup:
        self.browser.get(url)
        return BeautifulSoup(self.browser.page_source, 'html.parser')
