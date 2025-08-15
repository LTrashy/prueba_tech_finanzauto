import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def test_file_upload(driver, wait):
    driver.get("https://the-internet.herokuapp.com/upload")
    file_path = os.path.abspath("tests/sample.txt")
    driver.find_element(By.ID, "file-upload").send_keys(file_path)
    driver.find_element(By.ID, "file-submit").click()
    uploaded = wait.until(EC.presence_of_element_located((By.ID, "uploaded-files"))).text
    assert "sample.txt" in uploaded
