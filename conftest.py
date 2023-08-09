import pytest
from selene.support.shared import browser
from selenium import webdriver

@pytest.fixture(scope='session', autouse=True)
def config_browser():
    driver = webdriver.Chrome()
    browser.config.driver = driver
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    yield
    browser.quit()