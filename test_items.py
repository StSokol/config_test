# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 19:41:23 2019

@author: sokol
"""
import time
from selenium import webdriver

def test_add_to_busket_button_is_present(browser):

    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)

    time.sleep(5)

    buttons = browser.find_elements_by_css_selector('button.btn-add-to-basket')
    assert len(buttons) > 0, "Не найдена кнопка 'Добавить в корзину'!"

