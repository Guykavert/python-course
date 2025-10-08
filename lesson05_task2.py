from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def main():
    # Настройка драйвера Chrome
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
    try:
        # Переход на страницу
        driver.get("http://uitestingplayground.com/dynamicid")
        
        # Ожидание загрузки страницы
        time.sleep(2)
        
        # Поиск кнопки по тексту или классу (кнопка без статического ID)
        blue_button = driver.find_element(By.CSS_SELECTOR, "button.btn-primary")
        blue_button.click()
        
        print("Упражнение 2 выполнено успешно!")
        
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        
    finally:
        # Закрытие браузера
        driver.quit()

if __name__ == "__main__":
    main()
    