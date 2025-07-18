from pages.main_page import Main_page
from pages.contacts_page import Contacts_page
from selenium.webdriver.common.by import By
import logging


def test_scenario2(driver):
    logger = logging.getLogger(__name__)
    logger.info("TEST_SCENARIO 2: START")
    main_page = Main_page(driver, logger)
    main_page.open_page()

    contacts = main_page.open_contacts()
    assert type(contacts) is Contacts_page

    region = contacts.get_region_title()
    assert region == "Ярославская обл."

    old_partners_city = contacts.get_partners_block().find_element(By.ID, "city-id-2").text
    assert old_partners_city != 1
    assert contacts.change_region("Камчатский край") == 0

    region = contacts.get_region_title()
    assert region == "Камчатский край"

    new_partners_city = contacts.get_partners_block().find_element(By.ID, "city-id-2").text
    assert new_partners_city != 1
    assert old_partners_city != new_partners_city
    assert contacts.get_title() == "Saby Контакты — Камчатский край"
    
    url = contacts.get_url()
    url_region = url.split("/")[-1].split("?")[0]
    assert url_region == "41-kamchatskij-kraj"
    logger.info("TEST_SCENARIO 2: END")



