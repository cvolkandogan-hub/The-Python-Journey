# ============================================================
# DOSYA: basics/test_02_playwright_login.py
# AÇIKLAMA: First Playwright test - SauceDemo login automation
# Site: https://www.saucedemo.com (test için tasarlanmış demo site)
# ============================================================

import pytest
from playwright.sync_api import Page

def test_successful_login(page: Page):
    """Valid credentials should land on inventory page"""
    page.goto("https://www.saucedemo.com")
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")
    assert page.url == "https://www.saucedemo.com/inventory.html"

def test_wrong_password(page: Page):
    """Wrong password should show error message"""
    page.goto("https://www.saucedemo.com")
    page.fill("#user-name", "standard_user")
    page.fill("#password", "wrong_password")
    page.click("#login-button")
    error = page.locator(".error-message-container")
    assert error.is_visible()

def test_empty_credentials(page: Page):
    """Empty fields should show error message"""
    page.goto("https://www.saucedemo.com")
    page.click("#login-button")
    error = page.locator(".error-message-container")
    assert error.is_visible()

def test_wrong_url_on_login(page: Page):
    """This test was intentionally failed — To view a screenshot"""
    page.goto("https://www.saucedemo.com")
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")
    assert page.url == "https://www.saucedemo.com/YANLIS_SAYFA.html"