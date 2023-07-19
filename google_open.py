# Selenium
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

# Chrome Driver
from webdriver_manager.chrome import ChromeDriverManager

# ブラウザインスタンス
browser = webdriver.Chrome(ChromeDriverManager().install())

# リンクを開く
browser.get("https://www.google.co.jp/")