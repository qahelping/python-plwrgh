import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://playwright.dev/")
    page.get_by_role("link", name="Community").click()
    expect(page.get_by_role("heading", name="Welcome")).to_be_visible()

    page2 = context.new_page()
    page2.goto("https://playwright.dev/python/docs/api/class-browsercontext")
    count = context.pages

    cookies = {'name': 'value'}
    context.add_cookies([cookies])
    context.clear_cookies()
    print(count)
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
