def test_find_add_to_card_btn(browser):
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    assert browser.find_element_by_class_name('btn-add-to-basket').is_displayed(), \
        'Error'
