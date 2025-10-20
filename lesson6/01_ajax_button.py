from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_ajax_button():
    driver = webdriver.Firefox()
    
    try:
        driver.get("http://uitestingplayground.com/ajax")
        time.sleep(3)
        
        button = driver.find_element(By.ID, "ajaxButton")
        button.click()
        
        time.sleep(25)
        element = driver.find_element(By.XPATH, "//*[contains(text(), 'Data loaded')]")
        print(element.text)
        
    except Exception as e:
        print("Ошибка:", e)
    finally:
        driver.quit()

if __name__ == "__main__":
    test_ajax_button()
    
