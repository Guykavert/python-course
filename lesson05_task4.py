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
        driver.get("http://the-internet.herokuapp.com/login")

        wait = WebDriverWait(driver, 10)

        username_field = wait.until(
            EC.presence_of_element_located((By.ID, "username"))
        )
        username_field.send_keys("tomsmith")

        password_field = driver.find_element(By.ID, "password")
        password_field.send_keys("SuperSecretPassword!")

        login_button = driver.find_element(
            By.CSS_SELECTOR, "button[type='submit']"
        )
        login_button.click()

        success_message = wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "div.flash.success")
            )
        )
        message_text = success_message.text
        print("Текст сообщения:", message_text)

        print("Упражнение 4 выполнено успешно!")

    except Exception as e:
        print(f"Произошла ошибка: {e}")

    finally:
        time.sleep(2)
        driver.quit()


if __name__ == "__main__":
    main()
