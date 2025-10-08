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
        driver.get("http://the-internet.herokuapp.com/inputs")
        
        # Ожидание загрузки страницы
        time.sleep(2)
        
        # Поиск поля ввода
        input_field = driver.find_element(By.CSS_SELECTOR, "input[type='number']")
        
        # Ввод текста "Sky"
        input_field.send_keys("Sky")
        time.sleep(1)
        
        # Очистка поля
        input_field.clear()
        time.sleep(1)
        
        # Ввод текста "Pro"
        input_field.send_keys("Pro")
        time.sleep(1)
        
        print("Упражнение 3 выполнено успешно!")
        
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        
    finally:
        # Закрытие браузера
        driver.quit()

if __name__ == "__main__":
    main()
    