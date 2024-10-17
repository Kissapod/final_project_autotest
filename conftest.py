import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def pytest_addoption(parser):
    parser.addoption(
        "--language", action="store", default="en", help="Choose language: en, ru, etc."
    )

@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    if language is None:
        raise pytest.UsageError("--language parameter must be provided")

    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    browser = webdriver.Chrome(options=options)

    yield browser
    browser.quit()
