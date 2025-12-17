from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

driver.get("https://checkout.stripe.dev/checkout")
driver.maximize_window()

# Switch vào iframe chứa form
iframes = driver.find_elements(By.TAG_NAME, "iframe")
driver.switch_to.frame(iframes[1])

# Tìm input email bằng XPath chứa ID động
email_input = wait.until(EC.presence_of_element_located(
    (By.XPATH, "//input[contains(@id, 'email') or @name='email']")
))
email_input.send_keys("testuser@example.com")
