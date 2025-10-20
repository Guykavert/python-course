from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_rename_button():
    driver = webdriver.Firefox()
    
    try:
        driver.get("http://uitestingplayground.com/textinput")
        time.sleep(3)
        
        input_field = driver.find_element(By.ID, "newButtonName")
        input_field.clear()
        input_field.send_keys("SkyPro")
        
        button = driver.find_element(By.ID, "updatingButton")
        button.click()
        
        time.sleep(2)
        print(button.text)
        
    except Exception as e:
        print("Ошибка:", e)
    finally:
        driver.quit()

if __name__ == "__main__":
    test_rename_button()
