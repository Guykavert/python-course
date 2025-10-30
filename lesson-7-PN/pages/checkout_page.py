from selenium.webdriver.common.by import By


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.first_name_input = (By.ID, "first-name")
        self.last_name_input = (By.ID, "last-name")
        self.postal_code_input = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.total_amount = (By.CLASS_NAME, "summary_total_label")
        self.finish_button = (By.ID, "finish")

    def fill_checkout_info(self, first_name, last_name, postal_code):
        self.driver.find_element(*self.first_name_input).send_keys(first_name)
        self.driver.find_element(*self.last_name_input).send_keys(last_name)
        postal_elem = self.driver.find_element(*self.postal_code_input)
        postal_elem.send_keys(postal_code)
        self.driver.find_element(*self.continue_button).click()

    def get_total_amount(self):
        total_text = self.driver.find_element(*self.total_amount).text
        return total_text

    def finish_checkout(self):
        self.driver.find_element(*self.finish_button).click()
