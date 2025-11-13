import re
import time

from playwright.sync_api import Playwright, sync_playwright, expect


import json
import time

from playwright.sync_api import sync_playwright, Route, Page, expect

playwright = sync_playwright().start()
device = playwright.devices["iPhone 14"]
browser = playwright.chromium.launch(headless=False)
context = browser.new_context(**device)
page = context.new_page()

page.goto("https://playwright.dev/python/docs/api/class-browsercontext")

expect(page).to_have_title("BrowserContext | Playwright Python")

context.close()
browser.close()

