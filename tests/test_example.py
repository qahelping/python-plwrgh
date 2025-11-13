import allure
import pytest
from axe_playwright_python.sync_playwright import Axe
from playwright.sync_api import Page, expect, Route

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
    assert_snapshot(page.screenshot(), "./__screenshots__/example.png")


@allure.title("Test Assert Snapshot for locator")
def test_snapshot2(page, assert_snapshot):
    assert_snapshot(page.locator('[class="hero hero--primary heroBanner_UJJx"]').screenshot(), "example.png")

@pytest.mark.console
@allure.title("Test ConsoleMessage")
def test_read_from_console(page):
    page.on("console", lambda msg: print(msg.text))

    page.on("console", lambda msg: print(f"error: {msg.text}") if msg.type == "error" else None)

    with page.expect_console_message() as msg_info:
        page.evaluate("console.log('hello', 42, { foo: 'bar' })")
    msg = msg_info.value

    msg.args[0].json_value()
    msg.args[1].json_value()


@pytest.mark.mock
@allure.title("Test mock")
def test_mock_the_fruit_api(page: Page):
    page.goto("https://demo.playwright.dev/api-mocking")

    page.wait_for_timeout(10000)

    def handle(route: Route):
        json = [{"name": "Strawberry", "id": 21}]
        # fulfill the route with the mock data
        route.fulfill(json=json)

    # Intercept the route to the fruit API
    page.route("*/**/api/v1/fruits", handle)

    # Go to the page
    page.goto("https://demo.playwright.dev/api-mocking")

    page.wait_for_timeout(10000)
    # Assert that the Strawberry fruit is visible
    expect(page.get_by_text("Strawberry")).to_be_visible()

@allure.title("Test Accessibility with Default Counts")
def test_accessibility_default_counts(page):
    axe_playwright = AxeHelper(Axe())
    axe_playwright.check_accessibility(page)


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
