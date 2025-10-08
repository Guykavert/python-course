from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
import time

def main():
    # Настройка драйвера Firefox
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    
    try:
        # Переход на страницу
        driver.get("http://the-internet.herokuapp.com/login")
        
        # Ожидание загрузки страницы
        time.sleep(2)
        
        # Ввод username
        username_field = driver.find_element(By.ID, "username")
        username_field.send_keys("tomsmith")
        
        # Ввод password
        password_field = driver.find_element(By.ID, "password")
        password_field.send_keys("SuperSecretPassword!")
        
        # Нажатие кнопки Login
        login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        login_button.click()
        
        # Ожидание загрузки следующей страницы
        time.sleep(2)
        
        # Получение текста с зеленой плашки
        success_message = driver.find_element(By.CSS_SELECTOR, "div.flash.success")
        message_text = success_message.text
        print("Текст сообщения:", message_text)
        
        print("Упражнение 4 выполнено успешно!")
        
    except Exception as e:
        print(f"Происзошла ошибка: {e}")
        
    finally:
        # Закрытие браузера
        driver.quit()

if __name__ == "__main__":
    main()
    