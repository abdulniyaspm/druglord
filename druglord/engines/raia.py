from ..engines import GenericEngine
from ..models.product import Product
from typing import List


class Engine(GenericEngine):

    def search(self, term: str) -> List[Product]:
        results = []
        soup = self._get_soup(f'https://busca.drogaraia.com.br/search?w={term}')
        if soup is not None:
            grid = soup.find('ul', attrs={'class': 'products-grid'})
            items = grid.find_all('li', attrs={
                'class': 'item', 'data-tb-sid': 'st_result-container-wrapper'})
            for item in items:
                out_of_stock = item.find(
                    'button', attrs={'class': 'out-of-stock'})
                if out_of_stock is None:
                    p = Product(
                        supplier='RAIA',
                        name=self.parse_name(item),
                        price=self.parse_price(item),
                        available=True
                    )
                    results.append(p)
        return results

    @staticmethod
    def parse_name(item) -> str:
        name = item.find(
            'a', attrs={'data-tb-sid': 'st_title-link'}).text.strip()
        qtd = item.find(
            'li', attrs={'class': 'quantidade show-hover'}).text
        return f'{name} {qtd}'

    @staticmethod
    def parse_price(item) -> float:
        unique_price = item.find(
            'p', attrs={'class': 'unique-price'})

        if unique_price is None:
            price = item.find(
                'span', attrs={'class': 'price-text'}).text
        else:
            price = unique_price.text.replace(
                'preço unitário: R$', '')
        return float(price.replace(',', '.'))
