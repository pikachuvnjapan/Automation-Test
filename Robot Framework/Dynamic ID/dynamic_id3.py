from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 15)

try:
    # Mở trang demo Dynamic Loading (Example 1)
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")
    driver.maximize_window()
    time.sleep(5)
    # Click nút Start để bắt đầu load
    start_btn = driver.find_element(By.CSS_SELECTOR, "#start button")
    start_btn.click()
    time.sleep(5)
    # Chờ phần tử xuất hiện (Hello World!)
    hello_text = wait.until(
        EC.presence_of_element_located((By.ID, "finish"))
    )
    time.sleep(5)
    print("Kết quả sau khi load:", hello_text.text)

finally:
    driver.quit()
