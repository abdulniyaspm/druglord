# Drug Lord

## Simple web scraping system to find best prices for (legal) drugs in Brazilian drugstores.

### Requirements
You **MUST** download at least one webdriver for working with Selenium. Default is Chrome.

You can find a suitable webdriver for your favorite browser below:

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
As simple as installing any other pip package

```bash
$ pip install druglord
```

### Usage
From command-line, you can search for a drug:

```bash
$ python druglord.py tylex
```

You can also search using multiple words:

```bash
$ python druglord.py "Vallium 10mg"
```

---

## Todo (Help wanted)
 - Add to PiPY
 - Add more tests
 - Traverse multiple page results
 - Use lxml for faster results
 - Group products by name if similar