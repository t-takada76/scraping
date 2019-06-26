import time
import csv
import chromedriver_binary
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from datetime import datetime

options = Options()
# ヘッドレスモードを有効化
options.add_argument('--headless')
# WebDriverオブジェクトを作成
driver = webdriver.Chrome(options=options)

# Googleのトップ画面を開く
driver.get('https://www.google.co.jp/')

# 検索ウィンドウに入力してエンター
input_element = driver.find_element_by_name('q')
input_element.send_keys('Python')
input_element.send_keys(Keys.RETURN)

# 描画待ち
time.sleep(2)

# ページの縦・横のサイズを取得してウィンドウサイズを変更
page_width = driver.execute_script('return document.body.scrollWidth')
page_height = driver.execute_script('return document.body.scrollHeight')
driver.set_window_size(page_width, page_height)

# 現在時刻を取得
now = datetime.now()
# スクリーンショット格納先
path = "C:\python\Scraping\ScreenShot\search_results_" + now.strftime("%Y%m%d_%H%M%S") + ".png"
# スクリーンショットを撮る
driver.save_screenshot(path)
# ファイルオープン
f = open('search_result.csv', 'a')
writer = csv.writer(f, lineterminator='\n')
# ファイルに追記
writer.writerow([now.strftime("%Y/%m/%d %H:%M:%S")])

# 検索結果を出力
for a in driver.find_elements_by_css_selector('.rc > .r > a:first-child'):
    data = []
    text = a.find_elements_by_css_selector('h3')[0].text
    href = a.get_attribute('href')
    print(text)
    print(href)
    data.append(text)
    data.append(href)
    # ファイルに追記
    writer.writerow(data)

# 最終行に追記
writer.writerow('')
# ファイルクローズ
f.close()
# ブラウザを終了
driver.quit()
