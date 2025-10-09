from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options

import time


def main():
    firefox_options = Options()

    driver = webdriver.Firefox(options=firefox_options)

    try:
        driver.get("http://the-internet.herokuapp.com/inputs")

        wait = WebDriverWait(driver, 10)
        input_field = wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "input[type='number']")
            )
        )

        input_field.send_keys("Sky")
        time.sleep(1)
        input_field.clear()
        time.sleep(1)
        input_field.send_keys("Pro")

        print("Упражнение 3 выполнено успешно!")

    except Exception as e:
        print(f"Произошла ошибка: {e}")

    finally:
        time.sleep(2)
        driver.quit()


if __name__ == "__main__":
    main()
