# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 19:41:23 2019

@author: sokol
"""
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_items_are_in_busket(browser):

    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)

    arr=browser.find_elements_by_css_selector('button.btn-add-to-basket')
    assert len(arr) > 0, "Не найдена кнопка 'Добавить в корзину'!"
    assert len(arr) == 1, "Должна быть только одна кнопка 'Добавить в корзину'!"

