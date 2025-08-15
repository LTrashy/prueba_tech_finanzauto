from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def test_login_success(driver, wait):
    driver.get("https://the-internet.herokuapp.com/login")
    wait.until(EC.presence_of_element_located((By.ID, "username"))).send_keys("tomsmith")
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    flash = wait.until(EC.presence_of_element_located((By.ID, "flash"))).text
    assert "You logged into a secure area!" in flash
