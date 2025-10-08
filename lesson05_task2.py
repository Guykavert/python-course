from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

import time


def main():
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=chrome_options)

    try:
        driver.get("http://uitestingplayground.com/dynamicid")

        wait = WebDriverWait(driver, 10)
        blue_button = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn-primary"))
        )
        blue_button.click()

        print("Упражнение 2 выполнено успешно!")

    except Exception as e:
        print(f"Произошла ошибка: {e}")

    finally:
        time.sleep(2)
        driver.quit()


if __name__ == "__main__":
    main()
