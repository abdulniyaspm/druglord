from ..engines import GenericEngine
from ..models.product import Product
from typing import List


class Engine(GenericEngine):

    def search(self, term: str) -> List[Product]:
        results = []
        soup = self._get_soup(f'https://www.drogariaspacheco.com.br/{term}?')
        if soup is not None:
            headers = soup.find_all('div', attrs={
                'class': 'product-immage-and-flags'})
            for header in headers:
                info = header.next_sibling.next_sibling
                name = self.parse_name(header)
                price = self.parse_price(info)

                p = Product(
                    supplier='PACHECO',
                    name=name,
                    price=price,
                    available=True
                )
                results.append(p)
        return results

    @staticmethod
    def parse_name(item) -> str:
        return item.h3.text

    @staticmethod
    def parse_price(item) -> float:
        return float(item.find('span', attrs={
                    'class': 'the-price'}).text.split(' ')[1].replace(',', '.'))
