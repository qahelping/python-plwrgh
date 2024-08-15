from playwright.sync_api import Page, expect, Locator

from helpers.expects import Expects


class IntroPythonPage:

    def __init__(self, page):
        self.page: Page = page
        self.expect = Expects()

        self.link_header_python_locator: Locator = page.locator('[class="navbar__link"]')
        self.next_button_locator: Locator = page.locator('.pagination-nav__link.pagination-nav__link--next')

    def open(self):
        self.page.goto('https://playwright.dev/python/docs/intro')

    def click_on_next(self):
        self.next_button_locator.click()

    def assert_that_intro_page_is_visible(self):
        self.expect.expect_to_have_text(self.link_header_python_locator, 'Python')

        expect(self.page).to_have_url('https://playwright.dev/python/docs/writing-tests')
        expect(self.page).to_have_title('Writing tests | Playwright Python')
