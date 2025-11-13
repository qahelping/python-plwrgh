from typing import Dict, Any

import allure
import pytest
import requests
from _pytest.fixtures import FixtureRequest
from _pytest.nodes import Item
from axe_playwright_python.sync_playwright import Axe
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


# @pytest.fixture
# def browser_context_args(
#     browser_context_args: Dict,
#     locale: str,
#     project: str,
#     build,
#     playwright,
#     pytestconfig,
#     base_url,
# ) -> Dict[str, Any]:
#     def _accept_language(loc: str) -> str:
#         lang = loc.split("-")[0]
#         return f"{loc},{lang};q=0.9,en-US;q=0.8,en;q=0.7"
#
#     context = {
#         **browser_context_args,
#         "locale": locale,
#         "ignore_https_errors": True,
#         "extra_http_headers": {
#             **(browser_context_args.get("extra_http_headers") or {}),
#             "Accept-Language": _accept_language(locale),
#         },
#         "base_url": base_url,
#     }
#     context.update(playwright.devices["Pixel 5"])
#     return context