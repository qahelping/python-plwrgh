import re
import time

import pytest
from playwright.sync_api import Page, expect, BrowserContext


def test_main1(page: Page):
    page.goto('https://playwright.dev/python/docs/intro')
    time.sleep(5)
    expect(page).to_have_title(re.compile("Playwright"))


def test_playwright_python(page: Page, context: BrowserContext):
    page.goto('https://playwright.dev')
    page.get_by_role("link", name="Playwright: Fast and reliable").click()
    page.get_by_label("Main", exact=True).get_by_role("link", name="Python").click()
    lst = context.pages
    print(lst)
    expect(page.get_by_role("link", name="Playwright logo Playwright")).to_be_visible()
