from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from pages.base_page import Base_page
from pages.tensor_page import Tensor_page
import logging

class Contacts_page(Base_page):
    tensor_logo = (By.XPATH, "//a[@href='https://tensor.ru/']")
    partners_block = (By.XPATH, "//div[@name='itemsContainer']")
    region_chooser_text = (By.XPATH, "//span[@class='sbis_ru-Region-Chooser__text sbis_ru-link']")
    def __init__(self, driver, logger):
        super().__init__(driver, logger)

    def get_partners_block(self):
        try:
            element = self.find_element(*self.partners_block)
            self.logger.info("Contacts_page.get_partners_block(): success")
            return element
        except NoSuchElementException:
            self.logger.exception("Contacts_page.get_partners_block(): error")
            return 1

    def get_region_title(self):
        try:
            element = self.find_element(*self.region_chooser_text).text 
            self.logger.info("Contacts_page.get_region_title(): success")
            return element
        except NoSuchElementException:
            self.logger.exception("Contacts_page.get_region_title(): error")
            return 1

    def change_region(self, region):
        try:
            self.wait.until_not(EC.presence_of_element_located(self.preload_block))
            self.find_element(*self.region_chooser_text).click()
            new_region = (By.XPATH, f"//span[@title='{region}']")
            self.wait.until_not(EC.presence_of_element_located(self.preload_block))
            self.find_element(*new_region).click()
            self.logger.info("Contacts_page.change_region(): success")
            return 0
        except:
            self.logger.exception("Contacts_page.change_region(): error")
            return 1


    def click_tensor_logo(self):
        try:
            self.wait.until_not(EC.presence_of_element_located(self.preload_block))
            self.find_element(*self.tensor_logo).click()
            self.logger.info("Contacts_page.click_tensor_logo(): success")
            return Tensor_page(self.driver, self.logger)
        except NoSuchElementException:
            self.logger.exception("Contacts_page.click_tensor_logo(): error")
            return 1
