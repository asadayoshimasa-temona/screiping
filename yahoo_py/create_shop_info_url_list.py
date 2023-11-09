from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
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


response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
search_results_count = soup.find(class_='SearchResultsDisplayOptions_SearchResultsDisplayOptions__count__WBsPf')
print(search_results_count.get_text().replace(",", "").replace("件", ""))
# 件数を取得し、数値型に変換
# 10回スクロールさせるところをこの数/30に変更すれば自動化いけるか


# 10回スクロールする
for _ in range(3):
    # driver.find_element_by_tag_name('body').send_keys(Keys.END)
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)

    time.sleep(1)  # ページがロードされるのを待つ

# BeautifulSoupを使用してページの内容を解析
soup = BeautifulSoup(driver.page_source, 'html.parser')

# SearchResultItemStore_SearchResultItemStore__rXVLG クラスを持つ要素の href を取得
# hrefs = [elem.get('href') for elem in soup.select('.SearchResultItemStore_SearchResultItemStore__rXVLG')]
matching_hrefs = [elem.get('href') for elem in soup.select('.SearchResultItemStore_SearchResultItemStore__rXVLG') if elem.get('href').startswith('https://store.shopping.yahoo.co.jp/')]
non_matching_hrefs = [elem.get('href') for elem in soup.select('.SearchResultItemStore_SearchResultItemStore__rXVLG') if not elem.get('href').startswith('https://store.shopping.yahoo.co.jp/')]

# Write the matching hrefs to list.txt
with open('shop_info_url_list.txt', 'w') as file:
    for href in matching_hrefs:
        file.write(href + "info.html" + "\n")

# Write the non-matching hrefs to list_ex.txt
with open('exception_shop_info_url_list.txt', 'w') as file:
    for href in non_matching_hrefs:
        file.write(href + "\n")

# ブラウザを閉じる
driver.quit()