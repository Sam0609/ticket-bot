import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome();
# 前往要去的網站
driver.get('https://tixcraft.com/activity/detail/24_ive')

driver.maximize_window()

# 使用 WebDriverWait 等待畫面載入完成按下立即購票按鈕
buyTicketBtn = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="tab-func"]/li[1]/a'))
)
driver.execute_script("arguments[0].click();", buyTicketBtn)

# 使用 WebDriverWait 等待畫面載入完成按下立即訂購按鈕
placeOrderBtn = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="gameList"]/table/tbody/tr[1]/td[4]/button'))
)
driver.execute_script("arguments[0].click();", placeOrderBtn)

seats = driver.find_elements(By.XPATH, '//*[@id="selectseat"]/div/div[2]')

time.sleep(10)

while True:
    try:
        # 假設你的 div 有一個特定的 CSS class
        div = driver.find_element(By.CSS_SELECTOR, '#selectseat > div > div.area_select.col-lg-5.col-md-5.col-sm-5.col-xs-12.col-12.mgt-32.line-lf')

        # 獲取 div 內的所有元素
        elements = div.find_elements(".//*")

        # 尋訪每一個元素
        # for element in elements:
        #     # 如果元素是 enabled，那麼就 click 它
        #     if element.is_enabled():
        #         element.click()
        #         break
    except NoSuchElementException:
        # 如果沒有找到 div 或元素，那麼就繼續 loop
        continue