from selene.support.shared import browser
import pytest


@pytest.fixture(scope="function", autouse=True)
def open_browser():
    browser.config.window_width = 1024
    browser.config.window_height = 768
    browser.open("https://google.com")


