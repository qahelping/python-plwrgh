from typing import Dict

import allure
import pytest
import requests
from _pytest.fixtures import FixtureRequest
from _pytest.nodes import Item
from playwright.sync_api import Page, Playwright
@pytest.fixture(autouse=True)
def attach_playwright_results(page: Page, request: FixtureRequest):
    """Fixture to perform teardown actions and attach results to Allure report
    on failure.

    Args:
        page (Page): Playwright page object.
        request: Pytest request object.
    """
    yield
    if request.node.rep_call.failed:
        allure.attach(
            body=page.url,
            name="URL",
            attachment_type=allure.attachment_type.URI_LIST,
        )
        allure.attach(
            page.screenshot(full_page=True),
            name="Screen shot on failure",
            attachment_type=allure.attachment_type.PNG,
        )


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item: Item):
    """Hook implementation to generate test report for each test phase.

    Args:
        item: Pytest item object.

    Yields:
        Outcome of the test execution.
    """
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)