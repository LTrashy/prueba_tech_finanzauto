import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

SELENIUM_URL = "http://selenium-chrome:4444/wd/hub"

@pytest.fixture
def driver():
    options = Options()
    # Si quieres forzar que se vea en noVNC, no agregues --headless
    driver = webdriver.Remote(command_executor=SELENIUM_URL, options=options)
    yield driver
    driver.quit()

@pytest.fixture
def wait(driver):
    return WebDriverWait(driver, 10)