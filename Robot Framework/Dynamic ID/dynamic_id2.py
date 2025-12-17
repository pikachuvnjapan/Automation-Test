from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

try:
    # Mở trang demo Dynamic Controls
    driver.get("https://the-internet.herokuapp.com/dynamic_controls")
    driver.maximize_window()
    time.sleep(5)

    # Click nút Remove để xóa checkbox
    remove_btn = driver.find_element(By.XPATH, "//button[contains(text(),'Remove')]")
    remove_btn.click()
    time.sleep(5)

    # Chờ thông báo xuất hiện
    message = wait.until(EC.presence_of_element_located((By.ID, "message")))
    print("Thông báo sau khi Remove:", message.text)
    time.sleep(5)

    # Click nút Add để thêm lại checkbox
    add_btn = driver.find_element(By.XPATH, "//button[contains(text(),'Add')]")
    add_btn.click()
    time.sleep(5)

    # Chờ checkbox xuất hiện lại (ID sẽ thay đổi động)
    checkbox = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='checkbox']")))
    checkbox.click()
    time.sleep(5)
    print("✅ Checkbox đã được chọn thành công với dynamic ID.")
    

finally:
    driver.quit()
