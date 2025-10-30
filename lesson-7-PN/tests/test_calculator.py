from pages.calculator_page import CalculatorPage


class TestCalculator:
    def test_calculator_with_delay(self, driver):
        calculator_page = CalculatorPage(driver)

        calculator_page.open()
        calculator_page.set_delay(45)
        calculator_page.click_button('7')
        calculator_page.click_button('+')
        calculator_page.click_button('8')
        calculator_page.click_button('=')

        result = calculator_page.get_result(timeout=50)
        expected = "15"
        assert result == expected, f"Expected '{expected}', but got '{result}'"
