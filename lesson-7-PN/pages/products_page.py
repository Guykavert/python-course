from selenium.webdriver.common.by import By


class ProductsPage:
    def __init__(self, driver):
        self.driver = driver
        self.product_add_buttons = {
            "Sauce Labs Backpack": (By.ID,
                                    "add-to-cart-sauce-labs-backpack"),
            "Sauce Labs Bolt T-Shirt": (By.ID,
                                        "add-to-cart-sauce-labs-bolt-t-shirt"),
            "Sauce Labs Onesie": (By.ID,
                                  "add-to-cart-sauce-labs-onesie")
        }
        self.cart_button = (By.CLASS_NAME, "shopping_cart_link")

    def add_product_to_cart(self, product_name):
        button_locator = self.product_add_buttons[product_name]
        add_button = self.driver.find_element(*button_locator)
        add_button.click()

    def go_to_cart(self):
        self.driver.find_element(*self.cart_button).click()
