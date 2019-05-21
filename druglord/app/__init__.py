import operator
from time import time
from ..engines import araujo, pacheco, pagmenos, raia
from ..models.product import Product


class SearchResults:
    def __init__(self, results: list = None):
        self.__results = results if isinstance(results, list) else []

    @property
    def results(self):
        return self.__results

    def append(self, value):
        self.__results.append(value)
        return self

    def merge(self, result_list: list):
        self.__results += result_list

    def order_by(self, attribute: str = 'price'):
        unordered = list(map(lambda p: p.to_dict(), self.__results))
        ordered = sorted(unordered, key=operator.itemgetter(attribute))
        self.__results = [Product(product['supplier'], product['name'],
                                  product['price'], product['available'])
                          for product in ordered]
        return self


class DrugLord(object):

    def __init__(self, browser):
        self.__results = SearchResults()
        self.engines = [araujo.Engine(browser), pagmenos.Engine(browser),
                        pacheco.Engine(browser), raia.Engine(browser)]
        self.search_time = 0.0

    @property
    def results(self):
        return self.__results.results

    def order_by(self, value: str = 'price'):
        self.__results.order_by(value)
        return self

    def search(self, term: str):
        start_time = time()
        for engine in self.engines:
            results = engine.search(term)
            self.__results.merge(results)
        end_time = time()
        self.search_time = end_time - start_time
        return self
