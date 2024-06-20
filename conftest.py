import pytest
from playwright.async_api import async_playwright
from config import config as conf


@pytest.fixture(scope="session")
def event_loop():
    import asyncio
    loop = asyncio.get_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="session")
async def browser():
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch()
        yield browser
        await browser.close()


@pytest.fixture
async def page(browser):
    page = await browser.new_page()
    yield page
    await page.close()


@pytest.fixture
async def login_page(login_page):
    username = conf.VALID_USER
    password = conf.VALID_PASSWORD

    # Perform login
    await login_page.load()
    await login_page.login(username, password)

    # Check if login was successful
    login_successful = await login_page.is_login_successful()
    assert login_successful, "Login was expected to succeed, but it failed."
    return login_page
