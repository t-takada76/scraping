import time
import traceback
import chromedriver_binary
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


options = Options()
driver = webdriver.Chrome(options=options)

# yahooにアクセス
driver.get("https://www.yahoo.co.jp/")
# 描画待ち
time.sleep(2)
# 検索ボックスに入力
driver.find_element_by_id("srchtxt").send_keys('python')
# 検索ボタンクリック
driver.find_element_by_id("srchbtn").click()
# 描画待ち
time.sleep(2)

# aタグを抽出・出力
for elem in driver.find_elements_by_css_selector("#WS2m .w .hd a"):
    print(elem.text) 
    print(elem.get_attribute("href"))

# ブラウザを閉じる
driver.quit()
