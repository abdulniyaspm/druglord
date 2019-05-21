# Drug Lord

## Simple web scraping system to find best prices for medicines in Brazilian drugstores.

### Requirements
You **MUST** download [Chrome webdriver](https://sites.google.com/a/chromium.org/chromedriver/downloads) for working with DrugLord.

If you want to implement your solution for another browser, find a suitable webdriver for your favorite browser below:

| Browser | Driver |
|:--:|:--|
| Chrome | [https://sites.google.com/a/chromium.org/chromedriver/downloads](https://sites.google.com/a/chromium.org/chromedriver/downloads) |
| Firefox | [https://github.com/mozilla/geckodriver/releases](https://github.com/mozilla/geckodriver/releases) |
| Safari | [https://webkit.org/blog/6900/webdriver-support-in-safari-10/](https://webkit.org/blog/6900/webdriver-support-in-safari-10/) |

After downloading your driver, extract the contents to any folder and make sure to add your webdriver to your computer **PATH**

**PS:** Windows users may have to restart the computer after adding the webdriver to **PATH**

**PPS:** If you need a headless environment, you must use Chrome webdriver

---

### Installation
It's as simple as installing any other pip package
```bash
$ pip install druglord
```
### Usage
Example:
Create a new project:
```bash
$ mkdir druglord_test
$ cd druglord_test
$ python -m venv venv
$ . ./venv/Scripts/activate
```
Create a new file named *search.py* and add the following contents:
```python
import sys
from druglord import DrugLord
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
```
From command-line, you can search for a medicine:
```bash
$ python search.py tylex
```
You can also search using multiple words:
```bash
$ python search.py "Vallium 10mg"
```
---

## Todo (Help wanted)
 - Add more tests
 - Add more drugstores
 - Traverse multiple page results
 - i18n
 - Use lxml for faster results
 - Machine learning to identify and group similar products