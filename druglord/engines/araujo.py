from ..engines import GenericEngine
from ..models.product import Product
from typing import List


class Engine(GenericEngine):

    def search(self, term: str) -> List[Product]:
        results = []
        soup = self._get_soup(f'https://busca.araujo.com.br/busca?q={term}')
        if soup is not None:
            products = soup.select('span.vtex-cpSkuIds')

            for product in products:
                p = Product(
                    supplier='ARAUJO',
                    name=self.parse_name(product),
                    price=self.parse_price(product),
                    available=product.get('data-sku-status') == 'available'
                )
                results.append(p)
        return results

    @staticmethod
    def parse_name(item) -> str:
        return item.get('data-sku-name')

    @staticmethod
    def parse_price(item) -> float:
        return float(item.get('data-sku-price').replace(',', '.'))

