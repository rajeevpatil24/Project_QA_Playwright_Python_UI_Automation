import logging

from playwright.async_api import Page, TimeoutError
from utils.exceptions import LoginFailedException, LoginSuccessException, LoginTimeoutException
from config.config import BASE_URL as base_url

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class LoginPage:
    def __init__(self, page: Page):
        self.page = page

    async def load(self):
        logger.info(f"Loading login page: {base_url}")
        await self.page.goto(f"{base_url}login")

    async def login(self, username: str, password: str):
        logger.info(f"Logging in with username: {username}")
        await self.page.fill('input[name="username"]', username)
        await self.page.fill('input[name="password"]', password)
        await self.page.click('button[type="submit"]')

    async def is_login_successful(self):
        try:
            await self.page.wait_for_selector('a[href="/view_cart"]', timeout=5000)
            logger.info("Login successful")
            return True
        except TimeoutError:
            raise LoginTimeoutException("Timed out waiting for the 'View Cart' link after login.")
        except Exception as e:
            raise LoginSuccessException(f"Login was expected to succeed, but failed due to an unexpected error: {e}")

    async def is_login_failed(self):
        try:
            await self.page.wait_for_selector('text="Invalid credentials. Please try again."', timeout=5000)
            logger.info("Login failed due to invalid credentials")
            return True
        except TimeoutError:
            raise LoginTimeoutException("Timed out waiting for the invalid credentials error message.")
        except Exception as e:
            raise LoginFailedException(f"Login was expected to fail, but an unexpected error occurred: {e}")

    async def navigate_to_product_listing(self):
        try:
            await self.page.goto(f"{base_url}product_listing", timeout=5000)
            logger.info("Login failed due to invalid credentials")
            return True
        except TimeoutError:
            raise LoginTimeoutException("Timed out waiting for the 'View Cart' link after login.")
        except Exception as e:
            raise LoginSuccessException(f"Login was expected to succeed, but failed due to an unexpected error: {e}")
