from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import Base_page
from pages.contacts_page import Contacts_page
from pages.download_page import Download_page
import logging


class Main_page(Base_page):
    download_element = (By.XPATH, "//a[@href='/download']")
    def __init__(self, driver, logger):
        super().__init__(driver, logger)

    def open_contacts(self):
        try:
            self.navigate_to("contacts")
            self.logger.info("Main_page.open_contacts(): success")
            return Contacts_page(self.driver, self.logger)
        except:
            self.logger.exception("Main_page.open_contacts(): error")
            return 1

    def open_download(self):
        try:
            self.wait.until_not(EC.presence_of_element_located(self.preload_block))
            self.find_element(*self.download_element).click()
            self.logger.info("Main_page.open_download(): success")
            return Download_page(self.driver, self.logger)
        except:
            self.logger.exception("Main_page.open_download(): error")
            return 1