import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://habr.com/ru/feed/")
    page.get_by_role("link", name="Как стать автором").click()
    page.get_by_role("link", name="Написать публикацию").first.click()
    expect(page.get_by_text("Для просмотра этой страницы необходимо авторизоваться")).to_be_visible()
    expect(page.get_by_role("main")).to_contain_text("Для просмотра этой страницы необходимо авторизоваться")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
