import os

import pytest
from selenium import webdriver


def pytest_addoption(parser):
    return parser.addoption('--browser')


@pytest.fixture()
def browser(request):
    return request.config.getoption('--browser')


# Exclude JAVA_HOME or any other environment variable
@pytest.hookimpl(tryfirst=True)
def pytest_configure():
    if "JAVA_HOME" in os.environ:
        del os.environ["JAVA_HOME"]


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    elif browser == 'edge':
        driver = webdriver.Edge()
    else:
        raise RuntimeError("Unsupported Browser")
    return driver
