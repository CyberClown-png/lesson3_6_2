import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="ru",
                     help="Choose language: es or ru etc")


@pytest.fixture(scope="function")
def browser(request):
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    language = request.config.getoption("language")
    yield browser
    print("\nquit browser..")
    browser.quit()
