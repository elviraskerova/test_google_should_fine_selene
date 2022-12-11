from selene.support.shared import browser
from selene import have


def test_positive_search(open_browser):
    browser.element('[name=q]').type('selene').press_enter()
    browser.element('[id=search]').should(have.text('yashaka/selene: User-oriented Web UI browser tests in Python'))


def test_negative_search(open_browser):
    browser.element('[name=q]').type('hthbdgnhjfyukoytfgh').press_enter()
    browser.element('[class=card-section]').should(have.text('По запросу hthbdgnhjfyukoytfgh ничего не найдено.'))