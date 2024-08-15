import allure
import pytest
from axe_playwright_python.sync_playwright import Axe
from playwright.sync_api import Page

from helpers.axe import AxeHelper
from pages.community_page import CommunityPage
from pages.main_page import MainPage
from pages.python_intro_page import IntroPythonPage


@pytest.fixture(scope="function", autouse=True)
def before_each_after_each(page: Page):
    print("beforeEach")
    page.goto("https://playwright.dev/")
    yield
    print("afterEach")


def test_browser_context_args(page):
    intro_page = IntroPythonPage(page)
    intro_page.open()
    intro_page.assert_that_intro_page_is_visible()


def test_browser_context_args2(page):
    intro_page = IntroPythonPage(page)
    intro_page.open()
    intro_page.click_on_next()
    intro_page.assert_that_intro_page_is_visible()


def test_page_object(page):
    main_page = MainPage(page)
    main_page.open()
    main_page.click_on_link_community()

    community = CommunityPage(page)
    community.expect_that_visible()


@allure.title("Test Assert Snapshot for page")
def test_snapshot1(page, assert_snapshot):
    assert_snapshot(page.screenshot(), "./__screenshots__/eexample.png")


@pytest.mark.only
@allure.title("Test Assert Snapshot for locator")
def test_snapshot2(page, assert_snapshot):
    assert_snapshot(page.locator('[class="hero hero--primary heroBanner_UJJx"]').screenshot(), "example.png")

@pytest.mark.only
@allure.title("Test Accessibility with Default Counts")
def test_accessibility_default_counts(page):
    axe_playwright = AxeHelper(Axe())
    axe_playwright.check_accessibility(page)

@pytest.mark.only
@allure.title("Test Accessibility with Custom Counts")
def test_accessibility_custom_counts(page):
    axe_playwright = AxeHelper(Axe())
    axe_playwright.check_accessibility(
        page,
        maximum_allowed_violations_by_impact={
            "minor": 2,
            "moderate": 5,
            "serious": 0,
            "critical": 0,
        },
    )
