# Robot Framework
Thư mục làm việc của Framework Robot Framework
## Các thư viện cần cài đặt
```Shell
# Cài thư viện selenium
pip install selenium

# Cài đặt WebDriver tự động cho Selenium
pip install webdriver-manager

```

## Cài đặt WebDriver thủ công cho Selenium

### 1. Chrome (ChromeDriver)

Kiểm tra phiên bản Chrome trên máy: 

Vào 
```Shell
chrome://settings/help 
```

để xem số phiên bản (ví dụ: 131.0.xxxx).

Tải ChromeDriver tương ứng từ trang chính thức: 

https://chromedriver.chromium.org/downloads

Giải nén file `chromedriver.exe` và đặt vào thư mục trong PATH (ví dụ: C:\WebDriver\bin).

Kiểm tra bằng lệnh:

```Shell
chromedriver --version
```
### 2. Firefox (GeckoDriver)
Tải GeckoDriver từ GitHub:

 https://github.com/mozilla/geckodriver/releases

Giải nén và thêm vào PATH.

Selenium sẽ tự động nhận khi bạn dùng webdriver.Firefox().

### 3. Edge (EdgeDriver)

Tải EdgeDriver từ:

https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/

Đặt file vào thư mục PATH.

📌 Ví dụ Python với ChromeDriver

```Shell
from selenium import webdriver
from selenium.webdriver.common.by import By

# Khởi tạo Chrome WebDriver
driver = webdriver.Chrome()

driver.get("https://www.google.com")
print("Tiêu đề trang:", driver.title)

driver.quit()

```




