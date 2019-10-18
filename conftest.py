# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 18:35:30 2019

@author: sokol
"""
import pytest
from selenium import webdriver

from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='en',
                     help="Choose language: en,ru,de....ua...")

@pytest.fixture(scope='module')
def browser(request):
    browser_name = request.config.getoption('browser_name')
    user_language = request.config.getoption('language')
    drv = None
    if browser_name == 'chrome':
        print('\nЗапуск драйвера Chrome...')

        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        drv = webdriver.Chrome(options=options)

    elif browser_name == 'firefox':
        print('\nЗапуск драйвера FireFox...')
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        drv = webdriver.Firefox(firefox_profile=fp)

    else:
        raise pytest.UsageError('Browser_name should be chrome or firefox')

    drv.implicitly_wait(5)
    yield drv

    print('\nГасим драйвер...')
    drv.quit()

