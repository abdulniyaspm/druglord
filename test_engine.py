import sys
from druglord.browser import Chrome
from druglord.engines.pagmenos import Engine

b = Chrome(headless=False)
e = Engine(b)
for product in e.search(sys.argv[1]):
    print(product.name, product.price)
