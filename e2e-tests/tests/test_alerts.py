from selenium.webdriver.common.by import By

def test_js_alert(driver):
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']").click()
    alert = driver.switch_to.alert
    alert.accept()
    assert "You successfully clicked an alert" in driver.find_element(By.ID, "result").text
