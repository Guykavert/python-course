from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


class TestSauceDemo:
    def test_complete_purchase_flow(self, driver):
        login_page = LoginPage(driver)
        products_page = ProductsPage(driver)
        cart_page = CartPage(driver)
        checkout_page = CheckoutPage(driver)

        login_page.open()
        login_page.login("standard_user", "secret_sauce")

        products_page.add_product_to_cart("Sauce Labs Backpack")
        products_page.add_product_to_cart("Sauce Labs Bolt T-Shirt")
        products_page.add_product_to_cart("Sauce Labs Onesie")

        products_page.go_to_cart()
        cart_page.proceed_to_checkout()
        checkout_page.fill_checkout_info("John", "Doe", "12345")

        total_text = checkout_page.get_total_amount()
        assert "58.29" in total_text, f"Expected $58.29, but got {total_text}"
