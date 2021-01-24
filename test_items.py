# -*- coding: utf-8 -*-

LINK = 'http://selenium1py.pythonanywhere.com/{}/catalogue/coders-at-work_207/'


def test_items(browser, language):
    browser.get(LINK.format(language))
    assert browser.find_element_by_class_name('btn-add-to-basket').is_displayed(),\
        'Кнопка подобаления товара в корзину не отображается на стрнице'
