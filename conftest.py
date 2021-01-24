# -*- coding: utf-8 -*-
import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help='Choose browser: chrome or firefox')
    parser.addoption('--language', default='ru',
                     help='Choose web store language')


@pytest.fixture()
def browser(request):
    browser_name = request.config.getoption('browser_name')
    browser = None
    if browser_name == 'chrome':
        browser = webdriver.Chrome()
    elif browser_name == 'firefox':
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError('--browser_name should be chrome or firefox')
    yield browser
    browser.quit()


@pytest.fixture()
def language(request):
    yield request.config.getoption('language')
