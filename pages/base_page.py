from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import logging

class Base_page:
    def __init__(self, driver, logger, url="https://saby.ru/"):
        self.driver = driver
        self.base_url = url
        self.wait = WebDriverWait(driver, 3)
        self.preload_block = (By.XPATH, "//div[@class='preload-overlay']")
        self.logger = logger

    def find_element(self, *locator):
        return self.driver.find_element(*locator)
    
    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def navigate_to(self, url):
        return self.driver.get(self.base_url + url)

    def get_title(self):
        return self.driver.title

    def get_url(self):
        return self.driver.current_url

    def open_page(self):
        return self.driver.get(self.base_url)
