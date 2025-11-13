import re

import pytest
from playwright.sync_api import expect, Page

@pytest.mark.only
def test_todo(page: Page) -> None:
    page.goto("https://demo.playwright.dev/todomvc/#/")
    page.get_by_role("textbox", name="What needs to be done?").fill("купить хлеб")
    page.get_by_role("textbox", name="What needs to be done?").press("Enter")
    page.get_by_role("textbox", name="What needs to be done?").fill("сделать домашку")
    page.get_by_role("textbox", name="What needs to be done?").press("Enter")
    page.get_by_role("textbox", name="What needs to be done?").fill("купить подарок на др")
    page.get_by_role("textbox", name="What needs to be done?").press("Enter")
    expect(page.get_by_text("купить хлеб")).to_be_visible()
    expect(page.get_by_text("сделать домашку")).to_be_visible()
    expect(page.get_by_text("купить подарок на др")).to_be_visible()
    page.get_by_role("listitem").filter(has_text="купить хлеб").get_by_label("Toggle Todo").check()
    expect(page.get_by_text("купить хлеб")).to_be_visible()
    expect(page.locator("body")).to_contain_text("купить хлеб")
    expect(page.get_by_role("listitem").filter(has_text="сделать домашку").get_by_label("Toggle Todo")).not_to_be_checked()
    page.get_by_text("купить хлеб").click()
    expect(page.get_by_role("listitem").filter(has_text="купить подарок на др").get_by_label("Toggle Todo")).not_to_be_checked()
    page.get_by_role("listitem").filter(has_text="сделать домашку").get_by_label("Toggle Todo").check()
    page.get_by_role("listitem").filter(has_text="купить подарок на др").get_by_label("Toggle Todo").check()
    page.get_by_role("link", name="Active").click()
    expect(page.get_by_role("textbox", name="What needs to be done?")).to_be_visible()
    page.get_by_text("0 items leftAll Active").click()
