import pytest
from playwright.sync_api import Page, expect

from pages.main_page import IntroPythonPage
from pages.python_intro_page import MainPage


@pytest.fixture(scope="function", autouse=True)
def before_each_after_each(page: Page):
    print("beforeEach")
    page.goto("https://playwright.dev/")
    yield
    print("afterEach")


def test_browser_context_args(page):
    main_page = MainPage(page)
    main_page.click_on_python_link()

    intro_page = IntroPythonPage(page)
    intro_page.assert_that_intro_page_is_visible()

def test_browser_context_args2(page):
    main_page = MainPage(page)
    main_page.click_on_python_link()

    intro_page = IntroPythonPage(page)
    intro_page.click_on_next()
    intro_page.assert_that_intro_page_is_visible()