link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207//"


def test_guest_should_see_button_add(browser):
    browser.get(f"http://selenium1py.pythonanywhere.com/{browser.language}/catalogue/coders-at-work_207//")
    browser.implicitly_wait(5)
    button = browser.find_element_by_class_name("btn-add-to-basket")
