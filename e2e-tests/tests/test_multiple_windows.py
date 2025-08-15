from selenium.webdriver.common.by import By

def test_multiple_windows(driver):
    driver.get("https://the-internet.herokuapp.com/windows")
    driver.find_element(By.LINK_TEXT, "Click Here").click()
    driver.switch_to.window(driver.window_handles[1])
    assert "New Window" in driver.page_source
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
