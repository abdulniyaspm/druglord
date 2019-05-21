import sys
from druglord.app import DrugLord
from druglord.browser import Chrome as Browser


if __name__ == '__main__':
    browser = Browser()
    dl = DrugLord(browser)
    term = sys.argv[1]
    print()

    results = dl.search(term).order_by('price').results

    for product in results:
        if product.available:
            print(f'{product.supplier[:9]: <10}', end='')
            print(f'{product.name[:89]: <90}R$ ', end='')
            print(f'{product.price: >7.2f}')

    print(f'\n{len(results)} produtos encontrados '
          f'em {dl.search_time:.2f} segundos')
