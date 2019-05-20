import atexit
from selenium import webdriver
from druglord.config import Config


class Browser:
    def __init__(self, browser):
        self.browser = browser
        self.browser.implicitly_wait(Config.SELENIUM_IMPLICIT_WAIT)
        atexit.register(self.quit)

    @property
    def page_source(self):
        source = self.browser.page_source
        return source

    def get(self, url) -> 'Browser':
        self.browser.get(url)
        return self

    def quit(self):
        self.browser.quit()


class Chrome(Browser):
    def __init__(self, headless: bool = True):
        options = webdriver.ChromeOptions()
        if headless:
            options.add_argument('headless')
        super(Chrome, self).__init__(webdriver.Chrome(options=options))


class Firefox(Browser):
    def __init__(self):
        super(Firefox, self).__init__(webdriver.Firefox())


class Safari(Browser):
    def __init__(self):
        super(Safari, self).__init__(webdriver.Safari())
