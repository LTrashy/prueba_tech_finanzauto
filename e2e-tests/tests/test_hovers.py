from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC

def test_hovers(driver, wait):
    driver.get("https://the-internet.herokuapp.com/hovers")
    figure = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "figure")))[0]
    ActionChains(driver).move_to_element(figure).perform()
    caption = figure.find_element(By.CLASS_NAME, "figcaption")
    assert caption.is_displayed()
