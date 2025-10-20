from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_wait_for_images():
    driver = webdriver.Firefox()
    
    try:
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")
        time.sleep(10)
        
        images = driver.find_elements(By.TAG_NAME, "img")
        print(images[2].get_attribute("src"))
        
    except Exception as e:
        print("Ошибка:", e)
    finally:
        driver.quit()

if __name__ == "__main__":
    test_wait_for_images()
