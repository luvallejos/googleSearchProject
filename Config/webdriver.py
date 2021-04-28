from selenium import webdriver


class Driver:

    def __init__(self):
        self.instance = webdriver.Chrome()

    def navigate(self, url):
        self.instance.maximize_window()
        self.instance.get(url)
