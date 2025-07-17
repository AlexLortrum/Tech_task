from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import logging
import os
import pytest

@pytest.fixture()
def driver():
    download_path = os.path.join(os.getcwd(), "tests")
    options = Options()
    options.set_preference("browser.download.dir", download_path)
    options.set_preference("browser.download.manager.showWhenStarting", False)
    options.set_preference("browser.download.folderList", 2)
    driver = webdriver.Firefox(options=options)
    driver.implicitly_wait(5)
    yield driver
    driver.close()
    driver.quit()