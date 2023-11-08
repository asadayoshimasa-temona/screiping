# import requests
# from bs4 import BeautifulSoup

# # URLを指定
# url = 'https://shopping.yahoo.co.jp/category/2496/list?p=&area=13&astk=&first=1&ss_first=1&ts=1699412102&mcr=b80fa60dde8057ac1d85b8b4167e0ffc&tab_ex=commerce&sretry=1&sc_i=shp_pc_search_searchBox_2&sretry=1'

# # URLからページの内容を取得
# response = requests.get(url)

# # BeautifulSoupオブジェクトを作成し、パーサーを指定
# soup = BeautifulSoup(response.text, 'html.parser')

# # SearchResultItemStore_SearchResultItemStore__rXVLG クラスを持つ要素の href を取得
# hrefs = [elem.get('href') for elem in soup.select('.SearchResultItemStore_SearchResultItemStore__rXVLG')]

# # 結果をコンソールに表示
# for href in hrefs:
#     print(href)




# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service  # Serviceをインポート
# from selenium.webdriver.chrome.options import Options  # Optionsをインポート
# from selenium.webdriver.common.keys import Keys
# from bs4 import BeautifulSoup
# import time

# # WebDriverのパスを指定（Chromeの場合）
# chromedriver_path = '/path/to/your/chromedriver'  # 実際のパスに置き換えてください

# # ChromeOptionsを設定（必要に応じて）
# options = Options()
# # options.add_argument('--headless')  # ヘッドレスモードで実行する場合など

# # WebDriverのServiceオブジェクトを作成
# service = Service(executable_path=chromedriver_path)

# # WebDriverを起動
# # driver = webdriver.Chrome(service=service, options=options)
# driver = webdriver.Chrome



from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

# ChromeOptionsを設定（必要に応じて）
options = Options()
options.add_argument('--headless')  # ヘッドレスモードで実行。
options.add_argument('--no-sandbox')  # OSのセキュリティモデルをバイパス。
options.add_argument('--disable-dev-shm-usage')
# options.add_argument('--headless')  # ヘッドレスモードで実行する場合など

# WebDriverのServiceオブジェクトを作成
# 実際のchromedriverのパスに置き換えてください
service = Service(executable_path='/usr/bin/chromedriver')

# WebDriverを起動
driver = webdriver.Chrome(service=service, options=options)

# URLを開く
url = 'https://shopping.yahoo.co.jp/category/2496/list?p=&area=13&astk=&first=1&ss_first=1&ts=1699412102&mcr=b80fa60dde8057ac1d85b8b4167e0ffc&tab_ex=commerce&sretry=1&sc_i=shp_pc_search_searchBox_2&sretry=1'
driver.get(url)

# 10回スクロールする
for _ in range(10):
    # driver.find_element_by_tag_name('body').send_keys(Keys.END)
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)

    time.sleep(1)  # ページがロードされるのを待つ

# BeautifulSoupを使用してページの内容を解析
soup = BeautifulSoup(driver.page_source, 'html.parser')

# SearchResultItemStore_SearchResultItemStore__rXVLG クラスを持つ要素の href を取得
hrefs = [elem.get('href') for elem in soup.select('.SearchResultItemStore_SearchResultItemStore__rXVLG')]

# 結果をコンソールに表示
# for href in hrefs:
#     print(href)
with open('list.txt', 'w') as file:
    for href in hrefs:
        file.write(href + "\n")
        
# ブラウザを閉じる
driver.quit()
