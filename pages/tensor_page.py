from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from pages.base_page import Base_page
from pages.tensor_about_page import Tensor_about_page
from selenium.webdriver.support import expected_conditions as EC
import logging


class Tensor_page(Base_page):
    strength_in_people_block = (By.XPATH, '//p[text()[contains(.,"Сила в людях")]]/..')
    strength_in_people_about = (By.XPATH, strength_in_people_block[1]+'//a[@href="/about"]')
    def __init__(self, driver, logger):
        super().__init__(driver, logger)

    def check_block(self):
        try:
            self.find_element(*self.strength_in_people_block)
            self.logger.info("Tensor_page.check_block(): success")
            return 0
        except NoSuchElementException:
            self.logger.exception("Tensor_page.check_block(): error")
            return 1 

    def click_about_elem(self):
        try:
            self.wait.until_not(EC.presence_of_element_located(self.preload_block))
            self.find_element(*self.strength_in_people_about).click()
            self.logger.info("Tensor_page.click_about_elem(): success")
            return Tensor_about_page(self.driver, self.logger)
        except:
            self.logger.exception("Tensor_page.click_about_elem(): error")
            return 1
