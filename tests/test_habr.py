import time

URL = 'https://habr.com/ru/feed/'

from playwright.sync_api import Page, expect

def test_habr(page: Page):
    page.goto(URL)

    selector = '[id="adfox_169815559787254866"]'
    expect(page.locator(selector)).to_be_visible()

    page.get_by_role("link", name="Как стать автором").click()
    page.get_by_role("link", name="Написать публикацию").first.click()
    expect(page.get_by_text("Для просмотра этой страницы необходимо авторизоваться")).to_be_visible()
    expect(page.get_by_role("main")).to_contain_text("Для просмотра этой страницы необходимо авторизоваться")








