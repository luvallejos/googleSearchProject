from selenium import webdriver


class Driver:

    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--lang=en-uk")
        self.instance = webdriver.Chrome(options=options)

    def navigate(self, url):
        self.instance.maximize_window()
        self.instance.get(url)
