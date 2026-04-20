# ============================================================
# DOSYA: tests/test_03_pom_login.py
# AÇIKLAMA: POM kullanarak yazılmış login testleri
# Testler artık "ne yapıldığını" anlatıyor, "nasıl" değil
# ============================================================

import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage


@pytest.fixture
def login_page(page: Page):
    """Her test için LoginPage hazırla ve siteye git"""
    lp = LoginPage(page)
    lp.navigate()
    return lp


def test_successful_login(login_page):
    """Doğru bilgilerle giriş başarılı olmalı"""
    login_page.login("standard_user", "secret_sauce")
    assert login_page.is_login_successful()


def test_wrong_password(login_page):
    """Yanlış şifre hata mesajı göstermeli"""
    login_page.login("standard_user", "wrong_password")
    assert login_page.get_error_message().is_visible()


def test_empty_credentials(login_page):
    """Boş bilgilerle giriş hata mesajı göstermeli"""
    login_page.login("", "")
    assert login_page.get_error_message().is_visible()


def test_locked_user(login_page):
    """Kilitli kullanıcı giriş yapamamalı"""
    login_page.login("locked_out_user", "secret_sauce")
    assert login_page.get_error_message().is_visible()