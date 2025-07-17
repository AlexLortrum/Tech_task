from pages.main_page import Main_page
from pages.download_page import Download_page
import os 
import logging
from time import sleep

def test_scenario3(driver):
    logger = logging.getLogger(__name__)
    logger.info("TEST_SCENARIO 3: START")
    size_aliases = {
        "КБ": 1,
        "МБ": 2,
        "ГБ": 3
    }
    
    main_page = Main_page(driver, logger)
    main_page.open_page()
    download = main_page.open_download()
    assert type(download) is Download_page

    filename = download.get_web_installer_name()
    assert download.download_web_installer() == 0

    filepath = os.path.join("tests", filename)
    web_installer_size = download.get_web_installer_size()

    timeout = 30
    while not os.path.exists(filepath):
        sleep(1)
        timeout -= 1
        if timeout == 0:
            print("times out")
            return 1
    
    file_size = os.path.getsize(filepath)
    for i in range(size_aliases[web_installer_size[1]]):
        file_size = file_size/1024
    assert round(file_size, 2) == float(web_installer_size[0])
    logger.info("TEST_SCENARIO 3: END")

