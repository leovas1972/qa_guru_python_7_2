from selene.support.shared import browser
from selene import be, have

def test_one():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('yashaka/selene: User-oriented Web UI browser tests in'))

def test_two():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('xxxrrruuulllsss').press_enter()
    browser.element("[id='result-stats']").should(have.text('Результатов: примерно 0'))