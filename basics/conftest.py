# ============================================================
# DOSYA: conftest.py
# AÇIKLAMA: Playwright global ayarlar - otomatik screenshot
# ============================================================

import pytest
import os

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "viewport": {"width": 1280, "height": 720}
    }

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")
        if page:
            os.makedirs("reports/screenshots", exist_ok=True)
            screenshot_path = f"reports/screenshots/{item.name}.png"
            page.screenshot(path=screenshot_path)
            print(f"\n📸 Screenshot kaydedildi: {screenshot_path}")