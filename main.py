import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome();
# 前往要去的網站
driver.get('https://tixcraft.com/activity/detail/24_ive')
# https://tixcraft.com/activity/detail/24_rod
# https://tixcraft.com/activity/detail/24_ive

driver.maximize_window()

# 使用 WebDriverWait 等待畫面載入完成按下會員登入按鈕
login_btn = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="bs-navbar"]/div/div[2]/ul[3]/li/a'))
)
driver.execute_script("arguments[0].click();", login_btn)

# 使用 Facebook 登入
login_btn = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="loginFacebook"]'))
)
driver.execute_script("arguments[0].click();", login_btn)

# 找到輸入框並輸入帳號密碼
username_box = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="email"]'))
)
username = input('請輸入帳號：')
username_box.send_keys(username)

password_box = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="pass"]'))
)
password = input('請輸入密碼：')
password_box.send_keys(password)

# 點擊登入按鈕
login_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="loginbutton"]'))
)
login_button.click()

# 按下立即購票按鈕
buy_ticket_btn = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="tab-func"]/li[1]/a'))
)
driver.execute_script("arguments[0].click();", buy_ticket_btn)

# 按下立即訂購按鈕
place_order_btn = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="gameList"]/table/tbody/tr[1]/td[4]/button'))
)
driver.execute_script("arguments[0].click();", place_order_btn)

while True:
    try:
        # 使用 XPath 來定位到包住所有位置的 div
        all_seats_div = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="selectseat"]/div/div[2]/div[2]'))
        )

        seats = all_seats_div.find_elements(By.TAG_NAME, 'a')

        if seats:
            firstSeat = seats[0]
            # firstSeat.click()
            driver.execute_script("arguments[0].click();", firstSeat)
            time.sleep(10)
            break
        else:
            print("找不到 <a> 標籤，將在一段時間後重新尋訪。")
            driver.refresh()  # 刷新頁面
    except NoSuchElementException:
        print("發生意外，終止程式")