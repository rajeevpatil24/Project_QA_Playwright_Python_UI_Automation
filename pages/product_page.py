from playwright.async_api import Page, TimeoutError
from utils.exceptions import LoginTimeoutException, ProductInteractionError


class ProductPage:
    def __init__(self, page: Page):
        self.page = page

    async def click_product_link(self, product_id: int):
        try:
            await self.page.click(f'a[href="/product_details/{product_id}"]')
        except TimeoutError:
            raise LoginTimeoutException("Timed out waiting for the 'View Cart' link after login.")
        except Exception as e:
            raise ProductInteractionError(f"Failed to click product link for ID {product_id}: {str(e)}")

    async def get_product_message(self):
        try:
            product_message = await self.page.inner_text('body')
            return product_message
        except TimeoutError:
            raise LoginTimeoutException("Timed out waiting for the 'View Cart' link after login.")
        except Exception as e:
            raise ProductInteractionError(f"Failed to get propduct message: {str(e)}")

    async def click_add_to_cart(self, product_id: int):
        try:
            await self.page.click(f'a[href="/add_to_cart/{product_id}"]')
        except TimeoutError:
            raise LoginTimeoutException("Timed out waiting for the 'Adding Cart' link after login.")
        except Exception as e:
            raise ProductInteractionError(f"Failed to click to add product  for {product_id}: {str(e)}")

    async def get_product_count(self):
        try:
            # Query all product list items and return the count
            product_elements = await self.page.query_selector_all('ul > li')

            return len(product_elements)
        except Exception as e:
            raise RuntimeError(f"Failed to get product count: {str(e)}")
