from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        base_url = "https://bonigarcia.dev/selenium-webdriver-java"
        self.url = base_url + "/slow-calculator.html"
        self.delay_input = (By.CSS_SELECTOR, "#delay")
        self.result_display = (By.CSS_SELECTOR, ".screen")
        self.buttons = {
            '7': (By.XPATH, "//span[text()='7']"),
            '8': (By.XPATH, "//span[text()='8']"),
            '+': (By.XPATH, "//span[text()='+']"),
            '=': (By.XPATH, "//span[text()='=']")
        }

    def open(self):
        self.driver.get(self.url)

    def set_delay(self, delay_value):
        delay_field = self.driver.find_element(*self.delay_input)
        delay_field.clear()
        delay_field.send_keys(str(delay_value))

    def click_button(self, button):
        button_element = self.driver.find_element(*self.buttons[button])
        button_element.click()

    def get_result(self, timeout=50):
        wait = WebDriverWait(self.driver, timeout)
        wait.until(
            lambda driver: driver.find_element(
                *self.result_display).text == "15"
        )
        return self.driver.find_element(*self.result_display).text
