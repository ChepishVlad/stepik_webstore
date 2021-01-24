# -*- coding: utf-8 -*-


def test_items(browser, language):
    browser.get(f'http://selenium1py.pythonanywhere.com/{language}/catalogue/coders-at-work_207/')

    assert browser.find_element_by_class_name('btn-add-to-basket').is_displayed(),\
        'Кнопка подобаления товара в корзину не отображается на стрнице'
