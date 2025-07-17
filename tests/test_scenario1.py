from pages.main_page import Main_page
from pages.contacts_page import Contacts_page
from pages.tensor_page import Tensor_page
from pages.tensor_about_page import Tensor_about_page
import logging
import os


def test_scenario1(driver):
    logger = logging.getLogger(__name__)
    logger.info("TEST_SCENARIO 1: START")
    main_page = Main_page(driver, logger)
    main_page.open_page()
    contacts = main_page.open_contacts()
    assert type(contacts) is Contacts_page
    tensor_main = contacts.click_tensor_logo()
    assert type(tensor_main) is Tensor_page
    driver.switch_to.window(driver.window_handles[1])
    block = tensor_main.check_block()
    assert block == 0
    about = tensor_main.click_about_elem()
    assert type(about) is Tensor_about_page
    images = about.check_images_are_equal()
    assert images == 0
    logger.info("TEST_SCENARIO 1: END")
