from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://checkout.stripe.dev/checkout")  # thay bằng URL sandbox của bạn
driver.maximize_window()

# Lấy tất cả iframe trên trang
iframes = driver.find_elements(By.TAG_NAME, "iframe")

print("Tổng số iframe tìm thấy:", len(iframes))
for idx, iframe in enumerate(iframes):
    try:
        # In ra các thuộc tính quan trọng để bạn nhận diện
        print(f"Iframe {idx}:")
        print(" - name:", iframe.get_attribute("name"))
        print(" - id:", iframe.get_attribute("id"))
        print(" - title:", iframe.get_attribute("title"))
        print(" - src:", iframe.get_attribute("src"))
    except Exception as e:
        print(f"Iframe {idx}: lỗi đọc thuộc tính ({e})")

driver.quit()
