import logging

import pytest
from playwright.async_api import async_playwright
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from config import config as conf

logging.basicConfig(level=logging.INFO)


@pytest.mark.asyncio
async def test_product_interaction():
    logging.info("Starting test_product_interaction...")
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch()
        page = await browser.new_page()

        # Perform login
        login_page = LoginPage(page)
        await login_page.load()
        await login_page.login(conf.VALID_USER, conf.VALID_PASSWORD)

        try:
            # Example: Initialize ProductPage using page
            product_page = ProductPage(page)

            # Navigate to product listing page
            await login_page.navigate_to_product_listing()

            # Get the count of products
            products = await product_page.get_product_count()
            logging.info(f"Found {products} products.")

            # Iterate over each product
            for i in range(1, products + 1):
                # Click on the product link
                logging.info(f"Processing product {i}...")
                await product_page.click_product_link(i)
                logging.info(f"Clicked on product {i} link.")
                # Capture screenshot after clicking on the product link
                await page.screenshot(path=f'screenshots/product_{i}_click.png')

                # Check the product message
                product_message = await product_page.get_product_message()
                assert f"This is product {i}." in product_message, f"Expected product {i} message not found."
                logging.info(f"Verified product {i} message: '{product_message}'")

                # Capture screenshot after verifying product message
                await page.screenshot(path=f'screenshots/product_{i}_message.png')

                # Click on Add to Cart for the current product
                await product_page.click_add_to_cart(i)
                logging.info(f"Clicked Add to Cart for product {i}.")

                # Capture screenshot after clicking on Add to Cart
                await page.screenshot(path=f'screenshots/product_{i}_add_to_cart.png')

        except Exception as e:
            # Capture screenshot on failure
            await page.screenshot(path=f'screenshots/test_failure.png')
            pytest.fail(f"Test execution failed: {str(e)}")

        finally:
            # Close the browser and cleanup
            await browser.close()
            logging.info("Browser closed.")
    logging.info("Finished test_product_interaction.")
