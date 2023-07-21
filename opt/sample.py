# Selenium
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
import time

# Chrome Driver
from webdriver_manager.chrome import ChromeDriverManager

# ブラウザインスタンス
#browser = webdriver.Chrome(ChromeDriverManager().install())

driver = webdriver.Chrome()
driver.get('https://www.yahoo.co.jp/')

time.sleep(2)
element = driver.find_element(By.LINK_TEXT, "ファイナンス")
element.click()
time.sleep(5)
driver.quit()


# ブラウザを開く。
# 対象のサイトに遷移する
driver = webdriver.Chrome()
driver.get('https://cha1ra.github.io/scrayping-handson/index.html')

# 入力フォームを選択する
el = driver.find_element(By.CSS_SELECTOR,'#id_text')
# 入力フォーム内をリセットする
el.clear()
# 入力フォームに文字を入力する
el.send_keys("test")
# ボタンを選択する
button = driver.find_element(By.CSS_SELECTOR,'button')
# ボタンをクリックする
button.click()
# id=result にある文章を表示する
print(driver.find_element(By.CSS_SELECTOR,'#result').text)