from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

try:
    # Mở trang Stripe Checkout sandbox
    driver.get("https://checkout.stripe.dev/checkout")
    driver.maximize_window()
    time.sleep(5)

    # Lấy danh sách iframe
    iframes = driver.find_elements(By.TAG_NAME, "iframe")
    print("Tổng số iframe:", len(iframes))

    # Switch vào iframe số 1 (inner checkout)
    driver.switch_to.frame(iframes[1])
    time.sleep(5)
    # Nhập email
    email_input = wait.until(EC.presence_of_element_located((By.NAME, "email")))
    email_input.send_keys("testuser@example.com")
    time.sleep(5)
    # Nhập số thẻ test
    card_number = wait.until(EC.presence_of_element_located((By.NAME, "cardNumber")))
    card_number.send_keys("4242424242424242")
    time.sleep(5)
    # Nhập ngày hết hạn
    exp_date = wait.until(EC.presence_of_element_located((By.NAME, "cardExpiry")))
    exp_date.send_keys("12/30")
    time.sleep(5)
    # Nhập CVC
    cvc = wait.until(EC.presence_of_element_located((By.NAME, "cardCvc")))
    cvc.send_keys("123")
    time.sleep(5)
    # Nhập tên chủ thẻ
    name_input = wait.until(EC.presence_of_element_located((By.NAME, "shippingName")))
    name_input.send_keys("Test User")
    time.sleep(5)
    # Điền Address line 1
    address1 = wait.until(EC.presence_of_element_located((By.NAME, "shippingAddressLine1")))
    address1.send_keys("123 Main Street")
    time.sleep(5)
    # Điền Address line 2
    address2 = wait.until(EC.presence_of_element_located((By.NAME, "shippingAddressLine2")))
    address2.send_keys("Apt 4B")
    time.sleep(5)
    # Điền City
    city = wait.until(EC.presence_of_element_located((By.NAME, "shippingLocality")))
    city.send_keys("Ho Chi Minh")
    time.sleep(5)
    # Điền ZIP
    zip_code = wait.until(EC.presence_of_element_located((By.NAME, "shippingPostalCode")))
    zip_code.send_keys("700000")
    time.sleep(5)
    # Chọn State từ dropdown
    state_dropdown = wait.until(EC.presence_of_element_located((By.NAME, "shippingAdministrativeArea")))
    Select(state_dropdown).select_by_visible_text("California")  # hoặc tên tỉnh phù hợp
    time.sleep(5)
    # Nhấn nút thanh toán
    pay_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
    pay_button.click()
    time.sleep(5)

    print("✅ Stripe checkout sandbox chạy thành công (demo).")
    time.sleep(5)

finally:
    driver.quit()
