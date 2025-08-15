from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def test_dynamic_controls(driver, wait):
    driver.get("https://the-internet.herokuapp.com/dynamic_controls")
    enable_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Enable']")))
    enable_button.click()
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#input-example input")))

def test_dynamic_loading_1(driver, wait):
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")
    driver.find_element(By.TAG_NAME, "button").click()
    finish = wait.until(EC.visibility_of_element_located((By.ID, "finish")))
    assert finish.text == "Hello World!"

def test_dynamic_loading_2(driver, wait):
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")
    driver.find_element(By.TAG_NAME, "button").click()
    finish = wait.until(EC.visibility_of_element_located((By.ID, "finish")))
    assert finish.text == "Hello World!"
