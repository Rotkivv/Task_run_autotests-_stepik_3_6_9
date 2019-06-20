import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_product_page_contains_a_add_to_cart_button(browser):
    browser.get(link)
    browser.find_element_by_css_selector(".btn-add-to-basket")