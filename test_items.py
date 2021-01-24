# -*- coding: utf-8 -*-

LINK = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_add_to_basket_button(browser):
    browser.get(LINK)
    assert browser.find_element_by_class_name('btn-add-to-basket').is_displayed(),\
        'Кнопка добаления товара в корзину не отображается на стрнице'
