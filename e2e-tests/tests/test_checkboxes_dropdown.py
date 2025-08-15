from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def test_checkboxes(driver, wait):
    driver.get("https://the-internet.herokuapp.com/checkboxes")
    checkbox1 = wait.until(EC.element_to_be_clickable((By.XPATH, "//form/input[1]")))
    if not checkbox1.is_selected():
        checkbox1.click()
    assert checkbox1.is_selected()

def test_dropdown(driver, wait):
    driver.get("https://the-internet.herokuapp.com/dropdown")
    dropdown = wait.until(EC.element_to_be_clickable((By.ID, "dropdown")))
    dropdown.click()
    option = driver.find_element(By.CSS_SELECTOR, "#dropdown option[value='1']")
    option.click()
    assert option.is_selected()
