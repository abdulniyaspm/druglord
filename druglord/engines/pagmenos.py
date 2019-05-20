from ..engines import GenericEngine
from ..models.product import Product
from typing import List


class Engine(GenericEngine):

    def search(self, term: str) -> List[Product]:
        results = []
        soup = self._get_soup(
            f'https://busca.paguemenos.com.br/search/?query={term}')

        if soup is not None:
            products = soup.find_all('article', attrs={
                'class': 'biggy-product-card'})
            for product in products:
                p = Product(
                    supplier='PAGMENOS',
                    name=self.parse_name(product),
                    price=self.parse_price(product),
                    available=True
                )
                results.append(p)
        return results

    @staticmethod
    def parse_name(item) -> str:
        return item.find('p', attrs={
            'class': 'biggy-product-card__name'
        }).text.strip()

    @staticmethod
    def parse_price(item) -> float:
        pees = item.find_all('p', attrs={
                    'class': 'biggy-product-card__price'
        })
        if len(pees) > 1:
            return float(pees[1].text.strip().split(' ')[1].replace(',', '.'))
        return float(pees[0].text.strip().split(' ')[1].replace(',', '.'))
