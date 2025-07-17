from selenium.webdriver.common.by import By
from pages.base_page import Base_page
import logging

class Download_page(Base_page):
    web_installer = (By.XPATH, '//a[@href="https://update.saby.ru/SabyDesktop/master/win32/saby-setup-web.exe"]')
    def __init__(self, driver, logger):
        super().__init__(driver, logger)

    def download_web_installer(self):
        try:
            self.find_element(*self.web_installer).click()
            logging.info("Download_page.download_web_installer(): success")
            return 0
        except:
            logging.exception("Download_page.download_web_installer(): error")
            return 1

    def get_web_installer_name(self):
        element = self.find_element(*self.web_installer).get_attribute("href")
        logging.info("Download_page.get_web_installer_name(): success")
        return element.split('/')[-1]

    def get_web_installer_size(self):
        text = self.find_element(*self.web_installer).text
        text = text.split(" ")[2:]
        text[1] = text[1].replace(")", "")
        logging.info("Download_page.get_web_installer_size(): success")
        return text
