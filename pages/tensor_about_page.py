from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from pages.base_page import Base_page
import logging

class Tensor_about_page(Base_page):
    working_images = (By.XPATH, '//div[@class="s-Grid-container"]//a//img')
    def __init__(self, driver, logger):
        super().__init__(driver, logger)

    def check_images_are_equal(self):
        try:
            images = self.find_elements(*self.working_images)
        except NoSuchElementException:
            logging.exception("Tensor_about_page.check_images_are_equal(): error")
            return 1
        
        first_image_height = int(images[0].get_attribute("height"))
        first_image_width = int(images[0].get_attribute("width"))
        for image in images[1:]:
            image_height = int(image.get_attribute("height"))
            image_width = int(image.get_attribute("width"))
            if first_image_height != image_height or first_image_width != image_width:
                return 1
        logging.info("Tensor_about_page.check_images_are_equal(): success")
        return 0
