from playwright.sync_api import Page, expect, Locator


class MainPage:
    def __init__(self, page):
        self.page = page

        self.python_locator: Locator = page.locator(
            '//*[@id="docusaurus_skipToContent_fallback"]/main/section[1]/div/div/div[1]/div/p[3]/a[3]')
        self.link: Locator = page.get_by_role("link", name="Community")

    def click_on_python_link(self):
        self.python_locator.wait_for()
        self.python_locator.click()

    def open(self):
        self.page.goto("https://playwright.dev/")

    def click_on_link_community(self):
        self.link.click()
