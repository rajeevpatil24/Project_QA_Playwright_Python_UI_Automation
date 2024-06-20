import logging

import pytest
from playwright.async_api import async_playwright
from pages.login_page import LoginPage
from config import config as conf

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@pytest.mark.parametrize("username, password, should_succeed", [
    (conf.VALID_USER, conf.VALID_PASSWORD, True),
    (conf.VALID_USER, conf.INVALID_PASSWORD, False),
    (conf.INVALID_USER, conf.VALID_USER, False)
])
async def test_login(username, password, should_succeed, page):
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch()
        page = await browser.new_page()
        login_page = LoginPage(page)

        await login_page.load()
        await login_page.login(username, password)

        if should_succeed:
            login_successful = await login_page.is_login_successful()
            if not login_successful:
                # Take screenshot on failure
                await page.screenshot(path=f'screenshots/{username}_login_failure.png')
            assert login_successful, "Login was expected to succeed, but it failed."
            logger.info("Login successful with valid credentials.")
        else:
            login_failed = await login_page.is_login_failed()
            if not login_failed:
                # Take screenshot on failure
                await page.screenshot(path=f'screenshots/{username}_login_failure.png')
            assert login_failed, "Login was expected to fail, but it succeeded."
            logger.info("Login failed with invalid credentials.")
